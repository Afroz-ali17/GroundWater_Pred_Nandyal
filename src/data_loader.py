import pandas as pd
import numpy as np
import os

def load_nandyal_gw_data(file_path=r'c:\Users\pafro\OneDrive\Desktop\GrondWaterLavel\NANDYAL GW LEVELS.xlsx'):
    """
    Loads and cleans the monthly groundwater level data for Nandyal District.
    Returns a cleaned pandas DataFrame indexed by Date with 'WaterLevel_mbgl' column.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found at: {file_path}")

    # Read excel file skipping header row if needed
    df_raw = pd.read_excel(file_path, header=1)
    
    # Standardize column names
    df = df_raw.rename(columns={
        df_raw.columns[0]: 'Date',
        df_raw.columns[1]: 'WaterLevel_mbgl'
    })
    
    # Ensure Date is datetime and sorted
    df['Date'] = pd.to_datetime(df['Date'])
    df['WaterLevel_mbgl'] = pd.to_numeric(df['WaterLevel_mbgl'], errors='coerce')
    
    # Drop invalid rows and sort chronologically
    df = df.dropna(subset=['Date', 'WaterLevel_mbgl']).sort_values('Date').reset_index(drop=True)
    
    # Set frequency to Monthly Start (MS)
    df.set_index('Date', inplace=True)
    df = df.asfreq('MS')
    
    # Interpolate if any missing dates exist
    if df['WaterLevel_mbgl'].isna().sum() > 0:
        df['WaterLevel_mbgl'] = df['WaterLevel_mbgl'].interpolate(method='time')
        
    return df

if __name__ == '__main__':
    df = load_nandyal_gw_data()
    print("Dataset successfully loaded.")
    print("Shape:", df.shape)
    print("Date Range:", df.index.min().strftime('%Y-%m'), "to", df.index.max().strftime('%Y-%m'))
    print(df.head())
