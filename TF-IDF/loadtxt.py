import jieba
import re
import time

# init jieba
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




if __name__ == "__main__":
    with open("test.txt", encoding='gbk') as blog_in:
        with open("blog_segment.txt", "w", encoding='utf-8') as blog_out:
            blog_out.writelines([' '.join(line) for line in segment(blog_in.readlines())])

