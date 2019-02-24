import csv

def match():
    labels = []
    area_number = []
    
    with open(r'/home/hadoop/myproject/demo/svm/SVM/result/predict_label.txt','r',encoding='utf-8') as f:
        labels = f.read()

    with open('/home/hadoop/myproject/demo/svm/raw_data/new.csv','r') as fr:
        reader = csv.reader(fr)
        for row in reader:
            if labels[int(row[4],base=10)-1] == '1':
                s = row[3]
                s = s[3:7]
                area_number.append(s)
    return labels, area_number


def seek(area_number):
    province = []
    city = []

    with open('/home/hadoop/myproject/demo/svm/match/number_area.csv','r') as f:
        reader = csv.reader(f)
        for row in reader:
            for t in area_number:
                if row[0]==t:
                    province.append(row[1])
                    city.append(row[2])
        
    with open('/home/hadoop/myproject/demo/svm/match/province.txt','wt') as f:
        for i in range(len(province)):
            f.writelines(province[i])
            f.write('\n')
    with open('/home/hadoop/myproject/demo/svm/match/city.txt','wt') as f:
        for i in range(len(city)):
            f.writelines(city[i])
            f.write('\n')
    print('ok')


if '__main__' == __name__:
    labels, area_number = match()
    seek(area_number)


