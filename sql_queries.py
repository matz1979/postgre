# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                    (
                    songplay_id SERIAL PRIMARY KEY,
                    start_time bigint, 
                    user_id integer,
                    level varchar,
                    song_id varchar,
                    artist_id varchar,
                    session_id integer,
                    location varchar,
                    user_agent text
                    );
""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
                    (
                    user_id integer NOT NULL PRIMARY KEY,
                    first_name varchar,
                    last_name varchar,
                    gender varchar,
                    level varchar
                    );
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
                    (
                    song_id varchar NOT NULL PRIMARY KEY,
                    title varchar,
                    artist_id varchar,
                    year integer,
                    duration numeric
                    );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist
                    (
                    artist_id varchar NOT NULL PRIMARY KEY,
                    name varchar,
                    location varchar,
                    latitude numeric,
                    longitude numeric
                    );
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
                    (
                    start_time bigint PRIMARY KEY,
                    hour integer,
                    day integer,
                    week integer,
                    month integer,
                    year integer,
                    weekday varchar
                    );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT ON CONSTRAINT users_pkey DO NOTHING;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s , %s)
                        ON CONFLICT ON CONSTRAINT songs_pkey DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT ON CONSTRAINT artist_pkey DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s ,%s);
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
                FROM songs s
                INNER JOIN artist a ON (s.artist_id = a.artist_id)
                WHERE (s.title = %s AND a.name = %s AND s.duration = %s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
