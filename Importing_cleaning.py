import pandas as pd
def import_clean(file_name):
    """Importing and cleaning of data"""
    #Reading files
    dataframe=pd.read_csv(file_name)
    #Renaming columns.
    dataframe.columns=['id','sentiment_type','tweet']
    #Dropping null values
    dataframe=dataframe.dropna(axis=1)
    #Dropping duplicates
    dataframe=dataframe.drop_duplicates()
    return dataframe
