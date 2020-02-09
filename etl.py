import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Open the file and insert the records into the song- and artist- table
       call the insert statement from the sql_queries.py file"""
    df = 'data\song_data'
    song_data =  list(df[['song_id', 'title', 'artist_id', 'year', 'duration']].values)
    cur.execute(song_table_insert, song_data)
    artist_data = list(df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """open the second file filter, convert the records and insert it into the time-, 
       user- and songplays-table, call the insert query from the sql_queries.py file"""
    df = pd.read_json(filepath, lines=True)
    # df filter
    df = df[df['page'] == 'NextSong']
    # time table
    t = pd.to_datetime(df['ts'],unit='ms')
    time_data = [df['ts'].values.tolist(),t.dt.hour.values.tolist(),t.dt.day.values.tolist(),t.dt.week.values.tolist(),t.dt.month.values.tolist(),t.dt.year.values.tolist(),t.dt.weekday_name.values.tolist()]
    column_labels = ('start_time','hour','day','week_of_year','month','year','weekday')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, list(row))

    # songplay
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        songid, artistid = results 
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        songplay_data = (index, row.ts, row.userId, row.level, songid, artistid, row.sessonId, row.artist_location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """return all json files from the filepath print the num of files out
       iterate over file and print the num of processed files out"""
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """Connect to the database insert the filepath into function process_data and close the connection"""
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()