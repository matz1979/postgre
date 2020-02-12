import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    ''' Read the the json song_file and convert it to a pandas DataFrame (df)
        and insert the song and artist records in the tables

        arg {
        :cur = open db connection cursor
        :filepath = json data filepath
        }
    '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data =  list(df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    ''' Read the the json log_file and convert it to a pandas DataFrame (df),
        filter the df by NextSong create the time_data and user_df
        and insert the time,user and songplays records in the tables

        arg {
        :cur = open db connection cursor
        :filepath = json data filepath
        }
    '''
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong'].reset_index()

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'],unit='ms')
    
    # insert time data records
    time_data = [df['ts'].values.tolist(),t.dt.hour.values.tolist(),t.dt.day.values.tolist(),t.dt.week.values.tolist(),t.dt.month.values.tolist(),t.dt.year.values.tolist(),t.dt.weekday_name.values.tolist()]
    column_labels = ('start_time','hour','day','week_of_year','month','year','weekday')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, list(row))

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (index, row.ts, row.userId, row.level, song_id, artist_id, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    ''' Read in both json files and return the number of files in the filepath
        also the number of processed files
        arg {
        :cur = open db connection cursor
        :conn = new db connection
        :filepath = json datafile path
        :func = Contains the function that will be performed on the provided filepath
        }
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''Contain the db connection data also the process_data'''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()