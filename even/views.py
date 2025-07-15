from django.shortcuts import render,redirect,get_object_or_404
from even.forms import CatagoryForm
from django.http import HttpResponse
from datetime import date
from django.contrib import messages
from even.models import Event,Category,Participant
from even.forms import EventForm,ParticipantForm,CatagoryForm
from django.db.models import Q
# Create your views here.


def home(request):
    type=request.GET.get('type')
    today=date.today()
    events=Event.objects.select_related('category').prefetch_related('participant').all()
    context={
        'events':events,
        'total_events':events.count(),
        'total_participants':Participant.objects.count(),
        'total_categories':Category.objects.count(),
        'upcoming_events':events.filter(date__gt=today).count(),
        'past_events':events.count(),
        'todays_events':events.filter(date=today),
    }
    return render(request,"event.html",context)
def Create_new_Event(request):
    form = EventForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Created Successfully")
        return redirect('dashboard')
    return render(request, 'eventform.html', {'form': form})

def UpdateEvent(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Event Updated Successfully")
        return redirect('dashboard')
    return render(request, 'eventform.html', {'form': form})

def DeleteEvent(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('dashboard')
    return render(request, 'eventform.html', {'event': event})

def Event_info(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'eventdetail.html', {'event': event})

def register_Participant(request):
    form = ParticipantForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Participant Added Successfully")
        return redirect('dashboard')
    return render(request, 'participantform.html', {'form': form})

def create_Category(request):
    form = CatagoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Category Added Successfully")
        return redirect('dashboard')
    return render(request, 'categoryform.html', {'form': form})

def search_event(request):
    query=request.GET.get('search')
    if query:
        events=Event.objects.filter(Q(name__icontains=query) | Q(location__icontains=query))
    else:
        events=Event.objects.all()
    
    context={
        'events':events,
        'total_events':events.count(),
        'total_participants':Participant.objects.count(),
        'total_categories':Category.objects.count(),
        'upcoming_events':events.filter(date__gt=date.today()).count(),
        'past_events':events.count(),
        'todays_events':events.filter(date=date.today()),
    }
    return render(request,'event.html',context)
