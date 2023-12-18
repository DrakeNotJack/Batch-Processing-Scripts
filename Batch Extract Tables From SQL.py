import sqlalchemy as sa
import pandas as pd
import os
import time

# database connection parameters
server = 'ServerName'
database = 'DatabaseName'
driver = 'SQL Server'

# SQLAlchemy connection string URI
conn_str = f"mssql+pyodbc://{server}/{database}?driver={driver}"

# list of tables to extract data from
tables = ['Tables to extract']

# SQL query to extract data from each table for each day
query_template = "SELECT * FROM {} WHERE BUSINESS_DATE = '{}'"

# create a SQLAlchemy engine object
engine = sa.create_engine(conn_str)

# loop over each day and table, and export data to a separate folder for that day
for date in pd.date_range('YYYY-MM-DD', 'YYYY-MM-DD', freq='D'): #First date is start date, second date is end date
    # format the date as a string
    date_str = date.strftime('%Y-%m-%d')
    # create a folder for the day if it doesn't exist
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', date_str)
    os.makedirs(folder_path, exist_ok=True)
    
    # record the start time for this folder's processing
    start_time = time.time()
    
    # loop over each table and extract data for the day
    for table in tables:
        # construct the file name for the CSV file
        file_path = os.path.join(folder_path, f"{date_str}_{table}.csv")
        # execute the SQL query to extract data for the day and table
        query = query_template.format(table, date_str)
        df = pd.read_sql(query, engine)
        # save the data to a CSV file in the folder for the day and table
        df.to_csv(file_path, index=False, header=False)
        
    # record the end time for this folder's processing
    end_time = time.time()
        
    # calculate the processing time for this folder
    processing_time = int(end_time - start_time)
    
    # calculate the minutes and seconds from the processing time
    minutes = processing_time // 60
    seconds = processing_time % 60
    
    # print the processing time for this folder
    print(f"Processed {date_str} in {minutes} minutes {seconds} seconds")

# close the database connection
engine.dispose()
