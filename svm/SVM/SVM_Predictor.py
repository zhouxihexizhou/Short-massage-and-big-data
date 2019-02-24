# -*- coding: utf-8 -*-
from sklearn import metrics


class Predictor:
    def __init__(self, test_data, test_target):
        self.test_data = test_data
        self.test_target = test_target

    def sample_predict(self, clf):
        test_result = clf.predict(self.test_data)
        print ('Zhouxi is very very cool')
        print (metrics.classification_report(self.test_target, test_result))
        print (metrics.confusion_matrix(self.test_target, test_result))

    def new_predict(self, clf):
        test_result = clf.predict(self.test_data)
        with open('/home/hadoop/myproject/demo/svm/SVM/result/predict_label.txt', 'wt') as f:
            for i in range(len(test_result)):
                f.writelines(test_result[i])
        self.test_target = test_result
        print ('write over')




