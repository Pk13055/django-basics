from django.test import TestCase
from .models import Question, Choice
from datetime import datetime
from django.utils import timezone
import datetime
# Create your tests here.


class QuestionModelTests(TestCase):
	
	def test_published_recently_with_future_result(self):
		"""
			This test exporses the bug that questions created with
			a future date are also marked as somthing published recently

		"""
		time = timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)
		self.assertIs(future_question.was_published_recently(), False)
