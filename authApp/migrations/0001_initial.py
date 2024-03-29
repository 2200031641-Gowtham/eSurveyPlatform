# Generated by Django 5.0.2 on 2024-03-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eZy_users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('age', models.IntegerField(max_length=2)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'eZy_users',
            },
        ),
    ]
