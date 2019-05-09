
import jieba.analyse
import jieba
import pandas as pd
import re
import h5py
import pickle

jieba.load_userdict("dict1.txt")
with open("chinese_stopwords.txt", encoding='utf-8') as fstop:
    stop_words = fstop.read().split()
# segmentation

def segment(blogs):
    seg_blogs  = [filters([word for word in jieba.cut(article) if word not in stop_words]) for article in blogs]
    return seg_blogs
# filter for words


def filters(tags):
    # remove pure numbers
    tags = [word for word in tags if re.match('^\d+(\.\d+)?$', word) == None]
    # remove substring
    for i in tags:
        for j in tags:
            if i != j and i in j:
                tags.remove(i)
                break
    return tags


def tf_idf(texts):
    #jieba.load_userdict("dict1.txt")
    #jieba.analyse.set_idf_path("idf.txt")
    #jieba.analyse.set_stop_words("stopwords.txt")

    corpus = [filters(jieba.analyse.extract_tags(s, topK = 15)) for s in texts]
    return corpus

if __name__ == '__main__':
    i = 0
    texts = []
    # Enter blog original text
    blogs = pd.read_csv('blog_segment.csv', header=None, sep=',', names=['id', 'title', 'text'], encoding='utf-8').astype(str)
    # Increase the weight of the title and remove the ellipsis
    #blogs = pd.read_pickle("sorted_data.pickle")
    while(i<100):
        line = blogs.ix[i]
        text1 = line.values[1]*4 + line.values[2]
        texts.append(text1)
        i=i+1

    tfidf0 = tf_idf(texts)

    # Calculate the topic of each article
    tfidf_corpus = pd.DataFrame(tfidf0)
    # Output the result
    result = pd.DataFrame({'keyword1': tfidf_corpus[0],'keyword2': tfidf_corpus[1],
                           'keyword3': tfidf_corpus[2]})
    result.to_csv('ans_task1.txt', index=None, encoding='utf-8')

    tfidf_corpus.to_csv('top15.txt', index=None, encoding='utf-8')
    print(type(tfidf_corpus))
