# Generated by Django 5.0.1 on 2024-02-26 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alldays', '0003_remove_year_month_delete_month_delete_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
