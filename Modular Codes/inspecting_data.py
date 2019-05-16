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


def data_distribution(column_name):
    """Distribution of label types"""
    # check the number of positive vs. negative tagged sentences
    positives ='number of positve tagged sentences is:  {}'.format(len(column_name[column_name == 0]))
    negatives ='number of negative tagged sentences is: {}'.format(len(column_name[column_name == 1]))
    #Percentage distribution of labels
    percentage=column_name.value_counts(normalize='True')
    return positives, negatives,percentage
