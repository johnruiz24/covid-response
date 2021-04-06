import numpy as np
import pandas as pd
import pycountry_convert as pc

def get_continent(country):
    try:
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format='default')
        return pc.country_alpha2_to_continent_code(country_code)
    except (KeyError, TypeError):
        return country

def sunburst_df(df, policy = 'Stay-at-Home Requirements'):
    sunburst = df[df['Day']=='2021-03-13'][['Entity',policy]]
    sunburst.drop_duplicates(inplace=True)
    sunburst.reset_index(drop=True, inplace=True)
    sunburst.insert(2,'Day', "")
    latest_measure = [(country, df[(df['Entity']==country) & (df['Day']=='2021-03-13')][policy].tolist()[0]) for country in df[df['Day']=='2021-03-13']['Entity'].unique()]
    for country, measure in latest_measure:
        try:
            sdate = df[(df.iloc[:, 0]==country) & (df[policy]==measure) & (df['Day'].str.contains('2021'))].head(1)['Day'].values[0]
            index = sunburst[(sunburst.iloc[:, 0]==country) & (sunburst.iloc[:, 1]==measure)].index[0]
            sunburst.iloc[index, 2]=sdate
        except IndexError:
            pass
    return sunburst