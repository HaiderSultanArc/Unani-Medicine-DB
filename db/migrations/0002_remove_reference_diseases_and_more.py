# Generated by Django 4.2.1 on 2023-05-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial_manual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='diseases',
        ),
        migrations.RenameField(
            model_name='diseasecauselink',
            old_name='causes',
            new_name='cause_id',
        ),
        migrations.AlterField(
            model_name='cause',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name_eng',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacotherapy',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='prevention',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='regimentaltherapy',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='icd_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='treatmentprinciple',
            name='name_persian',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='DiseaseReferenceLink',
        ),
        migrations.DeleteModel(
            name='Reference',
        ),
    ]
