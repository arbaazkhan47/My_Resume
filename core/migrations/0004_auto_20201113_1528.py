# Generated by Django 3.1.1 on 2020-11-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=300),
        ),
    ]
