# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:02:26 2023

@author: Åsa Ericsson
"""

import pandas as pd
import os
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_dir = CURR_DIR_PATH +"data/harmonized"

# create df_load_countries
df_SE_load_2017 = pd.read_csv("2017_SE_load.csv")
df_SE_load_2018 = pd.read_csv("2018_SE_load.csv")
df_SE_load_2019 = pd.read_csv("2019_SE_load.csv")
df_SE_load_2020 = pd.read_csv("2020_SE_load.csv")
df_SE_load_2021 = pd.read_csv("2021_SE_load.csv")
df_SE_load_2022 = pd.read_csv("2022_SE_load.csv")
df_SE_load_2023 = pd.read_csv("2023_SE_load.csv")


df_SE_load = pd.concat([df_SE_load_2017, df_SE_load_2018, df_SE_load_2019,df_SE_load_2020,df_SE_load_2021,df_SE_load_2022, df_SE_load_2023], axis=0)

df_DK_load_2017 = pd.read_csv("2017_DK_load.csv")
df_DK_load_2018 = pd.read_csv("2018_DK_load.csv")
df_DK_load_2019 = pd.read_csv("2019_DK_load.csv")
df_DK_load_2020 = pd.read_csv("2020_DK_load.csv")
df_DK_load_2021 = pd.read_csv("2021_DK_load.csv")
df_DK_load_2022 = pd.read_csv("2022_DK_load.csv")
df_DK_load_2023 = pd.read_csv("2023_DK_load.csv")

df_DK_load = pd.concat([df_DK_load_2017, df_DK_load_2018, df_DK_load_2019,df_DK_load_2020,df_DK_load_2021,df_DK_load_2022, df_DK_load_2023], axis=0)

df_DE_load_2017 = pd.read_csv("2017_DE_load.csv")
df_DE_load_2018 = pd.read_csv("2018_DE_load.csv")
df_DE_load_2019 = pd.read_csv("2019_DE_load.csv")
df_DE_load_2020 = pd.read_csv("2020_DE_load.csv")
df_DE_load_2021 = pd.read_csv("2021_DE_load.csv")
df_DE_load_2022 = pd.read_csv("2022_DE_load.csv")
df_DE_load_2023 = pd.read_csv("2023_DE_load.csv")

df_DE_load = pd.concat([df_DE_load_2017, df_DE_load_2018, df_DE_load_2019,df_DE_load_2020,df_DE_load_2021,df_DE_load_2022, df_DE_load_2023], axis=0)


df_FR_load_2017 = pd.read_csv("2017_FR_load.csv")
df_FR_load_2018 = pd.read_csv("2018_FR_load.csv")
df_FR_load_2019 = pd.read_csv("2019_FR_load.csv")
df_FR_load_2020 = pd.read_csv("2020_FR_load.csv")
df_FR_load_2021 = pd.read_csv("2021_FR_load.csv")
df_FR_load_2022 = pd.read_csv("2022_FR_load.csv")
df_FR_load_2023 = pd.read_csv("2023_FR_load.csv")

df_FR_load = pd.concat([df_FR_load_2017, df_FR_load_2018, df_FR_load_2019,df_FR_load_2020,df_FR_load_2021,df_FR_load_2022, df_FR_load_2023], axis=0)

df_load_countries = pd.concat([df_SE_load, df_DK_load, df_DE_load, df_FR_load], axis=0)