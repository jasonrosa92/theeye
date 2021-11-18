# Generated by Django 3.2.9 on 2021-11-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('data', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('saved_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
