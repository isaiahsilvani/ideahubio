# Generated by Django 3.2.2 on 2021-05-12 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20210512_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
    ]