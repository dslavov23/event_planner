from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from study_buddy.classroom.forms import AddEvent, AddSchool, EditEvent, DeleteEvent, JoinEventForm, DeleteJoinedEvent, \
    CommentsModelForm
from study_buddy.classroom.models import Event, JoinedEvent, Comment
from study_buddy.members.models import Profile


# Create your views here.#
def base(request):
    events_joined = JoinedEvent.objects.all()

    context = {
        'events_joined': events_joined,
    }
    return render(request, 'base.html', context)


def index(request):
    return render(request, 'index.html')


def search_event(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(name__icontains=searched)

        context = {
            'searched': searched,
            'events': events,
        }

        return render(request, 'classroom/search_event.html', context)
    else:
        return render(request, 'classroom/search_event.html')

def my_events(request):
    events_joined = JoinedEvent.objects.all()

    context = {
        'events_joined': events_joined,
    }
    return render(request, 'classroom/my events.html', context)


class JoinEvent(DetailView):
    template_name = 'classroom/join_event.html'
    model = JoinedEvent


# class DetailEventView(DetailView):
#     template_name = 'classroom/join_event.html'
#     model = JoinedEvent

def comment_view(request,pk):
    comment_model = Event.objects.filter(id=pk).get()
    form=CommentsModelForm(request.POST)
    if form.is_valid():
        comment = form.save(
            commit=False
        )
        comment.event_c = comment_model
        comment.user_c = request.user
        comment.save()
        return redirect('dashboard')

    context={
        'form': form,
    }
    return render(request,'classroom/event_details.html',context)

def join_event(request, pk):
    event = Event.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = JoinEventForm(initial={'student': request.user,
                                      'event': pk})
    else:
        form = JoinEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my events')

    context = {
        'form': form,
        'event': event,
        'pk': pk,
    }

    return render(request, 'classroom/join_event.html', context)


def delete_joined_event(request, pk):
    event = JoinedEvent.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteJoinedEvent(instance=event)
    else:
        form = DeleteJoinedEvent(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'classroom/delete_joined_event.html', context)


def profile_details(request, pk):
    profile = Profile.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
    }
    return render(request, 'classroom/my_profile.html', context)


def dashboard(request):
    event_list = Event.objects.all()

    context = {
        'events': event_list,
        'form': CommentsModelForm(),
    }
    return render(request, 'classroom/dashboard.html', context)


def homework(request):
    return render(request, 'classroom/homework.html')


def add_school(request):
    if request.method == 'GET':
        form = AddSchool()
    else:
        form = AddSchool(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add event')

    context = {
        'form': form,
    }

    return render(request, 'classroom/add_school.html', context)


def event_add(request):
    if request.method == 'GET':
        form = AddEvent()
    else:
        form = AddEvent(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request,'classroom/add_event.html',context,)


def event_details(request, pk):
    event = Event.objects.filter(pk=pk).get()
    form = CommentsModelForm()


    context = {
        'event': event,
        'pk': pk,
        'form':form,
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
