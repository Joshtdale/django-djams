# Generated by Django 4.1.3 on 2022-11-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djams', '0003_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
