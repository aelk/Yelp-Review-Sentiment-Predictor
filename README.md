# Yelp Review Sentiment Predictor

## About

Given a Yelp review, this project builds two types of classifiers to assign to the review 1) a positive or negative sentiment, and 2) a rating in the interval [1, 5]. We use either Naive Bayes, SVM, or Logistic Regression as the model, and the [Yelp dataset](http://www.yelp.com/dataset_challenge/) to train the classifier.

## Motivation

From Section 1.2 of `predicting-sentiment-yelp.pdf`: "It is useful for Yelp to associate review text with a star rating (or at least a positive or negative assignment) accurately in order to judge how helpful and reliable certain reviews are. Perhaps users could give a good review but a bad rating, or vice versa. Also Yelp might be interested in automating the rating process, so that all users would have to do is write the review, and Yelp could give a suggested rating."

## Example

The user can specify which type of classification to perform (positive/negative or 5-star), which technique to use (Naive Bayes, SVM, or Logistic Regression), and how much data to use.

Assuming you have the Yelp review dataset in the same directory as `classify.py`, the following will build a Logistic Regression classifier for 5-star classification using 80% of the data:

```
classify.py svm False 80
```

In general, the classifier is used as follows:

```
classify.py <nb/svm/lr> <True/False> <number in [0, 100]>
```

where `True` indicates positive/negative classification, and `False` indicates 5-star classification.

## Installation

1. Get the Yelp data [here](https://www.yelp.com/dataset_challenge/dataset).

2. [Install scikit-learn](http://scikit-learn.org/stable/install.html).

3. Save `classify.py` and `yelp_utils.py` in the same directory as the Yelp data, and run `classify.py` as described in the Example section above.
Provide code examples and explanations of how to get the project.

## License

Copyright (c) 2015 Andrew Elkouri, released under the MIT license.
