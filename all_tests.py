# coding=utf-8
import unittest
import time
import HTMLTestRunner
from test_case import baidu,youdao
#把test_case 目录添加到path 下，这里用的相对路径


#将用例组装数组
alltestNames=[
    baidu.Baidu,
    youdao.Youdao
]
# #定义一个测试单元
testunit=unittest.TestSuite()

#循环读取数组中的用例
for test in alltestNames:
    testunit.addTest(unittest.makeSuite(test))

#将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(baidu.Baidu))
# testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)
#取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#定义个报告存放路径，支持相对路径
filename="C:\\selenium\\report\\"+now+'result.html'
fp = file(filename, 'wb')
#定义测试报告
runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况'
    )
runner.run(testunit)

