# Generated by Django 3.0.8 on 2020-08-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0002_auto_20200821_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
