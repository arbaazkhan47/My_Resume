# Generated by Django 3.1.1 on 2020-11-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
