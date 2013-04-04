import os
import pandas as pd

name_ind = ['name','sex','births']
data = pd.read_csv(os.path.join('baby_names','yob1880.txt'), names=name_ind)

grp = data.groupby('sex')
grp['births'].sum()
years = range(1880,2011)
name_ind = ['name','sex','births']
frames = []

for year in years:
    filename = os.path.join('baby_names','yob'+str(year)+'.txt')
    tmp = pd.read_csv(filename, names=name_ind)
    tmp['year'] = year
    frames.append(tmp)
names = pd.concat(frames, ignore_index=True)

total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum)
total_births.plot()


def add_prop(df):
    births = df.births.astype(float)
    total = births.sum()
    df['prop'] = births/total
    return df

pop_names = names.groupby(['year','sex']).apply(add_prop)

def top1000names(df):
    return df.sort_index(by='births', ascending=False)[:1000]

grp = pop_names.groupby(['year','sex'])
top_names = grp.apply(top1000names)

top_names_prop = top_names.pivot_table('prop', rows='year', cols='sex', aggfunc=sum)

top_names_prop.plot()

