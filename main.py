from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble
import pandas, xgboost, numpy, string
from keras.preprocessing import text, sequence
from keras import layers, models, optimizers
data = pandas.read_excel('data.xlsx');
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(data['Task'], data['time'])
# load the pre-trained word-embedding vectors 
embeddings_index = {}
for i, line in enumerate(open('wiki-news-300d-1M.vec')):
    values = line.split()
    embeddings_index[values[0]] = numpy.asarray(values[1:], dtype='float32')

# create a tokenizer 
token = text.Tokenizer()
token.fit_on_texts(data['Task'])
word_index = token.word_index
# convert text to sequence of tokens and pad them to ensure equal length vectors 
train_seq_x = sequence.pad_sequences(token.texts_to_sequences(train_x), maxlen=70)
valid_seq_x = sequence.pad_sequences(token.texts_to_sequences(valid_x), maxlen=70)

# create token-embedding mapping
embedding_matrix = numpy.zeros((len(word_index) + 1, 300))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

# create a count vectorizer object 
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(data['Task'])

# transform the training and validation data using count vectorizer object
xtrain_count =  count_vect.transform(train_x)
xvalid_count =  count_vect.transform(valid_x)

mdl = ensemble.RandomForestRegressor().fit(train_seq_x, train_y)
sprint(mdl.predict(count_vect.transform(["finishing homework"])))

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    word = request.args.get('word')
    print("processing " + word)
    return mdl.predict(sequence.pad_sequences(token.texts_to_sequences([word]), maxlen=70))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
