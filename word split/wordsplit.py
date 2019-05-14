import jieba.analyse
import jieba
import pandas as pd
import re


jieba.load_userdict("dict1.txt")
with open("chinese_stopwords.txt", encoding='utf-8') as fstop:
    stop_words = fstop.read().split()
with open ('common dic.txt', encoding='utf-8') as fskip:
    skip_words=fskip.read().split()
# segmentation
def segment(blogs):#切出词语
    seg_blogs = [filter([word for word in jieba.cut(article) if word not in stop_words]) for article in blogs]
    for i in range(len(seg_blogs)):
        for j in range (len(seg_blogs[i])):
            for word in  seg_blogs[i][j]:
               if re.match('[a-zA-Z]',word) and seg_blogs[i][j] not in skip_words:
                   seg_blogs[i][j]=''
    return seg_blogs
# filter for words

def filter(tags):
    # remove pure numbers

    tags = [word for word in tags if re.match('^\d+(\.\d+)?$', word) == None]
    tags = [word for word in tags if re.match('^(?=.*\d)(?=.*[a-zA-Z])[\u4E00-\u9FA5a-zA-CE-Z0-9]*$', word) == None]
    tags = [word for word in tags if re.match('\d+\.?\d*', word) == None]
    tags = [word for word in tags if re.match(u'[’!"#$%&\'()*+（）,-.￥—/:;<=>?@，。●?★_、–∑ ≤−「≥∗∈ ′…【】《》\？“”‘’！[\\]^__`{|}~]+', word) == None]


    # remove substring
    for i in tags:
        for j in tags:
            if i != j and i in j:
                tags.remove(i)
                break
    return tags




if __name__ == '__main__':
    blogs=pd.read_csv("part_2.txt",header=None,sep='\001',names=['id', 'title', 'text']).astype(str)
    # segmentation
    blogs['text'] = [' '.join(line) for line in (segment(blogs['text']))]
    blogs['title']= [' '.join(line) for line in (segment(blogs['title']))]
    blogs.to_csv('blog_segment11.csv',encoding='utf-8')
