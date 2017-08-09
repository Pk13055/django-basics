from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return timezone.now() - self.pub_date < datetime.timedelta(days = 3)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return "{ C: %s | V: %d }" % (self.choice_text, self.votes)