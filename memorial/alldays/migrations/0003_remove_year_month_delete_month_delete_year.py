# Generated by Django 5.0.1 on 2024-02-26 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alldays', '0002_month_authors_month_filename_alter_month_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='month',
        ),
        migrations.DeleteModel(
            name='Month',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
