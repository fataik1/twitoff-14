# twitoff-14


#Installation

Todo : clone the repo
## Setup
# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables

##Usage

```sh
#windows version
set FLASK_APP=web_app
flask run 
```