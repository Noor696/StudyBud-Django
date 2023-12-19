from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Developers'},
]

def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'home.html', {'rooms':rooms})

# {'rooms':rooms} pass a dictionary and specify the value name (key value pair) (address in the template : the value)

def room(request):
    return render(request, 'room.html')

