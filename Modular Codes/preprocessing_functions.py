from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk  # for text manipulation
import re  # for regular expressions
import warnings
warnings.filterwarnings('ignore')
# Import necessary packages


def lower_case(input_column):
    """Transforming all column values to Lower case"""
    return input_column.apply(lambda x: " ".join(x.lower() for x in x.split()))


def remove_url(input_column):
    """Removing urls and web addresses from text"""
    return input_column.apply(lambda x: re.sub('http\S+', '', x))


def remove_handles(input_column):
    """Removing twitter handles (i.e. @user_name) from text"""
    return input_column.apply(lambda x: re.sub("@[\w]*", '', x))


appos = {"aren't": "are not", "can't": "cannot", "couldn't": "could not", "didn't": "did not", "doesn't": "does not",
         "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would", "he'll": "he will",
         "he's": "he is", "i'd": "i would", "i'd": "i had", "i'll": "i will", "i'm": "i am", "isn't": "is not", "it's": "it is",
         "it'll": "it will", "i've": "i have", "let's": "let us", "mightn't": "might not", "mustn't": "must not", "shan't": "shall not",
         "she'd": "she would", "she'll": "she will", "she's": "she is", "shouldn't": "should not", "that's": "that is", "there's": "there is",
         "they'd": "they would", "they'll": "they will", "they're": "they are", "they've": "they have", "we'd": "we would",
         "we're": "we are", "weren't": "were not", "we've": "we have", "what'll": "what will", "what're": "what are",
         "what's": "what is", "what've": "what have", "where's": "where is", "who'd": "who would", "who'll": "who will",
         "who're": "who are", "who's": "who is", "who've": "who have", "won't": "will not", "wouldn't": "would not",
         "you'd": "you would", "you'll": "you will", "you're": "you are", "you've": "you have", "'re": " are", "wasn't": "was not",
         "we'll": " will", "didn't": "did not"}


def remove_apostrophes(input_column):
    """Removing Apostrophes from text"""
    return input_column.apply(lambda x: " ".join(appos[x] if x in appos else x for x in x.split()))


def remove_sc(input_column):
    """Removing special characters, numbers, punctuations, # tags from text"""
    return input_column.apply(lambda x: re.sub("[^a-z\s]", '', x))


def remove_stopwords(input_column):
    """Removing Stop Words from text"""
    s_words = stopwords.words('english')
    not_stopwords = ['no', 'nor', 'not']
    stop_words = set([word for word in s_words if word not in not_stopwords])
    return input_column.apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))


def remove_shortwords(input_column):
    """Removing short words (words having word length of 2 or less) from text"""
    return input_column.apply(lambda x: ' '.join([w for w in x.split() if len(w) > 2]))


def tokenization(input_column):
    """Tokenization of tidy text"""
    return input_column.apply(lambda x: word_tokenize(x))


def lemmatization(input_column):
    """Lemmatization of tokenized text"""
    input_column = input_column.apply(lambda x: [WordNetLemmatizer().lemmatize(i, 'v') for i in x])
    # Stitching of tokens back together
    for i in range(len(input_column)):
        input_column[i] = ' '.join(input_column[i])
    return input_column


def preprocessing(input_column):
    ''' Combining all function in one as preprocessing function'''
    input_column = lower_case(input_column)
    input_column = remove_url(input_column)
    input_column = remove_handles(input_column)
    input_column = remove_apostrophes(input_column)
    input_column = remove_sc(input_column)
    input_column = remove_stopwords(input_column)
    input_column = remove_shortwords(input_column)
    input_column = tokenization(input_column)
    input_column = lemmatization(input_column)
    return input_column
