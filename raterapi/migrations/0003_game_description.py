# Generated by Django 3.1.3 on 2020-12-01 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterapi', '0002_review_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
