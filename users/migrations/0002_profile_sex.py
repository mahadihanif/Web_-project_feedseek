# Generated by Django 3.1.4 on 2020-12-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], default='U', max_length=1),
            preserve_default=False,
        ),
    ]
