import re
from py2neo import neo4j,cypher
import requests
import json
def onegramTokenizer(l):
	k=l.split(" ")
	l1=[]
	for i in k:
		if i not in l1:
			l1.append(i)
	return l1
def twogramTokenizer(l):
	k=l.split(" ")
	twogramArray=[]
	for i in range(len(k)-1):
		twogramArray.append((k[i],k[i+1]))
	l1=[]
	for i in twogramArray:
		if i not in l1:
			l1.append(' '.join(i))
			
	return l1
def threegramTokenizer(l):
	k=l.split(" ")
	twogramArray=[]
	for i in range(len(k)-2):
		twogramArray.append((k[i],k[i+1],k[i+2]))
	l1=[]
	for i in twogramArray:
		if i not in l1:
			l1.append(' '.join(i))
			
	return l1

g=neo4j.GraphDatabaseService()
query="match (n:Question)<-[r]-(b) where has (n.category) return n.title,n.category,b.name"
resultSet=cypher.execute(g,query)[0]
count=1
for i in resultSet:
	#try:
		
		#print url
		#print i[0]
		#print onegramTokenizer(i[0])
		onel=onegramTokenizer(i[0])
		twol=twogramTokenizer(i[0])
		threel=threegramTokenizer(i[0])
		#print i[2]
		tax=i[1]
		tax=tax[1:]
		tax=tax[:-1]
		tax=tax.split(",")
		#tax=map(str,tax)
		print tax[0]
		l=twol+threel+onel+tax
		print l
		d={
    "name" : i[0],
    "suggest" : {
        "input":l,
        "output":i[0],
        "payload" : { "artistId" :count,"authorName":i[2] },
        "weight" : count
    }
}
		#print d
		#print type(i[1])
		url="http://localhost:9200/music/song/"+str(count)+"?refresh=true"
		count+=1
		print requests.post(url,data=json.dumps(d))
	#except:
		#continue

