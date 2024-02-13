from tensorflow.keras.models import Model
from tensorflow.keras import models
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import Input,LSTM,Dense
from sklearn.feature_extraction.text import CountVectorizer

import numpy as np
import pickle

#initialize all variables
input_texts=[]
target_texts=[]
input_characters=set()
target_characters=set()


#read dataset file
with open('eng-french.txt','r',encoding='utf-8') as f:
    rows=f.read().split('\n')

#read first 10,000 rows from dataset
for row in rows[:10000]:

    #split input and target by '\t'=tab
    input_text,target_text = row.split('\t')

    #add '\t' at start and '\n' at end of text.
    target_text='\t' + target_text + '\n'
    input_texts.append(input_text.lower())
    target_texts.append(target_text.lower())

    #split character from text and add in respective sets
    input_characters.update(list(input_text.lower()))
    target_characters.update(list(target_text.lower()))

    # sort input and target characters
    input_characters = sorted(list(input_characters))
    target_characters = sorted(list(target_characters))

    # get the total length of input and target characters
    num_en_chars = len(input_characters)
    num_dec_chars = len(target_characters)

    # get the maximum length of input and target text.
    max_input_length = max([len(i) for i in input_texts])
    max_target_length = max([len(i) for i in target_texts])

    print("number of encoder characters : ", num_en_chars)
    print("number of decoder characters : ", num_dec_chars)

    print("maximum input length : ", max_input_length)
    print("maximum target length : ", max_target_length)