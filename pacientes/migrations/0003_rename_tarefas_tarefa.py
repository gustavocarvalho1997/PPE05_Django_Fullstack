# Generated by Django 5.1.6 on 2025-02-16 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_tarefas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]
