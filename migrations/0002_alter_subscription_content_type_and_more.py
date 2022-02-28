# Generated by Django 4.0.2 on 2022-02-27 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscribed', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]