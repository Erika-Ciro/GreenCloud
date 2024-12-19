# Import necessary libraries
import pandas as pd
import numpy as np
import glob
from sklearn.preprocessing import MinMaxScaler

# ------------------- 1. Load Data Functions -------------------

def load_dataset(file):
    """
    Loads a single dataset from a CSV file.
    """
    df = pd.read_csv(file)
    return df

def load_and_merge_dataset(file_pattern="data/raw/*.csv"):
    """
    Loads and merges datasets from multiple CSV files, adding a 'Year' column
    and sorting the combined DataFrame by 'Year'.
    """
    files = glob.glob(file_pattern)  # Find all files matching the pattern
    dataframes = []
    
    for file in files:
        year = file.split('/')[-1].split('.')[0]  # Extract year from filename
        df = pd.read_csv(file)
        df['Year'] = int(year)  # Add Year column
        dataframes.append(df)
    
    # Concatenate all datasets
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.sort_values(by='Year', inplace=True)
    combined_df.reset_index(drop=True, inplace=True)
    print("Datasets loaded and merged successfully.")
    return combined_df

# ------------------- 2. Data Exploration -------------------

def print_summarize_dataset(df):
    """
    Prints the data types and a statistical summary of the dataset.
    """
    print("Data Types:")
    print(df.dtypes)
    print("\nStatistical Summary:")
    display(df.describe())

# ------------------- 3. Data Cleaning and Transformation -------------------

def consolidate_carbon_intensity(dataframe):
    """
    Consolidates the 'Lifecycle grid carbon intensity (gCO2eq / kWh)' and 
    'Grid carbon intensity (gCO2eq / kWh)' columns into a single column.
    """
    dataframe['Consolidated Grid Carbon Intensity (gCO2eq / kWh)'] = dataframe[
        'Lifecycle grid carbon intensity (gCO2eq / kWh)'
    ].combine_first(dataframe['Grid carbon intensity (gCO2eq / kWh)'])
    
    dataframe.drop(['Lifecycle grid carbon intensity (gCO2eq / kWh)', 
                    'Grid carbon intensity (gCO2eq / kWh)'], axis=1, inplace=True)
    print("Carbon intensity columns consolidated successfully.")
    return dataframe

def prepare_data_for_ml(df):
    """
    Prepares data for machine learning, including feature engineering and normalization.
    """
    # Feature engineering
    df['Location High CFE'] = np.where(df['Google CFE'] > 0.5, 1, 0)
    df['Location High Carbon Intensity'] = np.where(df['Consolidated Grid Carbon Intensity (gCO2eq / kWh)'] > 400, 1, 0)
    
    df = df.sort_values(by=['Location', 'Year'])
    df['Grid Carbon Intensity YoY Change (%)'] = df.groupby('Location')[
        'Consolidated Grid Carbon Intensity (gCO2eq / kWh)'
    ].pct_change() * 100
    df['Google CFE YoY Change (%)'] = df.groupby('Location')['Google CFE'].pct_change() * 100
    df.fillna(0, inplace=True)
    
    # Variability (Standard Deviation) by location
    variability_df = df.groupby('Location')[
        ['Consolidated Grid Carbon Intensity (gCO2eq / kWh)', 'Google CFE']
    ].std().reset_index()
    variability_df.columns = ['Location', 'Grid Carbon Intensity StdDev', 'Google CFE StdDev']
    df = pd.merge(df, variability_df, on='Location', how='left')
    
    # Normalization
    scale_columns = [
        'Google CFE', 
        'Consolidated Grid Carbon Intensity (gCO2eq / kWh)', 
        'Grid Carbon Intensity YoY Change (%)', 
        'Google CFE YoY Change (%)',
        'Grid Carbon Intensity StdDev', 
        'Google CFE StdDev'
    ]
    scaler = MinMaxScaler()
    df[scale_columns] = scaler.fit_transform(df[scale_columns])
    print("Feature engineering and data preparation completed.")
    return df

# ------------------- 4. Usage Example -------------------

if __name__ == "__main__":
    # Example usage
    # Load a single dataset
    print("Loading a single dataset (2019)...")
    df_2019 = load_dataset("data/raw/2019.csv")
    print_summarize_dataset(df_2019)
    
    # Load and merge datasets
    print("\nLoading and merging datasets...")
    merged_data = load_and_merge_dataset()
    print_summarize_dataset(merged_data)
    
    # Consolidate carbon intensity columns
    consolidated_data = consolidate_carbon_intensity(merged_data)
    
    # Prepare data for ML
    prepared_data = prepare_data_for_ml(consolidated_data)
    print("\nPrepared Data (First 5 Rows):")
    print(prepared_data.head())
