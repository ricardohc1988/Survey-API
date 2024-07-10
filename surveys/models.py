from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"
        ordering = ['title']

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['text']

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
        ordering = ['text']

    def __str__(self):
        return self.text

class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['-created_at']

    def __str__(self):
        return str(self.choice)