#main
import DBAccess
import sys
from urllib.parse import urlparse

def add_tag(tag_name, url, site_name):
    with DBAccess.driver.session() as session:
        session.write_transaction(DBAccess.add_tag,tag_name,url, site_name)

def search_tags(tags):
    with DBAccess.driver.session() as session:
        session.write_transaction(DBAccess.search_tag,tags)

if sys.argv[1].upper() == "N":
    print("Criar novo")
    i=3
    while i<len(sys.argv):
        print(sys.argv[i].upper())
        url = sys.argv[2].upper()
        add_tag(sys.argv[i].upper(), url, urlparse(url).hostname)
        i=i+1

elif sys.argv[1].upper() == "S":
    print("Pesquisa")
    search_tags(sys.argv[2:])
