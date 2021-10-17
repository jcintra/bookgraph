from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "BookGraph"))

def add_tag(tx, tag, url, site):
    tx.run( "MERGE (u:Url {name: $Site, url: $Url})"
            "MERGE (t:Tag {name: $Tag}) "
            "MERGE (u)-[:IDENTIFIES]-(t)", Site=site, Tag=tag, Url=url)

def search_tag(tx, tags):
    query = "MATCH (u:Url)-[:IDENTIFIES]->(t:Tag) where ("
    for t in range(len(tags)):
        if t>0:
            query += " or "
        query += " t.name = '" + tags[t].upper() + "'"
    query += ") return distinct(u.url)"
    for record in tx.run(query):
        print(record)

    
    
    # t.name = "SEARCH" or t.name="ENGINE") return u
    # tx.run(query)

# def add_friend(tx, name, friend_name):
#     tx.run("MERGE (a:Person {name: $name}) "
#            "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
#            name=name, friend_name=friend_name)

# def print_friends(tx, name):
#     for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
#                          "RETURN friend.name ORDER BY friend.name", name=name):
#         print(record["friend.name"])

# with driver.session() as session:
#     session.write_transaction(add_friend, "Arthur", "Guinevere")
#     session.write_transaction(add_friend, "Arthur", "Lancelot")
#     session.write_transaction(add_friend, "Arthur", "Merlin")
#     session.read_transaction(print_friends, "Arthur")

driver.close()