from gensim.models import word2vec
from gensim.test.utils import datapath
import pandas as pd
import re
# make a word2vec model


def word2vec_model(blog_seg_path):
    sentences = word2vec.LineSentence(blog_seg_path)
    model = word2vec.Word2Vec(sentences, size=100, workers=4, min_count=2)
    return model



if __name__ == '__main__':
    i = 0
    results = []
    blogs = pd.read_csv('word2vecpre.txt', header=None, sep=' ',
                        encoding='utf-8').astype(str)
    while(i<37585):
        line = blogs.ix[i]
        result = []
        for j in range(15):
            result.append(line.values[j])
        results.append(result)
        i=i+1
    model = word2vec.Word2Vec(results, size=100, workers=4, min_count=1)
    model.save("model_word2vec.model")
    #word2vec_model('final_list.txt').save("model_word2vec.model")
        #model = word2vec.Word2Vec(blog_in, size=100, workers=4, min_count=1)
        #model.save("model_word2vec.model")