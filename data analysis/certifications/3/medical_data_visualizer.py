import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ""
BMI = df['weight'] / (df['height']/100)** 2
df['overweight'] = np.where(BMI >= 25, 1, 0)

# 3
# df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].applymap(lambda x: 0 if x == 1 else x)
# df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].applymap(lambda x: 1 if x >= 1 else x)
# applymap deprecated:
df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].map(lambda x: 0 if x == 1 else x)
df[["cholesterol", "gluc"]] = df[["cholesterol", "gluc"]].map(lambda x: 1 if x >= 1 else x)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()


    # 7
    


    # 8
    fig = sns.catplot(x="variable", y="total", 
            hue='value', col='cardio', kind="bar",
            data=df_cat).figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr(method="pearson")

    # 13
    mask = np.triu(corr) 

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(corr, center=0.08, linewidths=1, mask=mask, annot=True, square=True, fmt='.1f', linewidth=.5, cbar_kws={'shrink': 0.6})


    # 16
    fig.savefig('heatmap.png')
    return fig
draw_cat_plot()