import requests
import json
#url="http://localhost:9200/engine"
#requests.put(url)
#url="http://localhost:9200/engine/posts/_mapping"
d={"posts":
             {"properties":
                   {"name":{"type":"string"},
                      "suggest":{
                      
                                "type":"completion",
                                "index_analyzer":"simple",
                                "search_analyzer":"simple",
                                "payloads":True
                      
                      }
                   
                   
                   }
              
              }
              
   }
#requests.put(url,data=json.dumps(d))
url="http://locahost:9200/engine/posts/1?refresh=true"
d={ "name":"Journey Unfold","suggest":
                  {"input":["digest", "experiences", "good", "hobby", "life", "people", "study", "talking", "time"],
                  "output":"Choice between an Optimistic yes or Hopeless No Whether to hold on Or let it go",
       "payload":{"authorId":1,"authorName":"Deepshikha","blogUrl":"https://deepshikha3001.wordpress.com/2015/01/02/journey-unfold/"},
       "weight":67

       }
}

{
  "song" : {
        "properties" : {
            "name" : { "type" : "string" },
            "suggest" : { "type" : "completion",
                          "index_analyzer" : "simple",
                          "search_analyzer" : "simple",
                          "payloads" : True
            }
        }
    }
}


url="http://localhost:9200/music/song/1?refresh=true"

requests.put(url,data=json.dumps(d))


d={
    "name" : "Nevermind",
    "suggest" : {
        "input": [ "Nevermind", "Nirvana" ],
        "output": "Nirvana - Nevermind",
        "payload" : { "artistId" : 2321 },
        "weight" : 34
    }
}

url="http://localhost:9200/music/_suggest?pretty"
d={
    "song-suggest" : {
        "text" : "crossroads",
        "completion" : {
            "field" : "suggest"
        }
    }
}





d={
    "name" : "Nevermind",
    "suggest" : {
        "input": [ "Nevermind", "Nirvana" ],
        "output": "Nirvana - Nevermind",
        "payload" : { "artistId" : 2321 },
        "weight" : 34
    }
}
