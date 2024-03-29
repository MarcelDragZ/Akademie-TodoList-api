# Generated by Django 4.0.6 on 2024-02-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('progress', 'progress'), ('closed', 'closed')], default='open', max_length=15),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='medium', max_length=15),
        ),
    ]
