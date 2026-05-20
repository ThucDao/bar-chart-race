# import Python libraries
import pandas as pd
import bar_chart_race as bcr

df = pd.read_csv('Sudbury businesses 2015-2021.csv', sep=',', on_bad_lines='skip')
df = df.set_index('Year')

def period_summary(values, ranks):
    total_companies = int(values.sum())
    s = f'Total Companies: {total_companies}'
    return {'x': .95, 'y': .08, 's': s, 'ha': 'right', 'size': 10}

bcr.bar_chart_race(df=df, sort='desc', fixed_max=True,
                   perpendicular_bar_func='mean',
                   period_summary_func=period_summary,
                   period_length=1400, steps_per_period=10,
                   figsize=(6, 4), dpi=144,
                   bar_size=0.8,
                   bar_label_size=8, tick_label_size=8, title_size='large',
                   shared_fontdict={'family': 'DejaVu Sans', 'weight': 'normal', 'color': 'black'},                   
                   title='Businesses by industry sector in Sudbury, 2015-2021 (Thuc Dao)',
                   filename='Businesses in Sudbury, 2015-2021, made by Thuc Dao.gif')