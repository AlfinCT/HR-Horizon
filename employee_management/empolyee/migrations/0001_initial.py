# Generated by Django 4.2.8 on 2024-06-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('post', models.CharField(max_length=250)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
