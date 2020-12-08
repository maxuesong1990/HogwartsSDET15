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

    # 40071 UserTag Name Already Exist
    # 删除对应的tag（推荐使用此方法）
    # 已有的tag_name的基础上追加名字（时间戳，计数器）
    def test_add_tag(self):
        # todo：测试数据要放到测试文件中
        group_name="TMP00123"
        tag=[{"name": "TAg4"}, {"name": "TAg1"}]
        r= self.tag.add(group_name=group_name,tag=tag)
        assert  r.status_code==200
        assert  r.json()["errcode"]==0

    def test_add_before_detect(self):
        group_name = "TMP00123"
        tag = [{"name": "TAg9"}, {"name": "TAg16"}]
        r= self.tag.add_add_detect(group_name, tag)
        assert  r

    def test_list(self):
        self.tag.list()

   #"errcode": 40068,    #"errcode": 40068
   #0、添加tag
   #1、删除tag 有问题
   #2、再进行重试（重试次数为n）：手动实现，借助pytest 钩子（rerun插件）
    # a。 添加一个接口
    # b。 对新添加对接口再删除
    # c。 查询是否成功
    def test_delete_group(self):
        self.tag.delete_group(["etaHZMCAAAecj2j_QH-V4asBAc9jwBNQ"])

    def test_delete_tag(self):
        self.tag.delete_tag(["etaHZMCAAANcHqEm1br72yrdp7G7Zqvg"])

