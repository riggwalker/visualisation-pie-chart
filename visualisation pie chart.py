import pandas as pd
import matplotlib.pyplot as plt

def create_dataframes():
    """
    Creates two pandas DataFrames from hard-coded dictionaries, and sets the 'Internet Service Provider'
    column as the index of each DataFrame.
    
    Returns:
        A tuple of two pandas DataFrames.
    """
    # Data for 2018
    data_2018 = {'Internet Service Provider': ['BT', 'Sky', 'Virgin Media', 'TalkTalk', 'Others'], 
                 'Percentage of Market Share': [29, 23, 20, 14, 14]}
    df_2018 = pd.DataFrame(data_2018)
    df_2018.set_index('Internet Service Provider', inplace=True)

    # Data for 2021
    data_2021 = {'Internet Service Provider': ['BT', 'Virgin Media', 'Sky', 'TalkTalk', 'Plusnet', 'Others'], 
                 'Percentage of Market Share': [28, 22, 18, 8, 7, 17]}
    df_2021 = pd.DataFrame(data_2021)
    df_2021.set_index('Internet Service Provider', inplace=True)
    
    return df_2018, df_2021

def create_pie_charts(df_2018, df_2021):
    """
    Creates two pie charts to visualize the market share percentages of the top 5 internet service providers in the UK 
    for the years 2018 and 2021, using data from two pandas DataFrames.
    
    Args:
        df_2018: A pandas DataFrame containing the market share percentages of the top 5 internet service providers 
            in the UK for the year 2018.
        df_2021: A pandas DataFrame containing the market share percentages of the top 5 internet service providers 
            in the UK for the year 2021.
    
    Returns:
        None. Displays the pie charts using matplotlib.
    """
    # Create the pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Pie chart for 2018
    ax1.pie(df_2018['Percentage of Market Share'], labels=df_2018.index, autopct='%1.1f%%', startangle=90)
    ax1.set_title('UK Internet Providers Market Share in 2018')

    # Pie chart for 2021
    ax2.pie(df_2021['Percentage of Market Share'], labels=df_2021.index, autopct='%1.1f%%', startangle=90)
    ax2.set_title('UK Internet Providers Market Share in 2021')

    # Show the pie charts
    plt.show()

# Call the functions to create the dataframes and pie charts
df_2018, df_2021 = create_dataframes()
create_pie_charts(df_2018, df_2021)


















