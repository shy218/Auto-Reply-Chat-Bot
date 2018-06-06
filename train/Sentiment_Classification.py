import numpy as np
from keras.models import Model
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.initializers import glorot_uniform
import pickle
F = open('X_input.pkl','rb')
X = pickle.load(F)
D = open('Y_output.pkl','rb')
Y = pickle.load(D)

max_len = 40

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)



def Sentiment_Classification():
    X_input = Input(shape = (max_len, 300), dtype = 'float')
    X = LSTM(128, return_sequences = True)(X_input)
    X = Dropout(0.5)(X)
    X = LSTM(128)(X)
    X = Dropout(0.5)(X)
    X = Dense(1, activation = 'sigmoid')(X)

    model = Model(inputs = [X_input], outputs = [X])

    return model

model = Sentiment_Classification()
model.summary()

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['accuracy'])

model.fit(X_train, Y_train, epochs = 10, batch_size = 64, shuffle = True)

loss, acc = model.evaluate(X_test, Y_test)
print(acc)

model.save('Sentiment_Classification_model.h5')
