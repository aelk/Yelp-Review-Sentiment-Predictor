from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from numpy import mean
from yelp_utils import numLines, loadData
import sys
import time

def classify(technique, posneg, percentData):
    filename = 'yelp_academic_dataset_review.json'
    num_lines = numLines(filename)
    linesToRead = int(num_lines*(float(percentData)/100.0))
    train_end = linesToRead*0.7

    train_data, train_labels = loadData(filename, 0, train_end, posneg)
    test_data, test_labels = loadData(filename, train_end+1, linesToRead, posneg)

    if technique == 'nb':
        clf_obj = MultinomialNB()
    elif technique == 'svm':
        clf_obj = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)
    elif technique == 'lr':
        clf_obj = LogisticRegression()

    start_time = time.time()
    text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                        ('tfidf', TfidfTransformer()),
                        ('clf', clf_obj),
    ])

    text_clf = text_clf.fit(train_data, train_labels)

    predicted = text_clf.predict(test_data)
    print "time: %s seconds" % (time.time() - start_time)

    print "accuracy:", mean(predicted == test_labels)

def print_usage():
    print "Usage: classify.py <nb/svm/lr> <True/False> <number in [0, 100]>"
    print "e.g., classify.py nb True 85"

def valid_args(avail_techniques, technique, posneg, percentData):
    return technique in avail_techniques and\
            (posneg == 'True' or posneg == 'False') and\
            (int(percentData) >= 0 and int(percentData) <= 100)

if __name__ == '__main__':
    techniques = {'nb': 'Naive Bayes', 'svm': 'Support Vector Machines', 'lr': 'Logistic Regression'}
    
    try:
        technique = sys.argv[1].lower() # nb or svm or lr
        posneg = sys.argv[2] # True or False
        percentData = sys.argv[3] # [0, 100]
    except IndexError:
        print_usage()
        sys.exit(1)

    if not valid_args(techniques.keys(), technique, posneg, percentData):
        print_usage()
        sys.exit(1)

    if posneg == 'True': posneg = True
    else: posneg = False
        
    print "Technique:", techniques[technique]
    if posneg: print "Positive/negative classification"
    else: print "5-star classification"
    print "% of data used:", percentData
    classify(technique, posneg, percentData)
