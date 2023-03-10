from django.contrib import admin, messages
from django_admin_filters import MultiChoice

# from .mailing import publish
from .forms import *
from .models import *
from mailing import publish


class StatusFilter(MultiChoice):
    FILTER_LABEL = "По стеку"
    BUTTON_LABEL = "Применить"


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'first_name', 'second_name', 'telegram_username', 'rating')
    list_display_links = ('tg_id', 'first_name', 'second_name')
    search_fields = ('tg_id', 'first_name', 'second_name', 'telegram_username')
    form = UserForm
    filter_horizontal = ['stacks']
    list_filter = ['stacks']


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    list_display_links = ('user', 'hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    list_filter = ('hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    form = SubscribeForm
    search_fields = ['user__stacks__title']


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    form = EventTypeForm


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'type_of_event', 'post_about_event')
    list_display_links = ('id', 'title', 'event_date', 'type_of_event', 'post_about_event')
    list_filter = ('event_date', 'type_of_event')
    search_fields = ('title', 'post_about_event', 'stacks__title')
    form = EventForm
    filter_horizontal = ['stacks']
    actions = ['mailing']
    date_hierarchy = 'event_date'

    @admin.action(description='Рассылка')
    def mailing(self, request, queryset):
        publish(queryset.values()[0])
        messages.add_message(request, messages.SUCCESS, f"Рассылка на {queryset.values()[0]['title']} отпрвлена")


@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_display_links = ('user', 'event')
    search_fields = ['event__title', 'user__first_name', 'user__second_name', 'user__telegram_username']
    form = UserEventForm
    list_filter = ['event__title']



@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    form = StackForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'quastion', 'answer')
    list_display_links = ('id', 'profile', 'quastion', 'answer')

