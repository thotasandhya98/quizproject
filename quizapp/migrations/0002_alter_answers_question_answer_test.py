# Generated by Django 4.0.6 on 2023-02-18 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quizapp.options'),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.options')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quizapp.questions')),
                ('show_answer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quizapp.answers')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.user')),
            ],
        ),
    ]
