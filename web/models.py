from django.db import models


class Stack(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название стека технологий')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Стек технологий'
        verbose_name_plural = 'Стеки технологий'


class User(models.Model):
    tg_id = models.IntegerField(verbose_name='telegram id', primary_key=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    second_name = models.CharField(max_length=30, verbose_name='Фамилия пользователя')
    birthdate = models.DateField(verbose_name='Дата рождения пользователя')
    about_user = models.TextField(verbose_name='О пользователе')
    telegram_username = models.CharField(max_length=50, verbose_name='telegram', unique=True)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    stacks = models.ManyToManyField(Stack)

    def __str__(self):
        return f'{self.second_name} {self.first_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    hackathon_subscribe = models.BooleanField(verbose_name='Подписка на хакатоны', default=True)
    lecture_subscribe = models.BooleanField(verbose_name='Подписка на лекции', default=True)
    meet_up_subscribe = models.BooleanField(verbose_name='Подписка на meet ups', default=True)
    vacancy_subscribe = models.BooleanField(verbose_name='Подписка на вакансии', default=True)

    def __str__(self):
        return f'{self.user} {self.hackathon_subscribe} {self.lecture_subscribe} {self.meet_up_subscribe} {self.vacancy_subscribe}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class EventType(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тип мероприятия'
        verbose_name_plural = 'Типы мероприятий'


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    event_date = models.DateField(verbose_name='Дата проведения мероприятия')
    type_of_event = models.ForeignKey(EventType, on_delete=models.PROTECT, verbose_name='Тип мероприятия')
    post_about_event = models.TextField(verbose_name='Текст поста мероприятия')
    stacks = models.ManyToManyField(Stack)

    def __str__(self):
        return f'{self.title} {self.event_date}'


    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class UserStack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    stack = models.ForeignKey(Stack, on_delete=models.PROTECT, verbose_name='Стек технологий')
    stack = models.ManyToManyField(Stack, verbose_name='Стек технологий')

    def __str__(self):
        return f'#{self.user} {self.stack}'


class EventStack(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
    stack = models.ForeignKey(Stack, on_delete=models.PROTECT, verbose_name='Стек технологий')
    stack = models.ManyToManyField(Stack, verbose_name='Стек технологий')

    def __str__(self):
        return f'#{self.event} {self.stack}'
class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    event = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name='Мероприятие')

    def __str__(self):
        return f'{self.user} {self.event}'

    class Meta:
        verbose_name = 'Посетитель мероприятий'
        verbose_name_plural = 'Посетители мероприятий'




class Message(models.Model):
    profile = models.ForeignKey(
        to='web.User',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
