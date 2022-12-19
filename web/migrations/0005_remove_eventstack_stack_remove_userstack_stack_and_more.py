# Generated by Django 4.1.4 on 2022-12-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_subscribe_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventstack',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='userstack',
            name='stack',
        ),
        migrations.AddField(
            model_name='eventstack',
            name='stack',
            field=models.ManyToManyField(to='web.stack', verbose_name='Стек технологий'),
        ),
        migrations.AddField(
            model_name='userstack',
            name='stack',
            field=models.ManyToManyField(to='web.stack', verbose_name='Стек технологий'),
        ),
    ]
