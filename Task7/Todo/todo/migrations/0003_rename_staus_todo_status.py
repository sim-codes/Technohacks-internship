# Generated by Django 4.2.6 on 2023-10-20 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_done_todo_staus_todo_created_todo_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='staus',
            new_name='status',
        ),
    ]
