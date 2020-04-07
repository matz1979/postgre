import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    
    ''' 
    Connect to the dafault database and create a new database named sparkify also connect to it.
    
    Args:
        Null
    Returns:
        cur : connection cursor
        conn : connection to db
        
    '''
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    ''' Call the DROP Tables statement from the sql_queries.py and execute it
    arg {
        :cur = connection cursor
        :conn = connection db
    }
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    ''' 
    
    Call the CREATE Tables statement from the sql_queries.py and execute it.
    Args:
        param cur : connection cursor
        parm conn = connection db
    Return:
        : Null
        
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()