# Generated by Django 5.1.1 on 2024-09-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_companydata_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydata',
            name='country',
        ),
        migrations.RemoveField(
            model_name='companydata',
            name='curr_emp_estimate',
        ),
        migrations.RemoveField(
            model_name='companydata',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='companydata',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='companydata',
            name='size_range',
        ),
        migrations.RemoveField(
            model_name='companydata',
            name='total_emp_estimate',
        ),
    ]
