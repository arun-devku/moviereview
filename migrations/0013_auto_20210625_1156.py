# Generated by Django 3.1.5 on 2021-06-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0012_auto_20210625_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies2',
            name='releasedate',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
