import gensim
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary = True)
count = 0
max_len = 40
sentences = np.zeros((7086,max_len,300))
Y = []
print('Model initialized success')
with open('training.txt','r',encoding = 'utf8') as f:
    for line in f:
        line = line.replace('.','').replace(',','').replace(':','').replace('!','').replace(';','').replace('?','')
        words = line.split()[1:]
        Y.append(line.split()[0])
        for i in range(len(words)):
            if words[i] in model.vocab.keys():
                sentences[count,i,:] = model[words[i]] 
        count += 1

F = open('X_input.pkl','wb')
import pickle
pickle.dump(sentences, F)
F.close()
Y = np.array(Y)

D = open('Y_output.pkl','wb')
pickle.dump(Y, D)
D.close()




