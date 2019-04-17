import warnings
warnings.filterwarnings('ignore')
# Import necessary packages




def lower_case(tweet_column):
    """Transforming all column values to Lower case"""
    return tweet_column.apply(lambda x: " ".join(x.lower() for x in x.split()))




