
import json
import datetime
import urllib2
import SecondTestData

def testAudio(runningLog,audUrl):
    """
    test audio url
    :type runningLog: the log file
    :type audUrl: the audio url to be tested
    :rtype: validation result: Failed/Passed
    """
    vaild='Failure'

    try:
        runningLog.debug(str(datetime.datetime.now())+'  start testing Audio URL : '+ str(audUrl))
        # access the url
        Status=urllib2.urlopen(audUrl).getcode()
        if Status==200:
            vaild="Pass"
    except Exception as e:
        runningLog.debug(str(datetime.datetime.now())+'  The Audio test failed : '+str(e))
    finally:
        runningLog.debug(str(datetime.datetime.now())+'  The Audio testing finished on '+str(audUrl))
        return vaild


def outResult(runningLog,results):
    """
    add  audio url test into log file
    :type runningLog: the log file
    :type results: the result list
    :rtype: None
    """
    runningLog.info('')
    runningLog.info('---------------The Validation Result-------------')
    for v in results:
        runningLog.info(str(v[0]) + ':' +str(v[1])+ '  on '+ str(v[2]))
    runningLog.info('---------------The Validation Result-------------')
    runningLog.info('')

def testAction(runningLog):
    """
    test actions in this testcases
    :type runningLog: the log file
    :rtype: None
    """
    # get test parameters
    try:
        url=SecondTestData.TestData['url']
        filetype= SecondTestData.TestData['type']
        runningLog.info(str(datetime.datetime.now())+'  Testing URL : '+ str(url))
        runningLog.info(str(datetime.datetime.now())+'  Excepted file type : '+ str(filetype))
    except Exception as e:
        runningLog.info(str(datetime.datetime.now())+'  Error in testdata: '+ str(e))
        assert(True,'  Error in testdata: ')
    # test API
    testResult=[['API   ', 'Failure', url]]
    try:
        # read a json string from url
        urllink=urllib2.urlopen(url).read()
        #grab result list and validate the content
        result = json.loads(urllink)
        testResult=[['API  ', 'Pass', url]]
        # save the json context in API
        with open('./report2/SecondTaskAPI.txt', 'w') as outfile:
            json.dump(result, outfile)

        # test Audio Url
        for v in result:
            # if no archiveAudio-mp3 in this value,skip this value
            if "archiveAudio" not in v or filetype not in v["archiveAudio"]:
                continue
            valiationFlag=testAudio(runningLog,v["archiveAudio"][filetype])

            testResult.append(['Audio',valiationFlag,v["archiveAudio"][filetype]])

    except Exception as e:
        runningLog.info(str(datetime.datetime.now())+'  Error in validation: '+ str(e))
        assert(True,'  Error in audio validation')

    # output the audio url test result
    outResult(runningLog,testResult)








