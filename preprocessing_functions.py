import warnings
warnings.filterwarnings('ignore')
# Import necessary packages




def lower_case(input_column):
    """Transforming all column values to Lower case"""
    return input_column.apply(lambda x: " ".join(x.lower() for x in x.split()))



def remove_url(input_column):
    """Removing urls and web addresses from text"""
    return input_column.apply(lambda x: re.sub('http\S+','',x))


def sample_custom_prep(input_column):
    ''' this is an example of a bigger preprocessing function that uses smaller functions'''
    input_column = lower_case(input_column)
    input_column = remove_url(input_column)
    return input_column


# complete this file with other functions