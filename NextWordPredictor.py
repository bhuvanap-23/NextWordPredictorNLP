#import the libraries

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Emberdding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
import pickle
import numpy as np
import os

from google.colab import files
uploaded = files.upload()

#load and pre-process the data
file = open("dataFile.txt","r",encoding="utf8")

#store file in list
lines=[]
for i in lines:
  lines.append(i)

#convert list to string
data=""
for i in lines:
  data=' '.join(lines)

#replace unnecessary with space
data=data.replace('\n','').replace('\r','').replace('\ufeff','').replace('"','')

#remove unnecessary spaces
data=data.split()
data=''.join(data)
data[:500]

#Tokenization
tokenizer=Tokenizer()
tokenizer.fit_on_texts([data])

#save the tokenizer for predict function
pickle.dump(tokenizer,open('token.pk1','wb'))
sequence_data=tokenizer.texts_to_sequences([data])[0]
sequence_data[:15]

sequences=[]
for i in range(3,len(sequence_data)):
  words=sequence_data[i-3:i+1]
  sequences.append(words)

sequences=np.array(sequences)
sequences[:10]

#dependent and independent variables
x=[]
y=[]
for i in sequences:
  x.append(i[0:3])
  y.append(i[3])

x=np.array(x)
y=np.array(y)

y=to_categorical(y,num_classes=vocab_size)

#creating the model
model=Sequential()
model.add(Embedding(vocab_size,10,input_length=3))
model.add(LSTM(1000,return_sequences=True))
model.add(LSTM(1000))
model.add(Dense(1000,activation="relu"))
model.add(Dense(vocab_size,activation="softmax"))
model.summary()

#plot the model
from tensorflow import keras
from keras.utils.vis_utils import plot_model
keras.utils.plot_model(model,to_file='plot.png',show_layer_names=True)

#build the model
from tensorflow.keras.callbacks import ModelCheckPoint
checkpoint = ModelCheckPoint("TextWords.h5",monitor='loss',verbose=1,save_best_only=True)
model.compile(loss='categorical_crossentropy",optimizer=Adam(learning_rate=0.001))
model.fit(x,y,epochs=70,batch_size=64,callbacks=[checkpoint])

#prediction
from tensorflow.keras.models import load_model
import numpy as np
import pickle

#load the model and tokenizer
model=load_model('nextWords.h5')
tokenizer=pickle.load(open('token.pk1','rb'))

def Predict_Next_Words(model,tokenizer,text):
  sequence=tokenizer.texts_to_sequences([text])
  sequence=np.array(sequence)
  preds=np.argmax(model.predict(sequence))
  predicted_word=""

  for key,value in tokenizer.word_index.items():
    if value==preds:
      predicted_word=key
      break
  print(predicted_word)
  return predicted_word


while(True):
  text=input("Enter the words:")

  if text=="0":
    print("Execution completed.....")
    break

  else:
    try:
        text=text.split(" ")
	text=text[-3:]
	print(text)

	Predict_Next_Words(model,tokenizer,text)

    except Exception as e:
      print("Error occured:",e)
      continue




















  



























