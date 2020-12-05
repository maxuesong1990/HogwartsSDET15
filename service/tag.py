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

    def add(self):
        pass

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

    def delete(self):
        pass

