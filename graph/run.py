from neo4j.v1 import GraphDatabase, basic_auth
import os

def conn():
    driver = GraphDatabase.driver("bolt://localhost", auth = basic_auth(os.environ['NEO4J_ID'], os.environ['NEO4J_PWD']))
    session = driver.session()
    return session

def insert(session):
    session.run("CREATE (a:Person {name:'Arthur', title:'King'})")

def search(session):
    result = session.run("MATCH (a:Person) WHERE a.name = 'Arthur' RETURN a.name AS name, a.title AS title")
    for record in result:
        print("%s %s" % (record["title"], record["name"]))

session = conn()

insert(session)
search(session)

session.close()
