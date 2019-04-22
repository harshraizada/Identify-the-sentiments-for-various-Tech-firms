import preprocessing_functions as prep

if __name__ == "__main__":
    
    #load data
    its=pd.read_csv('Identify the sentiments.csv')
    its.tweet = prep.sample_custom_prep(its.tweet)
    
