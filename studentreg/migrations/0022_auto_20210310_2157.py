# Generated by Django 3.1.6 on 2021-03-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentreg', '0021_auto_20210310_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salat',
            name='friday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='monday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='saturday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='sunday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='thursday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='tuesday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='salat',
            name='wednesday',
            field=models.PositiveIntegerField(blank=True, default=100, null=True),
        ),
    ]
