# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                    (
                    songplay_id SERIAL NOT NULL PRIMARY KEY,
                    start_time bigint REFERENCES time, 
                    user_id integer REFERENCES user,
                    level varchar,
                    song_id varchar REFERENCES song,
                    artist_id varchar REFERENCES artist,
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
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT ON CONSTRAINT songplays_pkey DO NOTHING;
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT DO UPDATE SET level = EXCLUDED.level;
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
                        VALUES (%s, %s, %s, %s, %s, %s ,%s)
                        ON CONFLICT ON CONSTRAINT time_pkey DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT song_id, artist.artist_id
                FROM songs
                INNER JOIN artist ON (songs.artist_id = artist.artist_id)
                WHERE (songs.title = %s AND artist.name = %s AND songs.duration = %s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
