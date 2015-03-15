import requests
import sys 
import json
url="http://localhost:9200/music/_suggest?pretty"

d={
    "song-suggest" : {
        "text" : sys.argv[1],
        "completion" : {
            "field" : "suggest"
        }
    }
}

print requests.post(url,data=json.dumps(d)).json()


