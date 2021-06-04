# Generated by Django 3.1.6 on 2021-03-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentreg', '0011_auto_20210305_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(blank=True, max_length=255, null=True)),
                ('lavel', models.CharField(blank=True, choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SS1', 'SS1'), ('SS2', 'SS2'), ('SS3', 'SS3')], max_length=255, null=True)),
                ('term', models.CharField(blank=True, choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('THIRD', 'THIRD')], max_length=255, null=True)),
                ('week', models.CharField(blank=True, choices=[('WEEK1', 'WEEK1'), ('WEEK2', 'WEEK2'), ('WEEK3', 'WEEK3')], max_length=255, null=True)),
                ('prep', models.CharField(blank=True, choices=[('TIME IN/OUT', 'TIME IN/OUT'), ('CALMNESS', 'CALMNESS'), ('READING/NOTE COPYING/ ASSIGN', 'READING/NOTE COPYING/ ASSIGN'), ('ATTENDANCE', 'ATTENDANCE')], max_length=255, null=True)),
                ('monday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('tuesday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('wednesday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('thursday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('friday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('saturday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sunday', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
