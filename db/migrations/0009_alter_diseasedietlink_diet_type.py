# Generated by Django 4.2.1 on 2023-05-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_alter_cause_description_alter_diet_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasedietlink',
            name='diet_type',
            field=models.CharField(max_length=255),
        ),
    ]
