# Generated by Django 4.0.5 on 2022-06-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrekModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('days', models.CharField(max_length=200)),
                ('start_destination', models.CharField(max_length=200)),
                ('end_destination', models.CharField(max_length=200)),
            ],
        ),
    ]
