# Database for a music streaming plattform

The Startup stored the data from their app at the moment as .json files.
Json data are dificult to analyse to make it easier the company hired a data engineer to
create a new database for the company. So that their Data team can analyse the data quickly
and understand the behaviors of the users.

## Steps I take to create the Postgres DB

### Why I choice a SQL Database

    The APP generate always the same data
    New files can be add at the same way without any change
    also the data team can extract the data with simple SQL queries.

### ETL process

* Extracting the data from json file:

  * Read the json files into pandas

* Transforming the data:

  * Bring the data to the 3 Normal Form

  * Create the PostgreSQL Database

  * Create the tables based on the data

* Load the data:
  
  * Load the pandas dataframe into the Database

### The Star schema of the database

![Sparkify Database Schema](sparkify_schema.png)
