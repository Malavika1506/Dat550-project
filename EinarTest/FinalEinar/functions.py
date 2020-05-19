# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:05:02 2020

@author: einar
"""
import ast
from collections import Counter
from scipy.sparse import csr_matrix
import numpy as np

def clean_url(x):
    x = x.replace('http://','').replace('https://','').replace('www.','')
    string = x.split('/')

    return string[0]



def create_binary(word_lists,n_common):
    
    a = [ ast.literal_eval(i) if type(i) ==str else "" for i in word_lists ]

    all_n = (gram for sublist in a for gram in sublist)

    popular_n = [i[0] for i in Counter(all_n).most_common(n_common)]

    the_matrix = csr_matrix((len(popular_n), len(a)), dtype=np.int8).toarray()
    for i,article_ngrams in enumerate(a):
            common_elements = np.in1d(popular_n,article_ngrams).nonzero() 
            the_matrix[common_elements,i] +=1

    
    return the_matrix.T