import pandas as pd
def import_clean(file_name):
    """Importing and cleaning of data"""
    #Reading files
    dataframe=pd.read_csv(file_name)
    #Dropping duplicates
    dataframe=dataframe.drop_duplicates()
    return dataframe
