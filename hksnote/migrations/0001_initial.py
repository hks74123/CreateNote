# Generated by Django 3.2.4 on 2021-06-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mynt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('Tag', models.CharField(max_length=500)),
                ('Note', models.TextField()),
            ],
        ),
    ]
