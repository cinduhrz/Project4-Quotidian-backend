# Generated by Django 4.1.7 on 2023-02-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]