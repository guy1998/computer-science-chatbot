
# importing the required modules.
import random
import json
import pickle
import numpy as np
import nltk

from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

print("-------------STARTING PREPROCESSING----------------")
lemmatizer = WordNetLemmatizer()

stop_words = set(json.loads(open('custom_stopwords_en.json').read())['stopwords'])
intents = json.loads(open('intents.json').read())

words = []  # All possible words in the dataset
classes = []
documents = []  # Tuples of patterns and associated tags
ignore_words = set(nltk.corpus.stopwords.words('english')).union(set(["?", "!", ".", ","]))
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each pattern into words
        word_list = nltk.word_tokenize(pattern)
        word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list if word.lower() not in ignore_words]

        # Generate bi-grams
        bigrams = list(ngrams(word_list, 2))
        combined_list = word_list + [' '.join(bigram) for bigram in bigrams]

        words.extend(combined_list)
        # Add the document as a tuple (combined_list, tag)
        documents.append((combined_list, intent['tag']))
        # Ensure each tag is added to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and sort words, removing duplicates
words = sorted(set(words))
classes = sorted(set(classes))

# saving the words and classes into binary files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Training will be a list of list that will basically have the possible inputs
# related with the possible patterns and the label will be the tag
training = []
# the output empty vector will be used later on to create a vector that has
# the number one precisely at the index that indicates the output tag
output_empty = [0] * len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns]
    # Checking which word is in the set of words for each pattern
    # this comes in handy to the model to determine which of the patterns
    # is most likely to be the correct pattern that the user has requested
    # with his input
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    # making a copy of the output_empty and placing 1 where the expected output tag should be
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)  # Shuffling the array
training = np.array(training, dtype=object)

# Ensure homogeneous shape of training data
train_x = np.array([np.array(x[0]) for x in training])
train_y = np.array([np.array(x[1]) for x in training])
print("Preprocessing finished")

print("-------------STARTING TRAINING----------------")


model = Sequential()
model.add(Dense(256, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.8, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
hist = model.fit(train_x, train_y, epochs=300, batch_size=8, verbose=1)

# Save the model
model.save("chatbotmodel.h5", hist)

print("-------------TRAINING SUCCESSFUL----------------")
