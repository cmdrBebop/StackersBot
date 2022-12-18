from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'tg_id',
            'first_name',
            'second_name',
            'birthdate',
            'telegram_username',
            'about_user',
            'rating',
            'stacks'
        )


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = (
            'user',
            'hackathon_subscribe',
            'lecture_subscribe',
            'meet_up_subscribe',
            'vacancy_subscribe',
        )


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = (
            'title',
        )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            'title',
            'event_date',
            'type_of_event',
            'post_about_event',
            'stacks'

        )


class UserEventForm(forms.ModelForm):
    class Meta:
        model = UserEvent
        fields = (
            'user',
            'event',
        )


class StackForm(forms.ModelForm):
    class Meta:
        model = Stack
        fields = (
            'id',
            'title',
        )
