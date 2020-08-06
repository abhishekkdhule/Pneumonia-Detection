from django.shortcuts import render,redirect
from .models import *
from .forms import *
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow import Graph
import json
import numpy as np



with  open('./models/labels.json','r') as f:
    labelInfo=f.read()

labelInfo=json.loads(labelInfo)

# model_graph=Graph()
# with model_graph.as_default():
#     tf_session=tf.compat.v1.keras.backend.get_session()
#     with tf_session.as_default():
model=load_model('./models/PNP.h5')

# Create your views here.
def homepage(request):
    if os.path.exists('homepage/static/homepage/image/image.jpg'):
        os.remove('homepage/static/homepage/image/image.jpg')
    object1=Upload_img.objects.all()
    if len(object1)>0:
        Upload_img.objects.all().delete()
    context={}
    form=Upload_form(request.POST or None, request.FILES or None)
    # print(request.FILES['img'])
    # request.FILES['img']='image.JPG'
    # print(request.FILES['img'])
    context={
    'form':form}
    # context={}

        
    if form.is_valid():
        print('in')
        form.save()
        return redirect('disp')
        # else:
            # print('invalid form')


    return render(request,'homepage/index.html',context)

def display_img(request):
    path='homepage/static/homepage/image/'
    filename=os.listdir(path)
    print(filename)
    os.rename(os.path.join(path,filename[0]),os.path.join(path,'image.jpg'))

    img=image.load_img(os.path.join(path,'image.jpg'),grayscale=True ,target_size=(180,180))
    x=image.img_to_array(img)
    x=x/255
    x=x.reshape(1,180,180,1)
    # with model_graph.as_default():
    #     tf_session=tf.compat.v1.keras.backend.get_session()
    #     with tf_session.as_default():
    print("this is x",x.shape)
    pred=model.predict(x)

    print(pred)
    if pred[0][0]<0.5:
        predictedlabel='Normal'
    else:
        predictedlabel='Pneumonia'
    # predictedlabel=labelInfo[str(np.argmax(pred[0]))]
    print(predictedlabel)
    context={
        'label':predictedlabel,
        'prob':pred[0][0],
    }
    return render(request,'homepage/display.html',context)