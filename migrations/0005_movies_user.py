# Generated by Django 3.1.5 on 2021-06-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviereviews', '0004_movies2'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='moviereviews.logindetails'),
            preserve_default=False,
        ),
    ]
