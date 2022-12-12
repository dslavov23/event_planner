from django.shortcuts import render, redirect

from study_buddy.classroom.forms import AddEvent, EditEvent, DeleteEvent
from study_buddy.classroom.models import Event


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    event_list = Event.objects.all()

    context = {
        'events': event_list,
    }
    return render(request, 'classroom/dashboard.html', context)


def homework(request):
    return render(request, 'classroom/homework.html')


def event_add(request):
    if request.method == 'GET':
        form = AddEvent()
    else:
        form = AddEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'classroom/add_event.html', context)


def event_details(request, pk):
    event = Event.objects.filter(pk=pk).get()

    context = {
        'event': event,
    }
    return render(request, 'classroom/event_details.html', context)


def event_edit(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = EditEvent(instance=event)
    else:
        form = EditEvent(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'classroom/event_edit.html', context)


def event_delete(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DeleteEvent(instance=event)
    else:
        form = DeleteEvent(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'classroom/event_delete.html', context)
