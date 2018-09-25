# Auto-Reply-Chat-Bot
This program can determine whether a sentence is good or bad using RNN with Keras.
It is combined with Wechat to create an Auto reply chat Bot.

## Quickstart

To use this model, you need to first download the word embedding model from Google (1.5G). https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing

You need to install gensim, numpy and wxpy to load the model.

gensim is an API to load Word Embedding model.

'''
pip install gensim
'''


wxpy is the API from Wechat. When you start the load_model.py, it will create a QS code.
You need to scan it by wechat to log in.

'''
pip install wxpy
'''
