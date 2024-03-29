# Generated by Django 4.2.1 on 2024-01-16 00:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0004_remove_bucket_events'),
        ('events', '0004_alter_event_buckets_alter_event_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='buckets',
        ),
        migrations.AddField(
            model_name='event',
            name='bucket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bucket', to='buckets.bucket'),
        ),
        migrations.AlterField(
            model_name='event',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('43086df6-78f9-4ccd-91b6-d424f0d267f6'), editable=False, unique=True),
        ),
    ]
