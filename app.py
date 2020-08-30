import tensorflow as tf
import streamlit as st

import cv2

from PIL import Image,ImageOps
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)


#Hiding details of streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



model = tf.keras.models.load_model('model.hdf5')
    

st.title('Elon Musk  v/s  Jeff Bezos Classifier')

for i in range(5):
    st.write(" ")

st.write('## Lame attempt to pass time')

st.write(' ')

file_image = st.file_uploader('Upload JPG images only',type = ['jpg','png'])


def import_and_predict(image_data,model):
    size = (250,350)
    image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_resize = (cv2.resize(img,dsize = (125,125),interpolation=cv2.INTER_CUBIC))/255.

    img_reshape = img_resize[np.newaxis,...]

    prediction = model.predict(img_reshape)

    return prediction

if file_image is None:
    st.text('Please upload an image(jpg) file')
else:
    image = Image.open(file_image)
    st.image(image,use_column_width=True)
    prediction = import_and_predict(image,model)

    st.balloons()

    if np.argmax(prediction) == 0:
        st.write("# All Hail Mighty Musk!!")
    else:
        st.write("# All Hail Master Bezos!!")

for i in range(5):
    st.write(' ')

st.write('*Info: Used Xception model by transfer learning.*')
st.write('*Trained using 400 images and tested using 100 images.So accuracy will be low*')
st.write('*Accuracy on train set: 73% \n Accuracy on test set 62% *')

st.write("Please Don't be rough on my model")