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

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, artist_id, sesson_id, location, user_agent)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s), ();
""")

user_table_insert = ("""INSERT INTO user (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s), ();
""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s ,%s), ();
""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s), ();
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s ,%s), ();
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
