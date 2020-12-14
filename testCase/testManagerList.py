import os
import unittest
import ddt
import time
from pages.managerListPage import ManagerListPage
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    genrandomstr,
    join_url
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)


@ddt.ddt
class TestManagerList(unittest.TestCase):
    """账号设置"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/manager/list')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*(get_data('managerList', 'CASE1')))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """账号设置"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.mlist = ManagerListPage(self.url, self.driver, data['title'])
        self.mlist.open
        old_num = self.mlist.get_name()
        # 创建帐号
        self.mlist.click_add()
        # 选择角色
        self.mlist.select_role(data['role'])
        # 输入姓名
        self.mlist.input_name(data['inputName'])
        # 输入手机号码
        phone = data['inputPhone'] + str(int(time.time()))
        self.mlist.input_phone(phone)
        # 选择门店
        self.mlist.select_shopselector_and_shopname()
        self.mlist.click_sure()
        # 选择管理权限
        self.mlist.select_userright(data['userRight'])
        # 点击保存
        self.mlist.click_save()
        new_num = self.mlist.get_name()
        self.assertTrue(self.mlist.assertTrue(old_num, new_num))
        # 禁用
        self.mlist.click_remove()
        # 确定
        self.mlist.click_ok()



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestManagerList)
    ]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print(filePath)

    with open(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yecc"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
