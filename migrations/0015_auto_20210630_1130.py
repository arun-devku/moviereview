# Generated by Django 3.1.5 on 2021-06-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0014_auto_20210630_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies2',
            name='releasedate',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
