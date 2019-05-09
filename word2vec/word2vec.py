from gensim.models import word2vec
import pandas as pd
import re
# make a word2vec model


def word2vec_model(blog_seg_path):
    sentences = word2vec.LineSentence(blog_seg_path)
    model = word2vec.Word2Vec(sentences, size=100, workers=4)
    return model




if __name__ == '__main__':
    T=1
    F=0
    i=1
    train_y = []
    blogs = pd.read_csv('trainuserkeywords.csv', header=None, sep=',', names=['id', 'l1', 'l2', 'l3','text'],encoding='utf-8')
    labels = pd.read_csv('SMPCUP2017_LabelSpace_Task2.txt', header=None, encoding='gbk')
    while(i<371):
        line = blogs.ix[i]
        j = 0
        train = []
        while(j<42):
            if(labels.values[j] == line.values[1]):
                train.append(T)
            elif(labels.values[j] == line.values[2]):
                train.append(T)
            elif(labels.values[j] == line.values[3]):
                train.append(T)
            else:
                train.append(F)
            j = j + 1
        train_y.append(train)
        i=i+1
        print(train)
    pd.DataFrame(train_y).to_csv('y_train1.txt', index=None, header=None, encoding='utf-8')



