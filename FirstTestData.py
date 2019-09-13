
webSiteData={
    'url':'https://theworldgame.sbs.com.au/video/1600471107966/belgium-brush-scotland-aside?playlist=match-highlights'
}

testCase=[
    #play the content
    [ {"Play":"document.getElementsByClassName('video-player__play-pause-icon')[0].click()"},
    #{"Play":"document.getElementsByClassName('video-player__play-pause-button button button--clean').click()"},
     {"Wait":80}
    ],
    # pause the ad
    [{"Pause":"document.getElementsByClassName('video-player__play-pause-icon')[0].click()"},
     {"Wait":10}
    ],
    # Click Play after pause
    [{"Play":"document.getElementsByClassName('video-player__play-pause-icon')[0].click()"},
     {"Wait":10}
     ],
    #Wait for the Ad to finish and then pause the content after 3 minutes of playback
    [ {"Wait":10},
      {"Wait":180},
     {"Pause":"document.getElementsByClassName('video-player__play-pause-icon')[0].click()"}
     ],
]
