# Generated by Django 5.1.1 on 2024-09-28 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_paricipants_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
