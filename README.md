This repository contains a simple setup that allows to quickly rise env for learning SQL.

Before use be sure that:

1. You have installed on your computer 
    - docker https://docs.docker.com/get-docker/
    - docker compose https://docs.docker.com/compose/install/

Only if you want to load example dataset into postgres:
    - Python3 with libraries:
        * sqlalchemy 
        * psycopg2-binary
        * pandas

To raise containers run from a main catalog:
`docker compose up -d`

To load example data run from a main catalog:
`python3 data_import.py`

To login into pgAdmin:
1. open in web browser http://localhost:5050
2. login using user postgres password postgres

When adding server in pgAdmin use those creds
- user: _postgres_ 
- password: _postgres_ 
- database: _postgres_ 
- host: _db_
- port: 5432
 
