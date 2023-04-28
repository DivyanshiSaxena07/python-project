# Generated by Django 4.2 on 2023-04-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accountholders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=120)),
                ('fathername', models.CharField(max_length=120)),
                ('smdId', models.TextField(max_length=120)),
                ('pan', models.TextField(max_length=120)),
                ('date', models.DateField()),
                ('adhar', models.CharField(max_length=120)),
                ('nName', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('relation', models.CharField(max_length=120)),
                ('accNo', models.IntegerField()),
                ('ifsc', models.TextField(max_length=120)),
                ('hno', models.IntegerField()),
                ('address', models.CharField(max_length=120)),
                ('browser', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('landmark', models.CharField(max_length=120)),
            ],
        ),
    ]