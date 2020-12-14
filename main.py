# _*_coding:utf-8_*_
import unittest
import os
from lib import (HTMLTESTRunnerCN, gl, scripts)
from lib.emailstmp import EmailClass

if __name__ == "__main__":
    scripts.remove_all_files(gl.imgPath)
    suite = unittest.TestSuite()
    suite.addTest(
        unittest.defaultTestLoader.discover(gl.casePath, 'test*.py')
    )
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print(filePath)

    with open(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester="ycc"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)

    EmailClass().send()
