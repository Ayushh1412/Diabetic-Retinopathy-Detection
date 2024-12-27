from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
from .models import User
from django.core.exceptions import ObjectDoesNotExist
# from keras.models import load_model 
# import cv2 
# from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img 
# import numpy as np # linear algebra 

# Create your views here.
def home(req):
    # img = load
    return render(req, 'home.html')

def index(req):
    # img = load
    return render(req, 'index.html')

def treatment(req):
    return render(req, 'treatment.html')

def about(req):
    return render(req, 'about.html')

def project(req):
    return render(req, 'project.html')

def login(req):
    return render(req, 'login.html')

def validate(req):
    email = req.POST["email"]
    password = req.POST["password"]
    try:
        v = User.objects.get(email = email,password = password)
        if v is not None:
            req.session['userid']= v.id
            return redirect(reverse('adminzone:admin_index'))
    except ObjectDoesNotExist or ValueError:
        pass
    return redirect('generalzone:index')
    
def createUser(req):
    email = req.POST["email"]
    name = req.POST["name"]
    password = req.POST["password"]
    contact = req.POST["contact"]
    File = req.FILES["image"]
    if User.objects.filter(email = email).exists():
        return render(req, 'index.html')
    image=File.name
    fs=FileSystemStorage()
    fs.save(image,File)
    c = User(name = name, contact = contact, email = email, password = password, image = image)
    c.save()
    return render(req, 'index.html')

def signup(req):
    return render(req, 'signup.html')
    