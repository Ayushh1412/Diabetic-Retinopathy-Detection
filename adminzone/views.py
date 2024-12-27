from django.shortcuts import render, redirect, reverse
from generalzone.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# from keras.layers import TFSMLayer
from keras.models import load_model

import cv2 
import tensorflow as tf
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img 
import numpy as np # linear algebra 
# Create your views here.
def index(req):
    try:
        img = load_img('./abc.jpg')
        img = img_to_array(img)
        img = cv2.resize(img, (128,128)) 
        img = np.array(img, dtype="float") / 255.0 
        img = np.expand_dims(img, axis = 0) 
        # pred = model.predict(img) 
        # y_pred= np.argmax(pred, axis = 1) 
        # print(y_pred[0]) 
        print(req.session['userid'])
        if req.session['userid']:
            return render(req,'admin_index.html')
    except KeyError:
        pass
    return redirect(reverse('generalzone:index'))

def about(req):
    try:
        print(req.session['userid'])
        if req.session['userid']:
            return render(req,'admin_about.html')
    except KeyError:
        pass
    return redirect(reverse('generalzone:index'))

def treatment(req):
    try:
        if req.session['userid']:
            return render(req,'admin_treatment.html')
    except KeyError:
        pass
    return redirect(reverse('generalzone:index'))

def project(req):
    try:
        if req.session['userid']:
            return render(req,'admin_project.html')
    except KeyError:
        pass
    return redirect(reverse('generalzone:index'))

def signout(req):
    try:
        if req.session['userid']:
            del req.session['userid']
    except KeyError:
        pass
    return redirect(reverse('generalzone:index'))

def int_to_classes(i):
    if i == 0: return "No Diabetic Retinopathy"
    elif i == 1: return "Mild Diabetic Retinopathy"
    elif i == 2: return "Moderate Diabetic Retinopathy"
    elif i == 3: return "Severe Diabetic Retinopathy"
    elif i == 4: return "Proliferative Diabetic Retinopathy"
    print("Invalid class ", i)
    return "Invalid Class"

def predict(req):
    File = req.FILES["image"]      
    image=File.name
    fs=FileSystemStorage()
    img = fs.save(image,File)
    img = load_img(img)
    img = img_to_array(img)
    img = cv2.resize(img, (600,600)) 
    img = np.array(img, dtype="float") / 255.0    
    img = np.expand_dims(img, axis = 0)    
    model = load_model("MY_MODEL/mymodel.keras") 
    # model = tf.saved_model.load("MY_MODEL/mymodel")
    pred = model.predict(img)     
    y_pred= np.argmax(pred, axis = 1)           
    print(y_pred[0]) 
    html = "<html><body>It is now Awsome</body></html>"
    return render(req, 'admin_predictOutput.html', {'output': int_to_classes(y_pred[0])})
