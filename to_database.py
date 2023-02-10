import pandas as pd
import os
from sqlalchemy import create_engine



# def to_load_table():
#     table_name = 'load'
#     folder = "5. cleansed_to_database"
    
#     for file in os.listdir(folder):
#         if file.endswith("load_cleansed.csv"):
#             file_path = os.path.join(folder, file)
#             df = pd.read_csv(file_path)
#             df.to_sql(table_name, engine, if_exists='append', index=False)
            

def to_load_and_generation():
    engine = create_engine('postgresql://postgres:5731@localhost:5432/ENTSOE')
    load_table = 'load'
    generation_table = 'generation'
    folder = "data/harmonized/"
    
    
    for file in os.listdir(folder):
        if file.endswith("load.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            df.to_sql(load_table, engine, if_exists='append', index=False)

        elif file.endswith("generation.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            
            #Ta bort när Santi har fixat drop på Marine
            column_name = "Marine"
            if column_name not in df.columns:
                df[column_name] = None
            df.to_sql(generation_table, engine, if_exists='append', index=False)
        else:
            pass
    print("All files transferred to database.")

to_load_and_generation()

def to_database():
    engine = create_engine('postgresql://postgres:5731@localhost:5432/ENTSOE')
    load_table = 'zone_load'
    generation_table = 'zone_generation'
    folder = "data/harmonized/" 
    
    
    
    for file in os.listdir(folder):
        if file.endswith("load.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            df.to_sql(load_table, engine, if_exists='append', index=False)

        elif file.endswith("generation.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            
            #Ta bort när Santi har fixat drop på Marine
            column_name = "Marine"
            if column_name not in df.columns:
                df[column_name] = None
            df.to_sql(generation_table, engine, if_exists='append', index=False)
        else:
            pass
    print("All files transferred to database.")