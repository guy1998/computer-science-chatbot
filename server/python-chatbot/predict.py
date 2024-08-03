import random
import json
import pickle
import numpy as np
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

no_information_responses = ["Sorry, I do not have information on that topic!", "I am not sure if I can help you with that!", "That information is unavailable. Try asking something else!"]

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')


# This function breaks the sentence into words, lemmatizes them, and generates n-grams
def clean_up_sentences(sentence, n=2):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    # Generate n-grams
    ngrams_list = []
    for i in range(1, n+1):
        ngrams_list.extend([' '.join(ngram) for ngram in ngrams(sentence_words, i)])
    return ngrams_list


# This function finds the tag where each n-gram is present
def bagw(sentence):
    sentence_words = clean_up_sentences(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


# Here we make the prediction based on the information we have
# about each word being present in respective tags
def predict_class(sentence):
    bow = bagw(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res)
               if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]],
                            'probability': str(r[1])})
        return return_list
    return return_list


# This gets the response based on the tag that was predicted
# it randomly selects one of the intents present on that tag
def get_response(intents_list, intents_json):
    if len(intents_list) == 0:
        return random.choice(no_information_responses)
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def respond(prompt):
    ints = predict_class(prompt)
    res = get_response(ints, intents)
    return res
