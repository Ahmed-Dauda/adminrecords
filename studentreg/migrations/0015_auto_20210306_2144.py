# Generated by Django 3.1.6 on 2021-03-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentreg', '0014_auto_20210306_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salat',
            name='salat',
        ),
        migrations.AddField(
            model_name='salat',
            name='attitudes',
            field=models.CharField(blank=True, choices=[('FAJR SALAT', 'FAJR SALAT'), ('ZUHR SALAT', 'ZUHR SALAT'), ('ASRI SALAT', 'ASRI SALAT'), ('MAGRIB SALAT', 'MAGRIB SALAT'), ('ISHA SALAT', 'ISHA SALAT'), ('TIMELY IN DINING', 'TIMELY IN DINING'), ('ORDERLINESS IN DINING', 'ORDERLINESS IN DINING'), ('CALMNESS IN DINING', 'CALMNESS IN DINING'), ('PARKING OF PLATES IN DINING', 'PARKING OF PLATES IN DINING'), ('ALLERGY IN DINING', 'ALLERGY IN DINING'), ('TIMELY TO LIGHTOUT', 'TIMELY TO LIGHTOUT'), ('OBEDIENT TO LIGHTOUT', 'OBEDIENT TO LIGHTOUT'), ('QUITNESSS TO LIGHTOUT', 'QUITNESS TO LIGHTOUT'), ('SWICH OF LIGHT TO LIGHTOUT', 'SWICH OF LIGHT TO LIGHTOUT'), ('ATTENDANCE TO PREP', 'ATTENDANCE TO PREP'), ('TIME IN/OUT TO PREP', 'TIME IN/OUT TO PREP'), ('CALMNESS TO PREP', 'CALMNESS TO PREP'), ('READING/NOTE COPYING/ ASSIGN TO PREP', 'READING/NOTE COPYING/ ASSIGN TO PREP')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dining',
            name='dining',
            field=models.CharField(blank=True, choices=[('TIMELY', 'TIMELY'), ('ORDERLINESS', 'ORDERLINESS'), ('CALMNESS', 'CALMNESS'), ('PARKING OF PLATES', 'MAGRIB'), ('ALLERGY', 'ALLERGY')], max_length=255, null=True),
        ),
    ]
