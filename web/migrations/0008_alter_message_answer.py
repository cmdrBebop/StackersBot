# Generated by Django 4.1.4 on 2022-12-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_text_message_quastion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='answer',
            field=models.TextField(null=True, verbose_name='Ответ'),
        ),
    ]