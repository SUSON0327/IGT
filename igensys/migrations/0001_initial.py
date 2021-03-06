# Generated by Django 4.0.3 on 2022-07-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(blank=True, max_length=100)),
                ('QuaPrice', models.CharField(blank=True, max_length=100)),
                ('Sizes', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TDate', models.CharField(blank=True, max_length=100)),
                ('DDate', models.CharField(blank=True, max_length=100)),
                ('Pay', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(blank=True, max_length=100)),
                ('Last_name', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=100)),
                ('Address', models.CharField(blank=True, max_length=250)),
                ('Contact_number', models.IntegerField()),
                ('Notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
