# Generated by Django 2.1.2 on 2018-11-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]
