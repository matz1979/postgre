# DROP TABLES

songplay_table_drop = ""
user_table_drop = ""
song_table_drop = ""
artist_table_drop = ""
time_table_drop = ""

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                    (songplay_id int, start_time int, user_id, level int, song_id int, artist_id int, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level int)
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id int, title varchar, artist_id int, year int, duration numeric)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist(artist_id int, name varchar, location varchar, latitude numeric, longitude numeric)
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time numeric, hour numeric, day numeric, week numeric, month numeric, year int, weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
""")

user_table_insert = ("""INSERT INTO user
""")

song_table_insert = ("""INSERT INTO song
""")

artist_table_insert = ("""INSERT INTO artist
""")


time_table_insert = ("""INSERT INTO time
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
