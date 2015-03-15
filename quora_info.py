from py2neo import neo4j,cypher
import requests
import json
import re

g=neo4j.GraphDatabaseService()
def getUser(l):
	return l['username']
def filter_sentence(l):
	k=l.split(" ")
	for i in range(len(k)):
		k[i]=re.sub("[^a-zA-Z]","",k[i])
	return " ".join(k)
def createRecord(username):
	l=requests.get("http://quora-api.herokuapp.com/users/"+username+"/activity").json()
	user=getUser(l)
	print cypher.execute(g,"create (n:People {name:'"+user+"'})")
	for i in l['activity']:
		query="create (n:Question {title:'"+filter_sentence(i['title'])+"'})"
		print cypher.execute(g,query)
		nextQuery="match (n:People),(b:Question) where n.name='"+user+"' and b.title='"+filter_sentence(i['title'])+"' create  (n)-[:RELATED_TO]->(b)"
		print cypher.execute(g,nextQuery)
		print query
		#print i['title']
		
createRecord('Novels')
