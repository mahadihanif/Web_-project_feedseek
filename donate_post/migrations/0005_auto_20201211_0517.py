# Generated by Django 3.1.4 on 2020-12-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate_post', '0004_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]