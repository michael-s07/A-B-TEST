
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
print(ad_clicks.utm_source.value_counts())
ad_clicks['is_click']=ad_clicks.ad_click_timestamp.notnull()
print(ad_clicks)

clicks_by_source=ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot=clicks_by_source.pivot(index='utm_source',columns='is_click',values='user_id').reset_index()
print(clicks_pivot)
experimental_grp=ad_clicks.groupby(['experimental_group']).user_id.count()
print(experimental_grp)
is_c=ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
is_pivot=is_c.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()
print(is_pivot)
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(a_clicks)
print(b_clicks)

a_group=ad_clicks.groupby(['is_click','day']).experimental_group.count().reset_index()
a_pivot=a_group.pivot(index="day", columns='is_click', values='experimental_group').reset_index()
print(a_pivot)

"Company Should use Ad A"