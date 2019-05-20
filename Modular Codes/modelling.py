# Importing necessary packages
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import RandomizedSearchCV
import time
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix


def LRmodelling(X_train_vec, y_train, X_test_vec, y_test):
    """Applying Logistic Regression model"""
    # Instantiate a logistic classifier
    lr = LogisticRegression(random_state=42, class_weight='balanced')
    lr.fit(X_train_vec, y_train)
    y_predict_bow = lr.predict(X_test_vec)
    print('The accuracy of model is: \n', accuracy_score(y_test, y_predict_bow))
    print('The precision of model is: \n', precision_score(y_test, y_predict_bow, pos_label=0))
    print('The recall or sensitivity of model is: \n',
          recall_score(y_test, y_predict_bow, pos_label=0))
    # calculating f1 score for positive label
    f1score = f1_score(y_test, y_predict_bow, pos_label=0)
    print('The f1 score of model is %.2f' % (f1score))
    print('The confusion matrix of model is: \n', confusion_matrix(y_test, y_predict_bow))
    print('The classification report of the model is: \n',
          classification_report(y_test, y_predict_bow))
    return


def cross_validation(X_train_vec, y_train):
    # Build the stratified k-fold cross-validator(5-fold cross-validation) and defining metrices
    stratkfold = StratifiedKFold(n_splits=5, random_state=42)
    scoring = ['accuracy', 'precision', 'recall', 'f1']
    lr = LogisticRegression(random_state=42, class_weight='balanced')
    # calculating score for the model after CV
    result = cross_validate(lr, X_train_vec, y_train, cv=stratkfold,
                            scoring=scoring, return_train_score=False)
    print('The accuracy after CV is: \n', result['test_accuracy'].mean())
    print('The precision after CV is: \n', result['test_precision'].mean())
    print('The recall after CV is: \n', result['test_recall'].mean())
    print('The f1 score after CV is: \n', result['test_f1'].mean())
    return


# modelling with random search (for hyperparameter tuning)
# Defining the grid values of the hyperparameters
def tuning(X_train_vec, y_train):
    """modelling with random search (for hyperparameter tuning)"""
    # Defining the grid values of the hyperparameters
    param_grid = {'penalty': ['l1', 'l2', 'elasticnet'], 'C': [
        0.5, 1.0, 1.5, 2.0, 2.5], 'l1_ratio': [0, 0.25, 0.5, 0.75, 1]}
    # Defining scoring metrices
    scoring = {'accuracy': make_scorer(accuracy_score), 'precision': make_scorer(
        precision_score), 'Recall': make_scorer(recall_score), 'F1 score': make_scorer(f1_score)}
    # Instantiating LR model
    lrht = LogisticRegression(max_iter=200, class_weight='balanced', solver='saga')
    # Running Randomized search on parameters
    lrrs = RandomizedSearchCV(estimator=lrht, param_distributions=param_grid, cv=5,
                              n_iter=20, n_jobs=-1, random_state=42, scoring=scoring, refit='accuracy')
    lrrs.fit(X_train_vec, y_train)
    print('Best Score: {}%'.format(lrrs.best_score_))
    print('Best Parameters: {}'.format(lrrs.best_params_))
    return


def tuned_params(X_train_vec, y_train, X_test_vec, y_test):
    """LR with best parameters after hyperparameter tuning"""
    lrbst = LogisticRegression(max_iter=200, class_weight='balanced',
                               solver='saga', C=1.5, penalty='l2', l1_ratio=0.25, random_state=42)
    lrbst.fit(X_train_vec, y_train)
    y_predictbst_bow = lrbst.predict(X_test_vec)
    # Model evaluation
    # Compute and print the confusion matrix and classification report
    print('The accuracy of model is: \n', accuracy_score(y_test, y_predictbst_bow))
    print('The precision of model is: \n', precision_score(y_test, y_predictbst_bow, pos_label=0))
    print('The recall or sensitivity of model is: \n',
          recall_score(y_test, y_predictbst_bow, pos_label=0))
    # calculating f1 score for positive label
    f1score = f1_score(y_test, y_predictbst_bow, pos_label=0)
    print('The f1 score of model is %.2f' % (f1score))
    print('The confusion matrix of model is: \n', confusion_matrix(y_test, y_predictbst_bow))
    print('The classification report of the model is: \n',
          classification_report(y_test, y_predictbst_bow))
    return
