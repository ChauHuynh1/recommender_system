import pandas as pd

# Modules for data visualization
import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def missing_percentage(df):
    """This function takes a DataFrame(df) as input and returns two columns, total missing values and total missing values percentage"""
    total = df.isnull().sum().sort_values(ascending=False)[df.isnull().sum().sort_values(ascending=False) != 0]
    percent = round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2)[
        round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2) != 0]
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

def draw_missing_plot(df):
    # display missing values in descending
    print("Missing values in the user dataframe in descending: \n", missing_percentage(df).sort_values(by='Total', ascending=False))

    # visualize where the missing values are located
    msno.matrix(df, color=(255 / 255, 192 / 255, 203 / 255))
    pink_patch = mpatches.Patch(color='pink', label='present value')
    white_patch = mpatches.Patch(color='white', label='absent value')
    plt.legend(handles=[pink_patch, white_patch])
    plt.show()

def whitespace_remover(df):
    """
    The function will remove extra leading and trailing whitespace from the data.
    """
    # iterating over the columns
    for i in df.columns:
        # checking datatype of each columns
        if df[i].dtype == 'object' or df[i].dtype == 'str':
            # applying strip function on column
            df[i] = df[i].map(str.strip)
        else:
            # if condition is False then it will do nothing.
            pass

