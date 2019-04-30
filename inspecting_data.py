import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

def data_inspection(dataframe):
    #Exploring dataset Dimensions
    shape=dataframe.shape
    columns=dataframe.columns
    # checking the content of dataset
    head=dataframe.head(10)
    #Exporing datatset info
    info=dataframe.info()
    #Exporing null values in datatset
    null=sns.heatmap(dataframe.isnull())
    return shape,columns,head,info,null
