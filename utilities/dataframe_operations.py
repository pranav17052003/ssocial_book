import pandas as pd
import numpy as np

def create_dataframe():

    data = [
        {"ID": 1, "Value1": 10, "Value2": 20},
        {"ID": 2, "Value1": 30, "Value2": 15},
        {"ID": 3, "Value1": 25, "Value2": 50},
        {"ID": 4, "Value1": 40, "Value2": 30},
        {"ID": 5, "Value1": 35, "Value2": 25},
        {"ID": 6, "Value1": 60, "Value2": 40},
        {"ID": 7, "Value1": 55, "Value2": 45},
        {"ID": 8, "Value1": 70, "Value2": 60},
        {"ID": 9, "Value1": 65, "Value2": 35},
        {"ID": 10, "Value1": 80, "Value2": 70},
    ]

    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    return df


def filter_dataframe_by_value(df, column, threshold):
    filtered_df = df[df[column] > threshold]
    print("Filtered DataFrame:")
    print(filtered_df)
    return filtered_df

def filter_columns(df, columns):
    filtered_df = df[columns]
    print(f"\nDataFrame with selected columns {columns}: ")
    print(filtered_df)
    return filtered_df

def replace_values(df, column, old_value, new_value):
    df[column] = df[column].replace(old_value, new_value)
    print(f"\nDataFrame after replacing {old_value} with {new_value} in column {column} with {new_value} :")
    print(df)
    return df


def append_dataframes(df1):
    data = {
        "ID": range(11, 21),
        "value1": np.random.randint(10, 100, size=10),
        "value2": np.random.randint(10, 100, size=10),
    }
    df2 = pd.DataFrame(data)
    appended_df = pd.concat([df1, df2], ignore_index=True)
    print("\nAppended DataFrame: ")
    print(appended_df)
    return appended_df


if __name__ == "__main__":
    df = create_dataframe()
    df = filter_dataframe_by_value(df, "Value1", 30)
    df = filter_columns(df, ["ID", "Value1"])
    df = replace_values(df, "Value1", 60, 99)
    df = append_dataframes(df)



        
