# -*- coding: utf-8 -*-

import json
from scipy import sparse, io
from sklearn.externals import joblib
from SVM_Trainer import TrainerLinear
from SVM_Predictor import Predictor
from preprocess import split_data
from preprocess import dimensionality_reduction




class Evaluator:
    clf = joblib.load('/home/hadoop/myproject/demo/svm/SVM/model/SVM_linear_estimator.pkl')

    def __init__(self, training_data, training_target, test_data, test_target):
        self.trainer = TrainerLinear(training_data, training_target)
        self.predictor = Predictor(test_data, test_target)

    def train(self):
        #self.trainer.learn_best_param()
        self.trainer.train_classifier()
        joblib.dump(self.clf, '/home/hadoop/myproject/demo/svm/SVM/model/Terminal_estimator.pkl')
        Evaluator.clf = joblib.load('/home/hadoop/myproject/demo/svm/SVM/model/Terminal_estimator.pkl')

    def cross_validation(self):
        self.trainer.cross_validation()

    def predict(self, type):
        if type == 'sample_data':
            self.predictor.sample_predict(Evaluator.clf)
        elif type == 'new_data':
            self.predictor.new_predict(Evaluator.clf)


if '__main__' == __name__:
    content = io.mmread('/home/hadoop/myproject/demo/svm/vector_data/word_vector.mtx')
    new_content = io.mmread('/home/hadoop/myproject/demo/svm/vector_data/new_vector.mtx')
    with open('/home/hadoop/myproject/demo/svm/vector_data/train_label.json', 'r') as f:
        label = json.load(f)
    training_data, test_data, training_target, test_target = split_data(content, label, new_content)
    training_data, test_data = dimensionality_reduction(training_data.todense(), test_data.todense(), type='pca')
    evaluator = Evaluator(training_data, training_target, test_data, test_target)
    evaluator.train()
    #evaluator.cross_validation()
    evaluator.predict(type='new_data')



