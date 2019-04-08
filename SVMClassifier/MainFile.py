from nlp_rake import rake
import json
from sklearn import model_selection, naive_bayes, svm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from joblib import dump, load
import numpy as np

np.random.seed(500)

stoppath = 'data/stoplists/SmartStoplist.txt'

traindata = 'C:/Users/Hiresh/PycharmProjects/Hackaton19/Data/arxivData.json'

rake_object = rake.Rake(stoppath, 4, 3, 1)

trainset = []
trainlabel = []

with open(traindata, 'r') as f:
    datastore = json.load(f)
    print(datastore)

for data in datastore:
    keywords = rake_object.run(data['summary'])
    # 3. print results
    for keyword in keywords:
        if len(str(keyword[0]).split(" "))>1:
            #print(keyword[0],keyword[1])
            trainset.append(keyword[0])
            if int(keyword[1]) > 7.5:
                trainlabel.append("core")
            elif int(keyword[1]) > 5:
                trainlabel.append("ph")
            else:
                trainlabel.append("other")

print(trainlabel)
print(trainset)
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(trainset,trainlabel,test_size=0.3)

Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)

Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(trainset)

Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)

dump(Tfidf_vect, 'tfid.joblib')

SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)

dump(SVM, 'filename.joblib')

#sample_file = open("data/docs/fao_test/w2167e.txt", 'r', encoding="iso-8859-1")
#text = sample_file.read()


