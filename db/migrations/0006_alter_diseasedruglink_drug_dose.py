# Generated by Django 4.2.1 on 2023-05-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_rename_cause_id_diseasecauselink_cause_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasedruglink',
            name='drug_dose',
            field=models.CharField(max_length=255),
        ),
    ]