# Generated by Django 4.1 on 2022-08-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_perfume_age_alter_perfume_flavor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='user',
        ),
        migrations.AlterField(
            model_name='perfume',
            name='age',
            field=models.CharField(choices=[('30', '30'), ('40', '40'), ('10', '10'), ('50 or more', '50 or more'), ('20', '20')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='flavor',
            field=models.CharField(choices=[('woody', 'woody'), ('floral', 'floral'), ('oriental', 'oriental'), ('fresh', 'fresh')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='gender',
            field=models.CharField(choices=[('woman', 'woman'), ('man', 'man')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='season',
            field=models.CharField(choices=[('spring', 'spring'), ('summer', 'summer'), ('winter', 'winter'), ('fall', 'fall')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='power',
            field=models.CharField(choices=[('bad', 'bad'), ('good', 'good'), ('moderate', 'moderate')], max_length=20, null=True),
        ),
    ]
