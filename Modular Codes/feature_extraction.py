# Import necessary packages

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Before feature extraction first splitting the data into train and test and then perform feature extraction


def traintest_split(X, y):
        """Split into training and test (hold-out) set"""
        # 80% of the input for training and 20% for training
        Xtrain, Xtest, ytrain, ytest = train_test_split(
            X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y)
        print(Xtrain.shape, ytrain.shape)
        print(Xtest.shape, ytest.shape)
        return Xtrain, Xtest, ytrain, ytest


def bow_vec(X_train, X_test):
    """Vectorization with Bag of Words(one-hot encoding)"""
    bowvec = CountVectorizer(binary=True)
    bowvec.fit(X_train)
    Xbow_train = bowvec.transform(X_train)
    Xbow_test = bowvec.transform(X_test)
    return Xbow_train, Xbow_test
