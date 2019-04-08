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

keywords = rake_object.run("Multiple hypothesis testing is a core problem in statistical inference and\narises in almost every scientific field. Given a set of null hypotheses\n$\\mathcal{H}(n) = (H_1,\\dotsc, H_n)$, Benjamini and Hochberg introduced the\nfalse discovery rate (FDR), which is the expected proportion of false positives\namong rejected null hypotheses, and proposed a testing procedure that controls\nFDR below a pre-assigned significance level. Nowadays FDR is the criterion of\nchoice for large scale multiple hypothesis testing. In this paper we consider\nthe problem of controlling FDR in an \"online manner\". Concretely, we consider\nan ordered --possibly infinite-- sequence of null hypotheses $\\mathcal{H} =\n(H_1,H_2,H_3,\\dots )$ where, at each step $i$, the statistician must decide\nwhether to reject hypothesis $H_i$ having access only to the previous\ndecisions. This model was introduced by Foster and Stine. We study a class of\n\"generalized alpha-investing\" procedures and prove that any rule in this class\ncontrols online FDR, provided $p$-values corresponding to true nulls are\nindependent from the other $p$-values. (Earlier work only established mFDR\ncontrol.) Next, we obtain conditions under which generalized alpha-investing\ncontrols FDR in the presence of general $p$-values dependencies. Finally, we\ndevelop a modified set of procedures that also allow to control the false\ndiscovery exceedance (the tail of the proportion of false discoveries).\nNumerical simulations and analytical results indicate that online procedures do\nnot incur a large loss in statistical power with respect to offline approaches,\nsuch as Benjamini-Hochberg.")
SVM = load('filename.joblib')
phrases=[]
labels=[]
for keyword in keywords:
    if len(str(keyword[0]).split(" ")) > 1:
        # print(keyword[0],keyword[1])
        phrases.append(keyword[0])
        if int(keyword[1]) > 7.5:
            labels.append("core")
        elif int(keyword[1]) > 5:
            labels.append("ph")
        else:
            labels.append("other")

Tfidf_vect = load('tfid.joblib')
phrases_Tfidf = Tfidf_vect.transform(phrases)

predictions_SVM = SVM.predict(phrases_Tfidf)
for i in range(len(phrases)):
    #print(phrases[i])
    if predictions_SVM[i]==0:
        print(phrases[i]+' - '+ 'core')
    elif predictions_SVM[i]==1:
        print(phrases[i]+' - '+'Peripheral')
    else:
        print(phrases[i]+' - '+'other')