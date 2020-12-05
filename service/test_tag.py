"""
上面todo的已完成
PO封装为2个文件
tag.py
test_tag.py
"""
"""
服务端接口自动化测试
https://ceshiren.com/t/topic/8664
"""
import requests
import json
import datetime
import pytest
from jsonpath import jsonpath

from service.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag=Tag()

    @pytest.mark.parametrize("tag_id,tag_name",[
                             ['etaHZMCAAAtY0TRM53ifUizJJBy1hA1Q','tag1_new_'],
                             ['etaHZMCAAAtY0TRM53ifUizJJBy1hA1Q','tag1——中文'],
                             ['etaHZMCAAAtY0TRM53ifUizJJBy1hA1Q','tag1[中文]']])
    def test_tag_list(self,tag_id,tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))  # 增加时间搓
        r=self.tag.list()
        r=self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        r=self.tag.list()
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] ==group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        # 同上面注释掉的代码


        print(jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'])
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # assert tags != []

    def test_tag_list_fail(self):
        pass
