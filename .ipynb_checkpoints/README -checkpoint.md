# Database for a music streaming plattform

The startup has currently saved the data from its app locally as .json files.
Json files are more difficult to analyze and manipulate, storing the data in a database makes it easier. So that your Data team can quickly extract the data and analyze the behaviors of the users.

## Why I choice a SQL Database

The APP generate always the same data
New data can be add easy with a copy command
also the data team can access and manipulate the data with simple SQL queries.

## How to use and explain the files

* Run the ```create_table.py``` to create the database and the tables, that are located in the ```sql_queries.py```.

* Run the ```etl.ipynb``` to extract the first row of the dataset and beginn the ETL process.

* With the ```test.py``` you can check if all tables are complete

* Run the ```etl.py``` to load the whole dataset into the database.

## The Star schema of the database

The Star schema is a simple database schema consists of fact and dimension tables that perform well.
In this schema for the Sparkify DB is the fact table songplays and it has four dimension tables named:

* songplays facttable were stored all ID\`s (songplay_id, user_id, artist_id, ...) Primary key column songplay_id.

* time were stored all time data (hour, day, month, ...) Primary key column start_time.

* users were stored all user data (first name, lastname, ...) Primary key column user_id.

* songs were stored all song data (title, year, ...) Primary key column song_id.

* artist were stored all artist data (name, location, ...) Primary key column artist_id.

![Sparkify Database Schema](sparkify_schem.png)
