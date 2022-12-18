from django.contrib import admin

from .forms import *
from .models import *



@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'first_name', 'second_name')
    form = UserForm


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    form = SubscribeForm

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = EventTypeForm

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'type_of_event', 'post_about_event')
    form = EventForm

@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    form = UserEventForm

@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = StackForm


@admin.register(UserStack)
class UserStackAdmin(admin.ModelAdmin):
    list_display = ('user',)
    form = UserStackForm

@admin.register(EventStack)
class EventStackAdmin(admin.ModelAdmin):
    list_display = ('event',)
    list_filter = ('stack',)
    form = EventStackForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')

