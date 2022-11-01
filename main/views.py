from django.shortcuts import render
from .models import Room

# rooms = [{'id': 1, 'name': 3},
#          {'id': 2, 'name': 3},
#          {'id': 3, 'name': 3}
#          ]

def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'main/index.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'main/room.html', context)

def createroom(request):
    context = {}
    return render(request, 'main/room_form.html', context)