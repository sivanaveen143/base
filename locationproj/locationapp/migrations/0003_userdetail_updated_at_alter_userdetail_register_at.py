# Generated by Django 4.1.1 on 2022-10-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationapp', '0002_remove_userdetail_register_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='register_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
