# Generated by Django 4.0.6 on 2024-02-12 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0006_remove_task_creatorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creatorId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]