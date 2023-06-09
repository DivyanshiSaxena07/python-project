# Generated by Django 4.2 on 2023-04-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('msg', models.TextField(max_length=120)),
                ('subject', models.TextField(max_length=120)),
                ('date', models.DateField()),
            ],
        ),
    ]
