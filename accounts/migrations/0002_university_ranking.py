# Generated by Django 4.2.10 on 2024-12-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='ranking',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]