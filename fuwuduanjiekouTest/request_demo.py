from mitmproxy import http

# #request 方法名称不能修改
# def request(flow:http.HTTPFlow):
#     #增加请求的头信息中的字段
#     flow.request.headers["myheader"]="feier"
#     print(flow.request.headers)


def request(flow:http.HTTPFlow):
    #发起请求，判断url是不是预期的url
    if flow.request.pretty_url=="https://www.baidu.com/":
        #创造一个response
        flow.response=http.HTTPResponse.make(
        200,#optional status code
        b"Hello wordl", #content
        {"Content-Type":"text/html"}#optional headers
        )
