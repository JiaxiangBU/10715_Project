import gensim
import numpy as np
import pickle

# Load the model
model = gensim.models.KeyedVectors.load_word2vec_format('Data/Embeddings/Full/GoogleNews-vectors-negative300.bin', binary=True)

# Get an array of CIFAR Labels
infile = open("Data/Labels/CIFAR_100_labels.txt", "r")
line = infile.readline()
words = {}
for line in infile:
    row = line.rstrip().rstrip(',').split(', ')
    for word in row:
        words[word] = 0

# Gather the relevant models
word_embeddings = {}
for word in words:
    if word == 'aquarium fish':
        word = (model['aquarium'] + model['fish']) / 2	# Can potentially change this
    else:
        word_embeddings[word] = model[word]

# Save the file
pickle.dump(word_embeddings, open("Data/Embeddings/CIFAR/CIFAR_w2v_google.pk", "wb"))


