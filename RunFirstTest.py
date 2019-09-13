"""
Tech test: Frontend
Navigate to this link and automate the player
https://theworldgame.sbs.com.au/video/1600471107966/belgium-brush-scotland-aside?playlist=match-highlights

.Play the content?
.Pause an Ad (pre-roll)
.Click Play after pause
.Wait for the Ad to finish and then pause the content after 3 minutes of playback
author: Yuan LIN
"""

import FirstTestScript
import logging
import datetime
import os


def clearup(runningLog):
    try:
        folder='./report1'
        for file in os.listdir(folder):
            filepath=os.path.join(folder,file)
            os.remove(filepath)
        runningLog.info(str(datetime.datetime.now())+'  removed previous files!!!')
    except Exception as e:
        runningLog.info(str(datetime.datetime.now())+'  Error in clearing up: '+str(e))


logH=logging.getLogger('')
logging.basicConfig(filename='FirstTasklog.log',filemode='w',level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.ERROR)
logH.info(str(datetime.datetime.now())+'  --The First Task started --!!!')
# remove old files
clearup(logH)
# run the test
test= FirstTestScript.WebTest()
test.testAction(logH)
logH.info(str(datetime.datetime.now())+'  --The First Task completed --!!!')

