import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r, p, std_err = linregress(x, y)

    def myfunc(x):
        return slope * x + intercept
    mymodel = list(map(myfunc, x))
    x_firstline=np.arange(x.min(), 2051)
    y_firstline=myfunc(x_firstline)

    plt.scatter(x, y)
    plt.plot(x_firstline, y_firstline)

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000] 
    x_new = df_2000['Year']
    y_new = df_2000['CSIRO Adjusted Sea Level']

    slope, intercept, r, p, std_err = linregress(x_new, y_new)

    def myfunc(x):
        return slope * x + intercept
    mymodel = list(map(myfunc, x_new))
    x_secondline=np.arange(x_new.min(), 2051)
    y_secondline=myfunc(x_secondline)

    plt.scatter(x_new, y_new)
    plt.plot(x_secondline, y_secondline)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()