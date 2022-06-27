from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Booking
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
import razorpay
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.http import HttpResponse
# Create your views here.
#password for user shreya is Shreya***000
#password for user sreetama sree@135
def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #print('Username taken')
                messages.success(request,'Username already taken')
            elif User.objects.filter(email=email).exists():
                #print('Email taken')
                messages.success(request,'Email already taken')
            else:
                user = User.objects.create_user(email=email,username=username,password=password1)
                user.save()
                #print("User created succesfully")
                messages.success(request,'User created succesfully')
        else:
            #print("Password not matching")
            messages.success(request,'Password not matching')
        return redirect("/login")
    return render (request,"register.html")
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request,'index.html')
def loginUser(request):
    if request.method == "POST":
        #check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request,'Incorrect username or password')
            return render (request,'login.html')
    return render(request,"login.html")
def logoutUser(request):
    logout(request)
    return redirect('/login')
def rent(request):
    if request.method == "POST":
        user_name =  request.user.username
        location = request.POST['location']
        pickup_date = request.POST['pick_up_date']
        return_date = request.POST['return_date']
        car = request.POST['cars']
        if(car=="Sedan" or car=="SUV"):
            cost = 1000
        elif(car=="Convertible"):
            cost = 1200
        elif(car=="Van"):
            cost = 800
        elif(car=="Mini-Van"):
            cost = 900
        elif(car=="CUV"):
            cost=1100
        book = Booking(user_name=user_name,location=location,pickup_date=pickup_date,return_date=return_date,car=car,cost=cost)
        book.save()
        request.session['booking_no'] = book.booking_no
        return redirect('/payment')
    return render(request,'rent.html')

def payment(request):
        '''client = razorpay.Client(auth=('rzp_test_lcA0SqSr4HzVQO', '5DcT4ODHfFpauyvqa9WSrNCC'))
        payment_order = client.order.create(dict(amount= 500,currency= "INR",payment_capture=1))
        payment_order_id = payment_order['id']
        context={
            'amount':500,'api_key':'rzp_test_lcA0SqSr4HzVQO','order_id': payment_order_id
        }'''
        print(request.session.get('booking_no'))
        #user_name = request.user.username
        #if Booking.objects.filter(user_name=user_name).exists():
        book = Booking.objects.filter(booking_no=request.session.get('booking_no')).last()
        d1 = book.pickup_date
        d2 = book.return_date
        diff = d2-d1
        print(diff.days)
        amount = (book.cost)*(diff.days)
        print(amount)
        book.total_amount = amount
        book.save()
        print(book.total_amount)
        context = {
                'amount' : amount
        }
        return render(request,'payment.html',context)

@csrf_exempt
def success(request):
    return render(request,"success.html")
    
#AUGjJ6ON9tjOvsfQSV4oNSBrdZluEWWM2dc_bTO0IlB_lPTw7kYfQ00Jh3DqjjVp1KCs79bD-4M_9s4d
def cancel(request):
    book = Booking.objects.filter(booking_no=request.session.get('booking_no')).last()
    book.delete()
    book = None
    return redirect('/rent')

def booking_list(request):
    book = Booking.objects.filter(user_name=request.user.username)
    context={
        'booking_list' : book
    }
    return render(request,'booking_list.html',context)

def cancel_order(request):
    booking_id = request.GET['booking_id']
    book = Booking.objects.filter(booking_no = booking_id).last()
    print(book.user_name)
    d1 = book.pickup_date
    today = date.today()
    if(today>d1):
        return HttpResponse('Cannot cancel now. Too late!')
    else:
        book.delete()
        book = None
        return redirect('/rent')

#<a href = "{% url '/cancel_order' booking_id = booking.booking_no %}">Cancel Order</a>
#<a href = "{% url 'cancel_order' %}?booking_id={{booking.booking_no}}">Cancel Order</a>