# Classifier-Transfer-Learning

## Elon Musk v/s Jeff Bezos Classifer


Here i created a classifer which takes an image and tells if it's Jeff Bezos or Elon Musk<br/>
I created this classifer using Transfer Learning  trained<br/>
Model used is Xception<br/>

*Accuracy is low since it was trained on 400 images and tested on 100 images only*

*Created a static web app using Streamlit but failed to deploy in Heroku due to 500mb Slug size limit since model is about 300mb.*

Dataset(images) for training and testing can be generated using Google Images Scraper Notebook  or using this repo [Link](https://github.com/ultralytics/google-images-download)

Front 

![Front](https://github.com/SanjayGBot/Classifier-Transfer-Learning/blob/master/Images/Screenshot%20(11).png)

Elon Musk

![Elon Musk](https://github.com/SanjayGBot/Classifier-Transfer-Learning/blob/master/Images/Screenshot%20(12).png)

Jeff Bezos

![Jeff Bezos](https://github.com/SanjayGBot/Classifier-Transfer-Learning/blob/master/Images/Screenshot%20(13).png)

### Model is not uploaded on github due to large size but Xception can be downloaded and trained using the code in Model Preparation notebook
