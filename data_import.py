from sqlalchemy import create_engine
import pandas as pd
import os

local_engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
file_list = os.listdir(f'{os.getcwd()}/data')

for csv_file in file_list:
    print(f'Loading file {csv_file} into database')
    df = pd.read_csv(f'{os.getcwd()}/data/{csv_file}')
    print(df.head())
    df.to_sql(
        name=csv_file.split('.')[0],
        schema='public',
        if_exists='replace',
        con=local_engine,
    )

print('Data uploading done.')
