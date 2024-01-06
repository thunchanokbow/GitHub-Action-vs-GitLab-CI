# %% [markdown]
# # COVID-19 time series by country
# 1. read Johns Hopkins COVID-19 time series data
# * https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
# 1. aggregate by country
# 1. save to CSV and Excel

# %%
import pandas as pd

# %%
def read_covid_time_series():
    '''
    read Johns Hopkins COVID-19 time series data
    data source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
    '''
    path = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_'
    status = ['Confirmed', 'Deaths', 'Recovered']
    dfs = [pd.read_csv(f'{path}{s.lower()}_global.csv') for s in status]

    df = pd.concat(dfs, keys=status)

    dtmps = [pd.melt(df.loc[k],
                     id_vars=['Province/State',
                              'Country/Region', 'Lat', 'Long'],
                     var_name='Date', value_name=k) for k in status]
    dx = [d.set_index(['Province/State', 'Country/Region', 'Date'])
          for d in dtmps]
    dcovid = pd.concat(dx, axis=1)
    dcovid.reset_index(inplace=True)
    dcovid = dcovid.loc[:, ~dcovid.columns.duplicated()]
    dcovid['Date'] = pd.to_datetime(dcovid['Date'])
    dcovid = dcovid.sort_values(
        ['Country/Region', 'Province/State', 'Date']).reset_index(drop=True)
    dcountry = dcovid.groupby(
        ['Country/Region', 'Date']).sum()[['Confirmed', 'Deaths', 'Recovered']]
    dcountry.reset_index(inplace=True)
    dcountry['daily_new_patient'] = dcountry.groupby(
        ['Country/Region'])['Confirmed'].diff()
    dcountry['daily_new_patient_pct'] = dcountry.groupby(
        ['Country/Region'])['Confirmed'].pct_change()
    return dcountry

# %%
if __name__ == "__main__":
    print('start retrieving data ....')
    df=read_covid_time_series()
    print('saving data to csv and excel')
    df.to_csv('covid19_time_series.csv', index=False)
    df.to_excel('covid19_time_series.xlsx', index=False)
    # dts=pd.read_csv('covid19_time_series.csv')
# %%
