from entsoe import EntsoePandasClient
import pandas as pd

#API-nyckel behöver vara i en string
client = EntsoePandasClient(api_key = 'api_key')

#Ger ut en dags data för Sverige, end är exkluderat
start = pd.Timestamp('20230201', tz='Europe/Brussels')
end = pd.Timestamp('20230202', tz='Europe/Brussels')
country_code = 'SE'  # Sweden

#client.query_load taget från Entsoes exempelkod
se_load = client.query_load(country_code, start=start,end=end)

df = se_load

#Vilken typ av orient= bör vi använda?
#varning varning! hårdkodat filnamn!
df.to_json('load20230201.json')