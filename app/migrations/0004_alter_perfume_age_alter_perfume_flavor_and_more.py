# Generated by Django 4.1 on 2022-08-18 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_perfume_age_alter_perfume_flavor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='age',
            field=models.CharField(choices=[('30', '30'), ('40', '40'), ('10', '10'), ('20', '20'), ('50 or more', '50 or more')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='flavor',
            field=models.CharField(choices=[('floral', 'floral'), ('oriental', 'oriental'), ('woody', 'woody'), ('fresh', 'fresh')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='season',
            field=models.CharField(choices=[('winter', 'winter'), ('spring', 'spring'), ('fall', 'fall'), ('summer', 'summer')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='power',
            field=models.CharField(choices=[('good', 'good'), ('moderate', 'moderate'), ('bad', 'bad')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.postmodel')),
            ],
        ),
    ]