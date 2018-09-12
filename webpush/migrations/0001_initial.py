# Generated by Django 2.1.1 on 2018-09-12 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('push_notifications', '0006_webpushdevice'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Title')),
                ('body', models.TextField(blank=True, default='', verbose_name='Body')),
                ('url', models.URLField(blank=True, default='', verbose_name='URL to open after a click/touch')),
                ('valid_from', models.DateTimeField(verbose_name='Validity start date and time')),
                ('valid_until', models.DateTimeField(null=True, verbose_name='Validity end date and time')),
                ('read', models.BooleanField(default=False, verbose_name='is Read')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='WebPushRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('NEW', 'Not-sent notification'), ('SENT', 'Sent notification'), ('ERR', 'Invalid notification')], default='NEW', max_length=4)),
                ('response', models.TextField(null=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpush.Notification')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='push_notifications.WebPushDevice')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='webpushrecord',
            unique_together={('subscription', 'notification')},
        ),
    ]
