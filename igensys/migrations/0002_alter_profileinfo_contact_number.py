# Generated by Django 4.0.3 on 2022-07-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igensys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='Contact_number',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]