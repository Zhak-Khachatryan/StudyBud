# Generated by Django 5.1.1 on 2024-09-20 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_paricipants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='paricipants',
            new_name='participants',
        ),
    ]
