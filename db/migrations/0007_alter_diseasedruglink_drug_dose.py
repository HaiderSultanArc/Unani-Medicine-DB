# Generated by Django 4.2.1 on 2023-05-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_diseasedruglink_drug_dose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasedruglink',
            name='drug_dose',
            field=models.CharField(max_length=255, null=True),
        ),
    ]