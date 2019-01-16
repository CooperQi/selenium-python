#coding=utf-8
import unittest
import os,time
import HTMLTestRunner

listaa='test_case/'
def creatsuitel():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,
                                               pattern='start_*.py',
                                               top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

alltestnames = creatsuitel()

now = time.strftime("%y-%m-%d_%H_%M_%S",time.localtime(time.time()))

#filename='report/'+now +'result.html'
filename = 'report/'+now +'result.html'
fp = file(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'翔云系统测试报告',
    description=u'用例测试情况：'
)

runner.run(alltestnames)
