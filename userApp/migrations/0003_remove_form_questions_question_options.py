# Generated by Django 5.0.1 on 2024-03-09 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_form_questions_form_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_questions',
            name='question_options',
        ),
    ]