"""
作业
新增标签的测试用例
删除标签的测试用例
数据清理过程
"""
import requests
import datetime

def test_tag_add():
    """
    添加企业客户标签
    请求方式: POST(HTTP)
    请求地址:https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?access_token=ACCESS_TOKEN
    :return:
    """
    #获取企业access_token
    corpid="ww99b10de358d81644"
    corpsecret="tUae2U3JmqMvkqX4aOKZzv0EcqHGJJQXYwwZuK7z34M"
    r=requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                        params={"corpid":corpid,
                                "corpsecret":corpsecret})
    assert  r.status_code ==200
    assert r.json()['errcode']==0
    token=r.json()['access_token']

    #获取标签
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
                      params={"access_token":token})
    print(r.json())

    #添加标签
    #tag_name="TAG_NAME_"+str(datetime.datetime)
    tag_name=133321313131
    group_id="etaHZMCAAAA4ctxPvHCOYBTjZRUXvxTQ"
    group_name="python15"
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        params={"access_token":token},
        json={
            "group_id":group_id,
            "group_name":group_name,
            "tag": [{
                "name": tag_name,
            }
            ]
        })


    #删除企业客户标签
    tag='etaHZMCAAAqag-jyWr_y5oYXvHgqA5ng'
    json={
    "tag_id": tag
    #"group_id": ["etaHZMCAAAiHsR_C0iAtzbdg8LAjVYjQ"]
    }
    r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                    params={"access_token":token},json=json)
    # for  tag in r.json()['tag_group']['tag']['id']:
    #     print(tag)

