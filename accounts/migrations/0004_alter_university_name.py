# Generated by Django 4.2.10 on 2024-12-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_established_on_university_established_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
