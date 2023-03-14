from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user_name


class Questions(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    A = models.TextField()
    B = models.TextField()
    C = models.TextField()
    D = models.TextField()

    def __str__(self):
        return '{} {} {} {}'.format(self.A,self.B,self.C,self.D)


class Answers(models.Model):
    question_answer = models.OneToOneField(Options, on_delete=models.DO_NOTHING)
    answer = models.TextField()

    def __str__(self):
        return self.answer


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    options = models.ForeignKey(Options, on_delete=models.CASCADE)
    show_answer = models.ForeignKey(Answers, on_delete=models.DO_NOTHING)

# Create your models here.
