# Generated by Django 4.2.1 on 2023-05-21 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_cause_name_eng_alter_diet_name_eng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasecauselink',
            old_name='cause_id',
            new_name='cause',
        ),
        migrations.RenameField(
            model_name='diseasecauselink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasedietlink',
            old_name='diet_id',
            new_name='diet',
        ),
        migrations.RenameField(
            model_name='diseasedietlink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasedruglink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasedruglink',
            old_name='drug_id',
            new_name='drug',
        ),
        migrations.RenameField(
            model_name='diseasepharmacotherapylink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasepharmacotherapylink',
            old_name='pharmaco_therapy_id',
            new_name='pharmaco_therapy',
        ),
        migrations.RenameField(
            model_name='diseasepreventionlink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasepreventionlink',
            old_name='prevention_id',
            new_name='prevention',
        ),
        migrations.RenameField(
            model_name='diseaseregimentaltherapylink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseaseregimentaltherapylink',
            old_name='regimental_therapy_id',
            new_name='regimental_therapy',
        ),
        migrations.RenameField(
            model_name='diseasesymptomlink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasesymptomlink',
            old_name='symptom_id',
            new_name='symptom',
        ),
        migrations.RenameField(
            model_name='diseasetreatmentprinciplelink',
            old_name='disease_id',
            new_name='disease',
        ),
        migrations.RenameField(
            model_name='diseasetreatmentprinciplelink',
            old_name='treatment_principle_id',
            new_name='treatment_principle',
        ),
        migrations.RenameField(
            model_name='drugpharmacotherapylink',
            old_name='drug_id',
            new_name='drug',
        ),
        migrations.RenameField(
            model_name='drugpharmacotherapylink',
            old_name='pharmaco_therapy_id',
            new_name='pharmaco_therapy',
        ),
        migrations.RenameField(
            model_name='symptomregimentaltherapylink',
            old_name='regimental_therapy_id',
            new_name='regimental_therapy',
        ),
        migrations.RenameField(
            model_name='symptomregimentaltherapylink',
            old_name='symptom_id',
            new_name='symptom',
        ),
    ]
