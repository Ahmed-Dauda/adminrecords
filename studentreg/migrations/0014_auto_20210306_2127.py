# Generated by Django 3.1.6 on 2021-03-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentreg', '0013_hygiene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salat',
            name='salat',
            field=models.CharField(blank=True, choices=[('FAJR', 'FAJR'), ('ZUHR', 'ZUHR'), ('ASRI', 'ASRI'), ('MAGRIB', 'MAGRIB'), ('ISHA', 'ISHA'), ('TIMELY', 'TIMELY'), ('ORDERLINESS', 'ORDERLINESS'), ('CALMNESS', 'CALMNESS'), ('PARKING OFPLATES', 'MAGRIB'), ('ALLERGY', 'ALLERGY'), ('TIMELY', 'TIMELY'), ('OBEDIENT', 'OBEDIENT'), ('QUITNESSS', 'QUITNESS'), ('SWICH OF LIGHT', 'SWICH OF LIGHT'), ('TIME IN/OUT', 'TIME IN/OUT'), ('CALMNESS', 'CALMNESS'), ('READING/NOTE COPYING/ ASSIGN', 'READING/NOTE COPYING/ ASSIGN'), ('ATTENDANCE', 'ATTENDANCE')], max_length=255, null=True),
        ),
    ]