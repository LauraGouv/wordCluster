# coding: utf-8

import pandas as pd
from gensim.models import Word2Vec, KeyedVectors
import copy
import numpy as np
import nltk
import os

#constantes:
num_clusters = 700

#iniciando o script
print('iniciando o script')

#pegando o dataframe
df = pd.read_csv('data/laptop_filtered_aspect_sample.csv')
df

words = df.values.tolist()
clean_words = []
clean_vector = []
for word in words:
    clean_words.append(nltk.word_tokenize(word[0]))
for word in words:
    clean_vector.append(word[0].split(" "))

#treinando o modelo de wordvec
model = Word2Vec(sg=0, ns_exponent=0.75,min_count=1, size=32, workers=1, seed = 1234)
model.build_vocab(clean_words, progress_per=10000)
model.train(clean_words, total_examples=model.corpus_count, epochs=30, report_delay=1)
print('modelo de palavras iniciado')

#criando o vetor de palavras
np_vector = []
np_label = []
for vec in clean_vector:
    count = 0
    string = ''
    aux = []
    exist = False
    for word in vec:
        if word in  model.wv.vocab:
            string += word + ' '
            aux.append(model[word])
            exist = True
    if exist:
        aux = sum(aux)/len(aux)
        np_vector.append(aux)
        np_label.append(string)

#colocando o modelo do TSNE
from sklearn.manifold import TSNE
SNEt = TSNE(n_components=2, random_state=1)
tsne_data = SNEt.fit_transform(np_vector)
print('modelo pronto')

#criando a lista de palavras com as coordenadas
tsne_word = []
for key, tupla in enumerate(tsne_data):
    tsne_word.append(tsne_data[key].tolist())
    tsne_word[key].append(np_label[key])
tsne_word

#transformando em um DataFrame
sne_pd = pd.DataFrame(tsne_word, columns=['X','Y','Word'])
sne_pd

#usando k-means
from sklearn.cluster import KMeans

#Fazendo o agrupamento pelo K-Means depois de reduzir as dimensões
#treinando o modelo
clustering = KMeans(n_clusters=num_clusters, random_state=0)
clustering.fit(sne_pd[['X','Y']])
predictClusterKMeans = clustering.predict(sne_pd[['X','Y']])
sne_pd['Group'] = predictClusterKMeans
print('agrupamento concluído')

#ordenando por grupo
sne_pd = sne_pd.sort_values('Group')

#criando o arquivo resposta
import glob
files_present = True
while(files_present):
    name = input('nome que deseja para o arquivo resposta: ')
    filename = name + '.csv'
    files_present = glob.glob(filename)
    if not files_present:
        sne_pd.to_csv(filename, encoding='utf-8', index=False, columns=['Word','Group'])
        file_path = os.getcwd()
        print('arquivo salvo em: ' + file_path + '\\' + filename)
    else:
        print('Esse Arquivo Já Existe, Tente novamente') 
        