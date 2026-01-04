#!/usr/bin/env python
# coding: utf-8

# In[9]:


def unigram_probability(corpus: str, word: str) -> float:
    total_words = len(corpus.split())
    count_w = corpus.count(word)
    return round(count_w / total_words, 4)


# In[10]:


corpus = "<s> Jack I like </s> <s> Jack I do like </s>"
word = "Jack"
print(unigram_probability(corpus, word))

