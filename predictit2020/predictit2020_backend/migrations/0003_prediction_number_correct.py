# Generated by Django 3.0.8 on 2020-07-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictit2020_backend', '0002_auto_20200726_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='number_correct',
            field=models.IntegerField(default=0),
        ),
    ]