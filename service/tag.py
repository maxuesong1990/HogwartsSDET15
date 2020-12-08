"""
上面todo的已完成
PO封装为2个文件
tag.py
test_tag.py
"""
import json
from datetime import datetime

import requests


class Tag:
    def __init__(self):
        self.token=self.get_token()

    def get_token(self):
        """
        获取企业标签库
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=ACCESS_TOKEN
        """
        corpid = 'ww99b10de358d81644'
        corpsecret = 'tUae2U3JmqMvkqX4aOKZzv0EcqHGJJQXYwwZuK7z34M'
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={'corpid': corpid, 'corpsecret': corpsecret})
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return  token

    #判断group_name是否已经存在
    def find_tag_group_id_by_name(self,group_name):
        for group in  self.list().json()["tag_group"]:
            if group_name  in group["group_name"]:
                return group["group_id"]
        print("group_name not in group")
        return ""

    def add(self,group_name,tag,**kwargs):
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                      params={"access_token": self.token},
                      json={"group_name":group_name,"tag":tag,**kwargs}
            )
        print(json.dumps(r.json(), indent=2))
        return r

    def add_add_detect(self, group_name, tag, **kwargs):
        r =self.add(group_name,tag,**kwargs)
        # 如果删除的元素已经存在
        if r.json()['errcode']==40071:
            group_id=self.find_tag_group_id_by_name(group_name)
            if not group_id:
                return  False
            self.delete_group(group_id)
            self.add(group_name, tag, **kwargs)

        result=self.find_tag_group_id_by_name(group_name)
        if not result:
            print("add not success")
        return result

    def list(self):
        """
        获取企业标签库
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=ACCESS_TOKEN
        """
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={'tag_id': []}
        )
        print(json.dumps(r.json(), indent=2))
        return   r

    def update(self,id,tag_name):
        """
        编辑企业客户标签
        请求方式: POST(HTTP)
        请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?access_token=ACCESS_TOKEN
        """
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={"access_token": self.token},
            json={
                'id': id,
                "name": tag_name
            }
        )
        print(json.dumps(r.json(), indent=2))
        return  r

    #查询 tag_id -> 删除 tag_id
    #如果正常：成功
    # {
    #    "errcode": 0,
    #    "errmsg": "ok"
    # }
    #如果异常：失败（）
    #手动获取
    def delete_group(self,group_id):
    # 删除企业客户标签
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                              params={"access_token": self.token},
                              json={'group_id':group_id}
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_tag(self,tag_id):
    # 删除企业客户标签
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                              params={"access_token": self.token},
                              json={'tag_id':tag_id}
                          )
        print(json.dumps(r.json(), indent=2))
        return r
