
import SecondTestScript
import logging
import datetime
import os


def clearup(runningLog):
    try:
        folder='./report2'
        for file in os.listdir(folder):
            filepath=os.path.join(folder,file)
            os.remove(filepath)
        runningLog.info(str(datetime.datetime.now())+'  removed previous files!!!')
    except Exception as e:
        runningLog.info(str(datetime.datetime.now())+'  Error in clearing up: '+str(e))


logH=logging.getLogger('')
logging.basicConfig(filename='SecTasklog.log',filemode='w',level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logH.info(str(datetime.datetime.now())+'  --The second Task started --!!!')
# remove old files
clearup(logH)
# run the test
SecondTestScript.testAction(logH)
logH.info(str(datetime.datetime.now())+'  --The second Task completed --!!!')

