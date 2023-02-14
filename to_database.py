import pandas as pd
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

def create_table(generation_table_creation):
    #THIS IS ONLY FOR THE SE_zones_generation TABLE
    #Since the generation-files creates some problems with differing column names, SQL Alchemy is used to create the table
    #Needs the ID column as a easy fix
    #Note that the column names are different, with an added _ between words, didn't work otherwise
    Base = declarative_base()
    class SZG(Base):
        __tablename__ = 'SE_zones_generation'
        id = Column(Integer, primary_key=True)
        SE_zone = Column(String)
        Timestamp = Column(String)
        Fossil_Gas = Column(Float)
        Hydro_Water_Reservoir = Column(Float)
        Nuclear = Column(Float)
        Other = Column(Float)
        Solar = Column(Float)
        Wind_Onshore = Column(Float)
    Base.metadata.create_all(generation_table_creation)

def countries_load_and_generation(engine):
    load_table = 'load'
    generation_table = 'generation'
    folder = "data/harmonized/"
    
    #Iterates through the folder and transfers the files to the database
    for file in os.listdir(folder):
        if file.endswith("load.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            df.to_sql(load_table, engine, if_exists='append', index=False)

        elif file.endswith("generation.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            df.to_sql(generation_table, engine, if_exists='append', index=False)
        else:
            pass
    print("All files transferred to database.")

def SE_zones(engine):
    
    create_table(engine)
    load_table = 'SE_zones_load'
    folder = "data/harmonized/SE_zones/" 

    for file in os.listdir(folder):
        if file.endswith("load.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            
            df = df.rename(columns = {"Country": "SE_zone"})
            #Just to make sure the columns are SE_1, SE_2 etc.
            values_from_filename = file[5:9]        
            df['SE_zone'] = values_from_filename

            df.to_sql(load_table, engine, if_exists='append', index=False)

        #Just the 2022 files since they have the most data
        elif file.startswith("2022") and file.endswith("generation.csv"):
            file_path = os.path.join(folder, file)
            df = pd.read_csv(file_path)
            #"Bad" solution in this step, but it works
            #When creating the table, the column names are not the same as the ones in the files
            #Variables are renamed to make sure the files matches the names created by SQL Alchemy
            df = df.rename(columns = {"Country": "SE_zone"})
            df = df.rename(columns = {"Hydro Water Reservoir": "Hydro_Water_Reservoir"})
            df = df.rename(columns = {"Fossil Gas": "Fossil_Gas"})
            df = df.rename(columns = {"Wind Onshore": "Wind_Onshore"})
            
            values_from_filename = file[5:9]        
            df['SE_zone'] = values_from_filename
            
            df.to_sql("SE_zones_generation", engine, if_exists='append', index=False)
        else:
            pass
    print("All files transferred to database.")


#Creates database connection, replace with your credentials
engine = create_engine('postgresql://postgres:Vera1234?@localhost:5432/entsoe')
create_table(engine)
countries_load_and_generation(engine)
SE_zones(engine)