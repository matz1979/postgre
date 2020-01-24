# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays
                    (
                    songplay_id int, 
                    start_time timestamp without time zone, 
                    user_id int,
                    level varchar,
                    song_id int,
                    artist_id int,
                    session_id int,
                    location varchar,
                    user_agent varchar,
                    PRIMARY KEY (user_id, song_id, artist_id, start_time),
                    CONSTRAINT songplays_user_user_id_fkey FOREIGN KEY (user_id)
                        REFERENCES users (user_id) MATCH SIMPLE
                         ON UPDATE NO ACTION ON DELETE NO ACTION,
                    CONSTRAINT songplays_songs_songs_id_fkey FOREIGN KEY (song_id)
                        REFERENCES songs (song_id) MATCH SIMPLE
                          ON UPDATE NO ACTION ON DELETE NO ACTION,
                    CONSTRAINT songplays_artist_artist_id_fkey FOREIGN KEY (artist_id)
                        REFERENCES artist (artist_id) MATCH SIMPLE
                          ON UPDATE NO ACTION ON DELETE NO ACTION,
                    CONSTRAINT songplays_time_start_time_fkey FOREIGN KEY (start_time)
                        REFERENCES time (start_time) MATCH SIMPLE
                          ON UPDATE NO ACTION ON DELETE NO ACTION
                    );
""")

user_table_create = ("""CREATE TABLE users 
                    (
                    user_id int PRIMARY KEY,
                    first_name varchar,
                    last_name varchar,
                    gender varchar,
                    level varchar
                    );
""")

song_table_create = ("""CREATE TABLE songs 
                    (
                    song_id int PRIMARY KEY,
                    title varchar,
                    artist_id int,
                    year int,
                    duration timestamp without timezone
                    );
""")

artist_table_create = ("""CREATE TABLE artist
                    (
                    artist_id int PRIMARY KEY,
                    name varchar,
                    location varchar,
                    latitude numeric,
                    longitude numeric
                    );
""")

time_table_create = ("""CREATE TABLE time 
                    (
                    start_time timestamp without timezone PRIMARY KEY,
                    hour numeric,
                    day numeric,
                    week numeric,
                    month numeric,
                    year int,
                    weekday varchar
                    );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, artist_id, sesson_id, location, user_agent)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s), (songplay_data);
""")

user_table_insert = ("""INSERT INTO user (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s), (user_df);
""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s ,%s), (song_data);
""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s), (artist_data);
""")


time_table_insert = ("""INSERT INTO time (id, start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s ,%s), (time_df);
""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
                FROM songs s
                JOIN artist a ON (s.artist_id = a.artist_id)
                WHERE (s.title = %s AND a.name = %s AND s.duration = %s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
