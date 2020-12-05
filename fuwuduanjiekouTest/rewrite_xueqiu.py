from mitmproxy import http
import json

def response(flow:http.HTTPFlow):
    #发起请求，判断url是不是预期的url
    if "quote.json" in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
        #把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        #json path   $['store']['book'][0]['title']
        #修改第一支股票的名称
        data['data']['items'][1]['quote']['name'] *=2
        data['data']['items'][2]['quote']['name']=''

        #把修改后的内容赋值给response原始数据格式
        flow.response.text = json.dumps(data)