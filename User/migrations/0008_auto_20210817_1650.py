# Generated by Django 3.2.5 on 2021-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20210817_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
