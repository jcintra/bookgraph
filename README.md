# Bookgraph
Play with graphs and bookmarks

Creation of a personal bookmark repository that allows:

- creation of a bookmark given an URL
- extraction of main tags with spaCy
- persistence of information on neo4j database
- search by tag
- search through a graph interface
- edit URL information including tags

Creating a virtual environment (Windows):
- python -m venv env

Activate the venv (Windows):
- env\Scripts\activate.bat

Install neo4j package
- pip install neo4j

Deactivate the venv (Windows):
- deactivate