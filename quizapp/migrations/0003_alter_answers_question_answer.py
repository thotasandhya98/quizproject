# Generated by Django 4.0.6 on 2023-02-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_alter_answers_question_answer_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question_answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='quizapp.options'),
        ),
    ]
