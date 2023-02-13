# Import packages & setting up a connection to the ENTSOE API Client
import pandas as pd
import numpy as np

# Create a Local Reference
import os
current_dir = os.path.abspath("")
parent_dir = os.path.abspath(current_dir + "/../")
data_dir = os.path.abspath(current_dir + "/data/raw/")
test_dir = os.path.abspath(current_dir + "/data/test/")
# print(current_dir)
# print(parent_dir)
# print(data_dir)

# Loop through directory, Extract data from file, Transform data in pandas
import glob

def raw_to_cleansed():
    for file in glob.glob(data_dir + "/*.csv"):
        print(file)

        # Split the path to get country code
        filename_split = file.split("_", maxsplit = 3)
        year = filename_split[0][-4:]

        if len(filename_split) == 2:
            country_code = filename_split[1]
        else:
            country_code = filename_split[1] + "_" + year[0]

        data_category = filename_split[2][1:-4]

        with open(file) as f:
            # Read file and create DataFrame
            df = pd.read_csv(
                f,
                delimiter = ",",
                parse_dates = ["Unnamed: 0"],
            )

            # Transforming "Timestamp"-column
            df.rename(columns = {"Unnamed: 0": "Timestamp"}, inplace = True)
            df["Timestamp"] = df["Timestamp"].dt.tz_localize(None) # Replaced tz = "Europe/Stockholm" with None to get rid of "00:00:00+01:00"

            # Create a new "Country"-column and shift it to be the "first"-column
            df['Country'] = np.nan
            df['Country'] = df['Country'].replace(np.nan, filename_split[1]) # filename_split[1] returns the country code from the path
            first_column = df.pop("Country")
            df.insert(0, "Country", first_column)

            # Drop second-source columns such as that contain ".1"
            df = df[df.columns.drop(list(df.filter(regex='.1')))]

            # Drop "Marine"-column
            df = df[df.columns.drop(list(df.filter(regex='Marine')))]

            # Drop first row in DataFrame if row contains "Actual" and if filename contains "generation"
            if (data_category == "generation"):
                df = df.drop(df[df["Wind Onshore"] == "Actual Aggregated"].index)

            # Fill missing values in df
            df.fillna(float(0))

            # Load to .csv and format date
            if "SE_" in country_code:
                df.to_csv(
                    f"{current_dir}/data/cleansed/SE_zones/{year}_{country_code}_{data_category}.csv",
                    date_format = "%Y-%m-%d",
                    index = False
                )
            else:
                df.to_csv(
                        f"{current_dir}/data/cleansed/{year}_{country_code}_{data_category}.csv",
                        date_format = "%Y-%m-%d",
                        index = False
                )
                
raw_to_cleansed()