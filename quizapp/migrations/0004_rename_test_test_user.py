# Generated by Django 4.0.6 on 2023-02-21 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_alter_answers_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='test',
            new_name='user',
        ),
    ]