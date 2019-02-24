from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('data', __name__)

import os
import functools
import csv

@bp.route('/')
def index():
    return render_template('data/index.html')



@login_required
@bp.route('/upload',methods=('GET','POST'))
def upload():
    if request.method == 'POST':
       # import pdb; pdb.set_trace()
      
        username = g.user['username']
        os.system('sudo rm -rf ./cache/'+username+'2')
        os.system('mkdir ./cache/'+username+'2')

        f = request.files['file']
        os.system('sudo cp ./source/'+f.filename+' ./cache/'+username+'2')
        os.system('sudo mv ./cache/'+username+'2/'+f.filename+' ./cache/'+username+'2/message2.csv')

        os.system('/usr/local/hadoop/bin/hdfs dfs -mkdir '+username)
        os.system('/usr/local/hadoop/bin/hdfs dfs -put ./cache/'+username+'2/message2.csv '+username)
     
        os.system('/usr/local/hadoop/bin/hadoop fs -getmerge '+username+' message.csv')
        os.system('/usr/local/hadoop/bin/hdfs dfs -rm -r '+username+'')
        os.system('/usr/local/hadoop/bin/hdfs dfs -mkdir '+username)
        os.system('/usr/local/hadoop/bin/hdfs dfs -put ./message.csv '+username)
        os.system('sudo rm ./message.csv')

    return render_template('data/index.html')


@bp.route('/solve')
def solve():
    username = g.user['username']
    os.system('/usr/local/hadoop/bin/hdfs dfs -get '+username+'/message.csv ~/myproject/demo/svm')
    os.system('sudo mv /home/hadoop/myproject/demo/svm/message.csv /home/hadoop/myproject/demo/svm/raw_data/new.csv')
    os.system('python3 /home/hadoop/myproject/demo/svm/load_data.py')
    os.system('python3 /home/hadoop/myproject/demo/svm/word_vector.py')
    os.system('python3 /home/hadoop/myproject/demo/svm/SVM/SVM_Trainer.py')
    os.system('python3 /home/hadoop/myproject/demo/svm/SVM/SVM_Evaluator.py')
    os.system('python3 /home/hadoop/myproject/demo/svm/match.py')
    return render_template('data/index.html')


@bp.route('/result')
def result():
    print('省份：')
    with open('/home/hadoop/myproject/demo/svm/match/province.txt','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    print('\n城市：')
    with open('/home/hadoop/myproject/demo/svm/match/city.txt','r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    return render_template('data/index.html')




