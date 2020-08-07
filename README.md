# Pneumonia-Detection
This is the Pneumonia detection web app wherein user need to uplaod chest x-ray image to diagnose if the patient has Pneumonia or not.
* You may refer my kaggle notebook which explains training of models. [kaggle notebook](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
### Steps followed to create this project:
  * Collected a dataset consisting x-ray images from kaggle. [here is the dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
  * Made a split of data as training, validation and test dataset.
  * Trained three different models:
      1. Simple CNN model
      2. VGG-16 model
      3. ResNet50 model
  * Saved the model which gave best accuracy.
  * Created a django app for making the classification.
  
## Want to run on your pc?
 * Download the zip and extract. 
 * Make sure your system tensorflow 2.0.
 * Make sure your cmd path is same as your working directory i.e 'xray_scan' directory, then run the local server using 'python manage.py runserver' command.
 * This is how homepage looks like :
 
 ![homepage](https://github.com/abhi9137/Pneumonia-Detection/blob/master/xray_scan/homepage.JPG)
 
 * Uplaod chest x-ray image to diagnose the x-ray
 * This is how output page looks like :
 
 ![output](https://github.com/abhi9137/Pneumonia-Detection/blob/master/xray_scan/output.JPG)
 
 ### For better understanding of training of models please go through my [kaggle notebook](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia), do upvote and suggest changes if any.
 
