# Generated by Django 4.0.6 on 2022-08-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_perfume_age_alter_perfume_flavor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='age',
            field=models.CharField(choices=[('30', '30'), ('10', '10'), ('20', '20'), ('40', '40'), ('50 or more', '50 or more')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='season',
            field=models.CharField(choices=[('spring', 'spring'), ('summer', 'summer'), ('fall', 'fall'), ('winter', 'winter')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='power',
            field=models.CharField(choices=[('moderate', 'moderate'), ('good', 'good'), ('bad', 'bad')], max_length=20, null=True),
        ),
    ]
