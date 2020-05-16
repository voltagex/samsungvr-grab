import m3u8
import json

def grab_video_by_id(id):
    #The page for a video
    #https://samsungvr.com/view/4qXIGUa9bpK

    #The equivalent playlist
    #https://samsungvr.com/cdn/4qXIGUa9bpK/master_list.m3u8


    #Metadata (not all of it)
    #curl 'https://samsungvr.com/graphql?' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://samsungvr.com/view/4qXIGUa9bpK' -H 'content-type: application/json' -H 'Origin: https://samsungvr.com' -H 'Connection: keep-alive' --data-raw '{"operationName":"video","variables":{"id":"4qXIGUa9bpK","commentFirst":30,"commentOffset":0,"recommentFirst":1,"recommentOffset":0},"query":"query video($id: String!, $commentFirst: Int!, $commentOffset: Int) {\n  video(id: $id) {\n    ...VideoFragmentV3\n    downloadableVideo {\n      url\n      fileSize\n      resolutionHorizontal\n      resolutionVertical\n      __typename\n    }\n    reaction(sla: Factual) {\n      mine\n      __typename\n    }\n    audioType\n    isInteractive\n    isLiveStream\n    isEncrypted\n    liveStartScheduled\n    author {\n      ...UserFragmentV4\n      __typename\n    }\n    categories {\n      id\n      name\n      __typename\n    }\n    tags {\n      name\n      __typename\n    }\n    extraDates {\n      published\n      __typename\n    }\n    comments(first: $commentFirst, offset: $commentOffset) {\n      totalCount\n      nodes {\n        ...CommentFragmentV1\n        replies(first: 1, offset: 0) {\n          totalCount\n          nodes {\n            ...CommentFragmentV1\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    recommendedVideos(count: 8) {\n      ...VideoFragmentV3\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VideoFragmentV3 on Video {\n  ...VideoFragmentV2\n  defaultDate\n  commentCount(sla: Factual)\n  reaction(sla: Factual) {\n    like\n    dislike\n    __typename\n  }\n  __typename\n}\n\nfragment VideoFragmentV2 on Video {\n  ...VideoFragmentV1\n  description\n  duration(unit: MILLISECOND)\n  isLivePreview\n  isPremiumContent\n  isPremiumContentPaid\n  liveStartScheduled\n  premiumContentPrice\n  publishStatus\n  stereoscopicType\n  thumbnails {\n    jpgThumbnail720x405\n    __typename\n  }\n  feature {\n    id\n    __typename\n  }\n  trailer {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment VideoFragmentV1 on Video {\n  type\n  id\n  name\n  isLiveStream\n  author {\n    ...UserFragmentV1\n    __typename\n  }\n  __typename\n}\n\nfragment UserFragmentV1 on User {\n  type\n  id\n  name\n  thumbnails {\n    userProfileLight\n    __typename\n  }\n  __typename\n}\n\nfragment UserFragmentV4 on User {\n  ...UserFragmentV3\n  videos(representation: 0) {\n    totalCount\n    __typename\n  }\n  __typename\n}\n\nfragment UserFragmentV3 on User {\n  ...UserFragmentV2\n  description\n  thumbnails {\n    profileBg1440x420\n    __typename\n  }\n  __typename\n}\n\nfragment UserFragmentV2 on User {\n  ...UserFragmentV1\n  followersCount\n  iAmFollowing\n  __typename\n}\n\nfragment CommentFragmentV1 on Comment {\n  id\n  abuseReported\n  author {\n    ...UserFragmentV1\n    __typename\n  }\n  createdAt\n  text\n  renderedText\n  votesUp\n  votesDown\n  votedUp\n  votedDown\n  isRestricted\n  __typename\n}\n"}'
    master = m3u8.load(f"https://samsungvr.com/cdn/{id}/master_list.m3u8")


    #sort by highest bandwidth - i.e. the highest quality video
    master.playlists.sort(key = lambda x: x.stream_info.bandwidth, reverse=True)

    print(f"youtube-dl --output \"{id}.%(ext)s\" {master.playlists[0].absolute_uri}" )
    print(f"sed s/REPLACEME/{id}/g template.videos.graphql.json > {id}.req.videos.json")
    print(f"sed s/REPLACEME/{id}/g template.video.graphql.json > {id}.req.video.json")
    print(f"curl -X POST -H \"Content-Type: application/json\" -d @{id}.req.video.json https://samsungvr.com/graphql > {id}.video.response.json" )
    print(f"curl -X POST -H \"Content-Type: application/json\" -d @{id}.req.videos.json https://samsungvr.com/graphql > {id}.videos.response.json" )




grab_video_by_id("DXRDmxvVhpZ")