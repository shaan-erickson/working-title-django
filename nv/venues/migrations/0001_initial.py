# Generated by Django 4.0.3 on 2022-04-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=255)),
                ('venue_manager', models.CharField(max_length=255)),
            ],
        ),
    ]
