# Generated by Django 3.2.9 on 2021-11-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poco_user',
            name='profilepic',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
