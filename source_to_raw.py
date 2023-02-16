# Import packages & setting up a connection to the ENTSOE API Client
import pandas as pd
from entsoe import EntsoePandasClient
client = EntsoePandasClient(api_key = "") # Do not forget to put in API key
type_marketagreement_type = "A01"
contract_marketagreement_type = "A01"

# Create a Local Reference
import os
current_dir = os.path.abspath("")
print(current_dir)
parent_dir = os.path.abspath(current_dir + "/../")
print(parent_dir)
# print(current_dir)
# print(parent_dir)

# A dictionary of dates - Comment IN/OUT
date_dic = {
    # "2017": ["20170101", "20180101"],
    # "2018": ["20180101", "20190101"],
    # "2019": ["20190101", "20200101"],
    # "2020": ["20200101", "20210101"],
    # "2021": ["20210101", "20220101"],
    # "2022": ["20220101", "20230101"],
    "2023": ["20230101", "20240101"]
}

# A list of timezones - Comment IN/OUT
timezone_list = [
    "Europe/Stockholm"
]

# A list of countries - Comment IN/OUT
country_list = [
    # "SE_1",
    # "SE_2",
    # "SE_3",
    # "SE_4",
    # "SE",
    # "DE",
    # "FR",
    "DK"
]

# Function for extracting Load/Consumption data from entsoe
def load_df_file():
    # Loop through date_dic
    for value in date_dic.values():
            start_date = value[0]
            end_date = value[1]

            # Loop through timezone_list
            for i in timezone_list:
                    tz = i

                    start_date = pd.Timestamp(start_date, tz = tz)
                    end_date = pd.Timestamp(end_date, tz = tz)

                    # Loop through country_list
                    for i in country_list:
                            country_code = i

                            # Extract data with ENTSOE'S API
                            load_df = client.query_load_and_forecast(
                                    country_code,
                                    start = start_date,
                                    end = end_date
                            )

                            # Convert RangeIndex to DatetimeIndex & Resample "D"
                            load_df.index = pd.to_datetime(load_df.index)
                            load_df = load_df.resample("D").sum()

                            # Load to .csv
                            load_df.to_csv(
                                    f"{current_dir}/data/test/{value[0][0:4]}_{country_code}_load.csv",
                                    # index = False,
                                    date_format = "%Y-%m-%d"
                            )
                            
                            # # Load to .json
                            # load_df.to_json(
                            #         f"{parent_dir}/data/test/{value[0][0:4]}_{country_code}_load.json",
                            #         indent = 4,
                            #         orient = "records",
                                    
                            # )
# # Function for extracting Generation/Production data from entsoe
def generation_df_file():
    # Loop through date_dic
    for value in date_dic.values():
            start_date = value[0]
            end_date = value[1]
            
            # Loop through timezone_list
            for i in timezone_list:
                    tz = i

                    start_date = pd.Timestamp(start_date, tz = tz)
                    end_date = pd.Timestamp(end_date, tz = tz)

                    # Loop through country_list
                    for i in country_list:
                            country_code = i

                            # Extract data with ENTSOE'S API
                            generation_df = client.query_generation(
                                    country_code,
                                    start = start_date,
                                    end = end_date,
                                    psr_type = None
                            )

                            # Convert RangeIndex to DatetimeIndex & Resample "D"
                            generation_df.index = pd.to_datetime(generation_df.index)
                            generation_df = generation_df.resample("D").sum()

                            # Load to .csv
                            generation_df.to_csv(
                                    f"{current_dir}/data/test/{value[0][0:4]}_{country_code}_generation.csv",
                                    # index = False,
                                    date_format = "%Y-%m-%d"
                            )
                            
                            # # Load to .json
                            # generation_df.to_json(
                            #         f"{parent_dir}/data/raw/{value[0][0:4]}_{country_code}_generation.json",
                            #         indent = 4,
                            #         orient = "records",
                            # )

load_df_file()
generation_df_file()