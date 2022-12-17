from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView

from study_buddy.classroom.forms import AddEvent, AddLocation, EditEvent, DeleteEvent, JoinEventForm, DeleteJoinedEvent, \
    CommentsModelForm, DeleteCommentsForm
from study_buddy.classroom.models import Event, JoinedEvent, Comment, Location
from study_buddy.members.models import Profile


# Create your views here.#
def base(request):
    events_joined = JoinedEvent.objects.all()

    context = {
        'events_joined': events_joined,
    }
    return render(request, 'base.html', context)


class Index(TemplateView):
    template_name = 'index.html'


# def index(request):
#     return render(request, 'index.html')


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



class MyEvents(TemplateView):
    template_name = 'classroom/my_events.html'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        events_joined = JoinedEvent.objects.all()
        context['events_joined'] = events_joined
        return context


# def my_events(request):
#     events_joined = JoinedEvent.objects.all()
#
#     context = {
#         'events_joined': events_joined,
#     }
#     return render(request, 'classroom/my_events.html', context)


class JoinEvent(DetailView):
    template_name = 'classroom/join_event.html'
    model = JoinedEvent


# class DetailEventView(DetailView):
#     template_name = 'classroom/join_event.html'
#     model = JoinedEvent

def comment_view(request, pk):
    comment_model = Event.objects.filter(pk=pk).get()
    form = CommentsModelForm(request.POST)
    if form.is_valid():
        comment = form.save(
            commit=False
        )
        comment.event_c = comment_model
        comment.user_c = request.user
        comment.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'comments_model': comment_model,
    }
    return render(request, 'classroom/dashboard.html', context)


def delete_comment_view(request, pk):
    comment = Comment.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form_delete = DeleteCommentsForm(instance=comment)
    else:
        form_delete = DeleteCommentsForm(request.POST, instance=comment)
        if form_delete.is_valid():
            form_delete.save()
            return redirect('dashboard')

    context = {
        'form_delete': form_delete,
        'comment': comment,
    }
    return render(request, 'classroom/dashboard.html', context)


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


# Switched to a CBV
# def profile_details(request, pk):
#     profile = Profile.objects.filter(pk=pk).get()
#
#     context = {
#         'profile': profile,
#         'pk': pk,
#
#     }
#     return render(request, 'classroom/my_profile.html', context)

UserModel = get_user_model()
class ProfileDetails(DetailView):
    model = Profile
    template_name = 'classroom/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.request.user.id
        context['profile'] = Profile.objects.filter(pk=pk).get()
        return context


# def dashboard(request):
#     event_list = Event.objects.all()
#
#     context = {
#         'events': event_list,
#         'form': CommentsModelForm(),
#     }
#     return render(request, 'classroom/dashboard.html', context)


class Dashboard(TemplateView):
    template_name = 'classroom/dashboard.html'
    model = Event

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = CommentsModelForm()
        context['events'] = Event.objects.all()
        return context


def add_location(request):
    if request.method == 'GET':
        form = AddLocation()
    else:
        form = AddLocation(request.POST)
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

    return render(request, 'classroom/add_event.html', context, )


def event_details(request, pk):
    event = Event.objects.filter(pk=pk).get()

    context = {
        'event': event,
        'pk': pk,
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


