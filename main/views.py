from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

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
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'main/room_form.html', context)