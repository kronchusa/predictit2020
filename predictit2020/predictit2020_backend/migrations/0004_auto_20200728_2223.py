# Generated by Django 3.0.8 on 2020-07-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictit2020_backend', '0003_prediction_number_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeclareWinners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='prediction',
            name='number_correct',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
