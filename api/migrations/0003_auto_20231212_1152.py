# Generated by Django 3.2.8 on 2023-12-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231212_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='marks_obtained',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='maximum_marks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='minimum_marks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
