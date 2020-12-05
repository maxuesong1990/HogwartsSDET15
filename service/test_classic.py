"""
服务端接口自动化测试
https://ceshiren.com/t/topic/8664

"""

import requests
import json
import datetime

# todo: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# todo: 代码冗余，需要封装
# todo: 无法清晰的描述业务
# todo: 使用jsonpath表达更灵活的递归查找
"""
上面todo的已完成
PO封装为2个文件
tag.py
test_tag.py
"""

def test_tag_list():
    """
    获取企业标签库
    请求方式: POST(HTTP)
    请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=ACCESS_TOKEN
    """
    corpid='ww99b10de358d81644'
    corpsecret='tUae2U3JmqMvkqX4aOKZzv0EcqHGJJQXYwwZuK7z34M'
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    params={'corpid':corpid ,'corpsecret':corpsecret})
    print(r)
    print(json.dumps(r.json(), indent=2))
    print(r.status_code)
    print(r.json()['errcode'])
    assert  r.status_code ==200
    assert r.json()['errcode']==0

    token=r.json()['access_token']
    print(token)

    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={"access_token":token},
        json={'tag_id':[]}
    )
    print(json.dumps(r.json(), indent=2))
    assert  r.status_code ==200
    assert r.json()['errcode']==0

    """
    编辑企业客户标签
    请求方式: POST(HTTP)
    请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag?access_token=ACCESS_TOKEN
    """
    tag_name="tag1_new"+str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))    #增加时间搓
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        params={"access_token":token},
        json={
            'id':"etaHZMCAAAtY0TRM53ifUizJJBy1hA1Q",
            "name":tag_name
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert  r.status_code ==200
    assert r.json()['errcode']==0

    """
    校验企业客户标签是否编辑成功
    获取企业标签库
    请求方式: POST(HTTP)
    """
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'python15'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    # jsonpath(f"$..[?(@.name='{tag_name}')]") jmepath
    assert tags != []



