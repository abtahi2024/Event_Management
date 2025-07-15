from django.urls import path
from even import views

urlpatterns = [
    path('',views.home,name='dashboard'),

    path('eventcreate/',views.Create_new_Event,name='create_event'),
    path('update/<int:id>/',views.UpdateEvent,name='update_event'),
    path('delete/<int:id>/',views.DeleteEvent,name='delete_event'),
    path('detail/<int:id>/',views.Event_info,name='event_detail'),

    path('participants/',views.register_Participant,name='add_participant'),
    path('categories/',views.create_Category,name='add_category'),
    path('search/',views.search_event,name='search_event'),
]
