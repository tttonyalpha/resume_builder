# Generated by Django 3.2.4 on 2022-12-08 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('surname', models.TextField(max_length=200)),
                ('email', models.TextField(max_length=100)),
                ('phone_number', models.TextField(max_length=15)),
                ('college', models.TextField(max_length=200)),
                ('pic', models.ImageField(upload_to='img/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]