# Generated by Django 2.2.19 on 2021-03-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelhub', '0003_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='adress',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
