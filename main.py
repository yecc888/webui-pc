# _*_coding:utf-8_*_
import unittest
import os
from lib import (HTMLTESTRunnerCN, gl, scripts)
from lib.emailstmp import EmailClass

if __name__ == "__main__":
    # scripts.remove_all_files(gl.imgPath)
    # suite = unittest.TestSuite()
    # suite.addTest(
    #     unittest.defaultTestLoader.discover(gl.casePath, 'test*.py')
    # )
    # filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    # print(filePath)
    #
    # with open(filePath, 'wb') as fp:
    #     runner = HTMLTESTRunnerCN.HTMLTestRunner(
    #         stream=fp,
    #         title=u'UI自动化测试报告',
    #         description=u'详细测试用例结果',  # 不传默认为空
    #         tester="ycc"  # 测试人员名字，不传默认为小强
    #     )
    #     # 运行测试用例
    #     runner.run(suite)
    #
    # EmailClass().send()
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
            title=u'线上商家后台UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester="yhleng; ycc"  # 测试人员名字，不传默认为小强
        )

        # 推测试报告设置
        msg_conf = CONF.read(gl.configFile)['MESSAGE']

        if msg_conf['DING']:
            token = '2c412f54-b815-45c5-b928-8fec114d1ea9'
            from lib.scripts import send_dding_msg

            TMPL_MSG = '{}:★开始Pro商家后台UI自动化测试★'.format(
                time.strftime(r'%Y%m%d_%H%M%S', time.localtime(time.time()))
            )
            send_dding_msg(token, TMPL_MSG)

        # 运行测试用例
        runner.run(suite)

        if msg_conf['DING']:
            TMPL_MSG = '''Pro商家后台UI自动化测试执行【已完成】:\n{}\n测试报告:http://60.205.217.8:5004/pos/pro_manage_web/report'''.format(runner.RESULT)
            send_dding_msg(token, TMPL_MSG)

        if msg_conf['EMAIL']:
            EmailClass().send()

