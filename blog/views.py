from django.shortcuts import render,redirect
import pyrebase
from collections import OrderedDict
# Create your views here.
config = {
  "apiKey": "AIzaSyC3PhwaLlFJsjijz9AybYFHPiTm_YJnNGg",
  "authDomain": "percobaan-e53e5.firebaseapp.com",
  "databaseURL": "https://percobaan-e53e5.firebaseio.com",
  "projectId": "percobaan-e53e5",
  "storageBucket": "percobaan-e53e5.appspot.com",
  "messagingSenderId": "1053555899978",
  "appId": "1:1053555899978:web:3c0971388e04ae71a530b3",
  "measurementId": "G-NERTFG6RPW"
};
firebase = pyrebase.initialize_app(config)
db = firebase.database()
def home(request):
	getdata = db.child("dball").child("fruitsall").get()
	odict = OrderedDict(getdata.val())
	return render(request,"main.html",{"data":odict.values()})

def add(request):
	if request.method == "POST":
		fruits = request.POST['fruits']
		result = db.child("dball").child("fruitsall").push({"name":fruits})
		return redirect("/blog/")


