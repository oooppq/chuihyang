# Generated by Django 4.0.6 on 2022-07-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='country',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
