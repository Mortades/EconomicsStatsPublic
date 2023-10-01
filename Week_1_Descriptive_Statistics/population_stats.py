import pandas as pd
import numpy as np


def calculate_population_stats(df, columns_to_calculate, interpolation='midpoint'):
    """
    Calculate various population statistics (mean, median, RMSD, STD, Q1, Q3, coefficient of variation, Inter Quartile Ratio) of specified columns in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns_to_calculate (list): A list of column names for which you want to calculate the population statistics.
        interpolation (string): The type of interpolation used for quantiles, affects inter-quartile ratio
    Returns:
        pd.DataFrame: A DataFrame with the calculated population statistics for specified columns.
    """
    # Select the columns to calculate the population statistics for
    selected_columns = df[columns_to_calculate]

    # Calculate the mean, median, RMSD, STD, Q1, Q3, coefficient of variation and IQR for each selected column
    means = selected_columns.mean()
    medians = selected_columns.median()
    rmsd = np.sqrt(((selected_columns - selected_columns.mean()) ** 2).mean())
    std = selected_columns.std(ddof=0)
    q1 = selected_columns.quantile(0.25, interpolation=interpolation)  # Using midpoint because it is a population
    q3 = selected_columns.quantile(0.75, interpolation=interpolation)  # Whatever method of finder quartiles comparing the two is more important
    cv = (std / selected_columns.mean()) * 100
    iq_ratio = (q3-q1)/medians * 100

    # Create a DataFrame to hold the population statistics
    stats_df = pd.DataFrame({'Mean': means, 'Median': medians, 'RMSD': rmsd, 'STD': std, 'CoV (%)': cv, 'Q1': q1, 'Q3': q3, 'IQRat (%)': iq_ratio})

    return stats_df
