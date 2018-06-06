import gensim
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary = True)

from keras.models import Model, load_model

sc_model = load_model('Sentiment_Classification_model.h5')


def sentence_to_vector(line):
    assert len(line.split()) <= 40, 'This length of sentence must be less or equal to 40'
    result = np.zeros((1,40, 300))
    line = line.replace('.','').replace(',','').replace(':','').replace('!','').replace(';','').replace('?','')
    words = line.split()
    for i in range(len(words)):
        if words[i] in model.vocab.keys():
            result[0,i,:] = model[words[i]] 
    return result

print(sc_model.predict(sentence_to_vector('Good to see you')))


from wxpy import *

bot = Bot(cache_path = True)

@bot.register()
def print_message(msg):
    print(msg.text)
    if sc_model.predict(sentence_to_vector(msg.text)) > 0.5:
        print('Good')
        return 'Thank you!'
    else:
        print('Bad')
        return 'Dont say that'

embed()

