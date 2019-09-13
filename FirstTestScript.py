import json
import datetime
import urllib2
from selenium import webdriver
import time

from  FirstTestData import testCase as TestCase, webSiteData as UrlDate

class WebTest():
    def _init__(self):
        self.log=None
        self.driver= None

    def testStep(self,driver,steps):
        """
        test actions in this testcases
        :type driver: webdriver
        :type steps: test steps
        :rtype: res: result info
        """
        res='Passed'
        for step in steps:
            if "Play" in step.keys() or "Pause" in step.keys():
                try:
                    self.log.debug(str(datetime.datetime.now())+' Current step:'+ str(step))
                    if list(step)[0]=="Play":
                        script=step["Play"]
                    else:
                        script=step["Pause"]
                        # use javascript to play
                    driver.execute_script(script)
                    #driver.execute_script("document.getElementsByClassName('video-player__play-pause-icon')[0].click()")
                    time.sleep(15)
                except Exception as e:
                    self.log.error(str(datetime.datetime.now())+' Error in testStep: '+ str(e))
                    if driver:
                        driver.save_screenshot("./report1/stepError.png")
                    res="Failed"
            elif "Wait" in step.keys():
                self.log.debug(str(datetime.datetime.now())+' Current step:'+ str(step))
                time.sleep(step["Wait"])

            if res=="Failed":
                break

        return res

    def testAction(self,runnnigLog):
        """
        test actions in this testcases
        :type runningLog: the log file
        :rtype: None
        """
        self.log=runnnigLog
        # check TestCase
        if not TestCase:
            self.log.info(str(datetime.datetime.now())+'  No testcase need to be tested!')
            assert(False,'No testDate')
        # get URL
        try:
            url=UrlDate['url']
            self.log.info(str(datetime.datetime.now())+'  Testing URL : '+ str(url))
        except Exception as e:
            self.log.error(str(datetime.datetime.now())+'  Error in URL: '+ str(e))
            assert(False,'  Error in url data ')

        # get webDriver and run test
        browser=''
        result="Failed"
        try:
            browser= webdriver.Chrome('./ChromDriver/chromedriver.exe')
            browser.maximize_window()
            time.sleep(5)
            browser.get(url)
            time.sleep(90)
            for steps in TestCase:
                result=self.testStep(browser,steps)
                if result=="Failed":
                    break
        except Exception as e:
            self.log.error(str(datetime.datetime.now())+'  Error in Testing: '+ str(e))
            if browser:
                browser.save_screenshot("./report1/ErrorTest.png")
        finally:
            browser.close()
            browser.quit()
            self.log.info("\n---------The test case "+str(result)+"------------\n")






