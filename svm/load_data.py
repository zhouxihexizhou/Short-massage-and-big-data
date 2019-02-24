# -*- coding: utf-8 -*-
# from numpy import *
import json
import csv

# 加载原始数据，进行分割
def load_message():
    content = []
    label = []
    lines = []
    new_content = []
  
    with open('/home/hadoop/myproject/demo/svm/raw_data/message.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in range(960):
            line = csvfile.readline()
            lines.append(line)
        num = len(lines)
        for row in range(num):
            message = lines[row].split(',')
            label.append(message[0])
            content.append(message[2])

    with open('/home/hadoop/myproject/demo/svm/raw_data/new.csv','r') as newfile:
        new_reader = csv.reader(newfile)
        for row in new_reader:
            new_content.append(row[2])

    return num, content, label, new_content


def data_storage(content, label, new_content):
    with open('/home/hadoop/myproject/demo/svm/raw_data/train_content.json', 'w') as f:
        json.dump(content, f)
    with open('/home/hadoop/myproject/demo/svm/raw_data/train_label.json', 'w') as f:
        json.dump(label, f)
    with open('/home/hadoop/myproject/demo/svm/raw_data/new_content.json', 'w') as f:
        json.dump(new_content, f)


if '__main__' == __name__:
    num, content, label, new_content = load_message()
    data_storage(content, label, new_content)





