# Generated by Django 3.2.8 on 2022-01-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_journey_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='plate_number',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
