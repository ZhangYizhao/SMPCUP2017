from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
import jieba

with open("chinese_stopwords.txt", encoding='utf-8') as fstop:
    stop_words = fstop.read().split()


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


def make_idf(corpus):
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    vectorizer.fit_transform(corpus)
    return vectorizer


if __name__ == '__main__':

    with open("blog_segment.txt", "r", encoding='utf-8') as fblog:
        text = fblog.readlines()
    # segmentation
    corpus = [' '.join(line) for line in segment(text)]
    # make idf.txt
    vec = make_idf(corpus)
    pd.DataFrame({'col1':vec.get_feature_names(), 'col2':vec.idf_}).to_csv("idf.txt", encoding='utf-8', sep=' ', index=None, header=None)
