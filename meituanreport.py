import  unittest,time
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    test_dir = (r'F:\appiumtest')
    discover = unittest.defaultTestLoader.discover(test_dir,'*case.py')
    testReportDir = (r'F:\report')
    nowTime = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    fileName = nowTime+".html"
    report_Name = testReportDir+fileName
    fp = open(report_Name,"wb")
    runner = HTMLTestRunner(stream=fp,title="美团自动化测试报告",description="测试结果")
    runner.run(discover)
    fp.close()