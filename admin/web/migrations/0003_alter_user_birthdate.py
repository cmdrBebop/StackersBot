# Generated by Django 4.1.4 on 2022-12-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_event_eventstack_eventtype_message_stack_subscribe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(verbose_name='Дата рождения пользователя'),
        ),
    ]
