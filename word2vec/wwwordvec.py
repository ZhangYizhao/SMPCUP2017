import word2vec
import pandas as pd
from gensim.models import word2vec

model = word2vec.Word2Vec.load('model_word2vec.model').wv
blogs = pd.read_csv('word2vecpre.txt', header=None, sep=' ',
                        encoding='utf-8').astype(str)
i=0
results = []
while (i < 370):
    line = blogs.ix[i]

    result = []
    mean = 0
    for j in range(15):
        mean = mean + model[line.values[j]]
    result = mean / 15
    results.append(result)
    print(i)
    i = i + 1

pd.DataFrame(results).to_csv('test_370.txt', index=None, header=None, encoding='utf-8')
