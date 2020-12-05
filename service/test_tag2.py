"""
作业
新增标签的测试用例
删除标签的测试用例
数据清理过程
"""
import requests
import datetime
import pytest
from jsonpath import jsonpath

from service.tag2 import Tag2


class TestTag:
    def setup_class(self):
        self.tag2=Tag2()

    @pytest.mark.parametrize("tag_name,group_id,group_name",
                             [['123','etaHZMCAAAA4ctxPvHCOYBTjZRUXvxTQ','python15'],
                              ['333','','']
                              ]
                             )
    def test_tag_add(self, tag_name, group_id, group_name):
        tag_name=tag_name+str((datetime.datetime).now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag2.tag_get()
        r = self.tag2.tag_add(
            tag_name=tag_name,
            group_id=group_id,
            group_name=group_name
        )

    def test_tag_delete(self):
        #删除企业客户标签
        tag_id='etaHZMCAAASpIXVf_4kjZcR-z9vQ5S5Q'
        r= self.tag2.tag_get()
        r= self.tag2.tag_delete(tag_id=tag_id)
        #print(jsonpath(r.json(), f"$..[?(@.id=='{tag_id}')]"))
        assert not jsonpath(r.json(), f"$..[?(@.id=='{tag_id}')]")