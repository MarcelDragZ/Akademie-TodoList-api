# Generated by Django 4.0.6 on 2024-02-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_todo_creatorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'Hoch'), ('medium', 'Mittel'), ('low', 'Niedrig')], default='medium', max_length=6),
        ),
    ]
