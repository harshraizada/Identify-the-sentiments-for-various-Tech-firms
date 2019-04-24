 # Import necessary packages
 
 from sklearn.model_selection import train_test_split
 from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
 
 # Before feature extraction splitting the data into train and test and then feature extraction
 
    """Split into training and test (hold-out) set"""
    # 80% of the input for training and 20% for training
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y, test_size = 0.2,random_state=42,shuffle= True,stratify=y)
    print (Xtrain.shape, ytrain.shape)
    print (Xtest.shape, ytest.shape)
    return
    
    
 def ohe_vectorization(X_train,X_test):
    """Vectorization (one-hot encoding)"""
    cvohe = CountVectorizer(binary=True)
    cvohe.fit(X_train)
    Xohe_train = cvohe.transform(X_train)
    Xohe_test = cvohe.transform(X_test)
    return Xohe_train,Xohe_test
