import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index(df['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
     # Draw line plot
    plt.figure(figsize=(15, 5))
    plt.plot(df['date'], df['value'],  color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Page Views', fontsize=15)

    fig = plt.gcf() 
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.read_csv('fcc-forum-pageviews.csv')
    df_bar['date'] = pd.to_datetime(df_bar['date'])

    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    
    fig, ax = plt.subplots(figsize=(15, 10))
    df_bar.plot(kind='bar', ax=ax) 
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    month_names = [calendar.month_name[i] for i in range(1, 13)]
    ax.legend(title='Months', labels=month_names, title_fontsize='13', fontsize='11')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    
    df_box = pd.read_csv('fcc-forum-pageviews.csv')
    df_box['date'] = pd.to_datetime(df['date'])
    df_box = df.set_index(df['date'])

    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    fig, axes = plt.subplots(figsize=(10,5), ncols=2, nrows=1)
    axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

     # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
