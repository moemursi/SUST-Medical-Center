# Generated by Django 2.2 on 2019-05-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0009_auto_20190502_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='designation',
            field=models.CharField(default=None, max_length=90),
        ),
    ]
