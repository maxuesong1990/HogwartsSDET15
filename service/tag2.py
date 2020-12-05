"""
作业
新增标签的测试用例
删除标签的测试用例
数据清理过程
"""
import requests
import datetime
import pytest
import json

class Tag2():
    def __init__(self):
        self.token=self.get_token()

    def get_token(self):
        #获取企业access_token
        corpid="ww99b10de358d81644"
        corpsecret="tUae2U3JmqMvkqX4aOKZzv0EcqHGJJQXYwwZuK7z34M"
        r=requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                            params={"corpid":corpid,
                                    "corpsecret":corpsecret})
        assert r.status_code ==200
        assert r.json()['errcode']==0
        token = r.json()['access_token']
        return token

    def tag_get(self):
        #获取标签
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                          params={"access_token":self.token})
        print(r.json())
        #print(json.dumps(r.json(), indent=2))
        return r

    def tag_add(self,tag_name,group_id,group_name):
        #添加标签
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token":self.token},
            json = {
                "group_id": group_id,
                "group_name": group_name,
                "tag": [{
                    "name": tag_name,
                }
            ]
        })
        #print(json.dumps(r.json(), indent=2))
        return r

    def tag_delete(self,tag_id):
        #删除企业客户标签
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                        params={"access_token":self.token},
                        json={'tag_id':tag_id})
        #print(json.dumps(r.json(), indent=2))
        return r
