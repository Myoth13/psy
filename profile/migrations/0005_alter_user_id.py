# Generated by Django 3.2.16 on 2022-11-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20221108_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
