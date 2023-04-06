# Generated by Django 4.1.7 on 2023-04-06 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=10)),
                ('pet_name', models.CharField(max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('owners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('statuses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.status')),
            ],
        ),
    ]
