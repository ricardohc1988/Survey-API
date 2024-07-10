from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Survey, Question, Choice, Answer

class SurveyTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.normal_user = User.objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )
        self.survey_data = {'title': 'Test Survey', 'description': 'This is a test survey.'}
        self.url = reverse('survey-list-create')

    def test_create_survey(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.url, self.survey_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Survey.objects.get().title, 'Test Survey')

    def test_create_survey_non_admin(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(self.url, self.survey_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_survey_list(self):
        Survey.objects.create(**self.survey_data)
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_survey_detail(self):
        survey = Survey.objects.create(**self.survey_data)
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(reverse('survey-detail', kwargs={'pk': survey.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Survey')

class QuestionTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.normal_user = User.objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )
        self.survey = Survey.objects.create(title='Test Survey', description='This is a test survey.')
        self.question_data = {'survey': self.survey.id, 'text': 'Test Question'}

    def test_create_question(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('question-list-create'), self.question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().text, 'Test Question')

    def test_create_duplicate_question(self):
        self.client.force_authenticate(user=self.admin_user)
        Question.objects.create(survey=self.survey, text='Test Question')
        response = self.client.post(reverse('question-list-create'), self.question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_question_list(self):
        Question.objects.create(survey=self.survey, text='Test Question')
        response = self.client.get(reverse('question-list-create'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_question_detail(self):
        self.client.force_authenticate(user=self.admin_user)
        question = Question.objects.create(survey=self.survey, text='Test Question')
        response = self.client.get(reverse('question-detail', kwargs={'pk': question.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Test Question')

class ChoiceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.normal_user = User.objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )
        self.survey = Survey.objects.create(title='Test Survey', description='This is a test survey.')
        self.question = Question.objects.create(survey=self.survey, text='Test Question')
        self.choice_data = {'question': self.question.id, 'text': 'Test Choice'}

    def test_create_choice(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('choice-list-create'), self.choice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Choice.objects.count(), 1)
        self.assertEqual(Choice.objects.get().text, 'Test Choice')

    def test_create_duplicate_choice(self):
        self.client.force_authenticate(user=self.admin_user)
        Choice.objects.create(question=self.question, text='Test Choice')
        response = self.client.post(reverse('choice-list-create'), self.choice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_choice_list(self):
        Choice.objects.create(question=self.question, text='Test Choice')
        response = self.client.get(reverse('choice-list-create'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_choice_detail(self):
        choice = Choice.objects.create(question=self.question, text='Test Choice')
        response = self.client.get(reverse('choice-detail', kwargs={'pk': choice.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'Test Choice')

class AnswerTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )
        self.normal_user = User.objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )
        self.survey = Survey.objects.create(title='Test Survey', description='This is a test survey.')
        self.question = Question.objects.create(survey=self.survey, text='Test Question')
        self.choice = Choice.objects.create(question=self.question, text='Test Choice')
        self.answer = Answer.objects.create(choice=self.choice)
        self.answer_data = {'choice': self.choice.id}

    def test_create_answer_authenticated(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(reverse('answer-list-create'), self.answer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 2)

    def test_create_answer_unauthenticated(self):
        response = self.client.post(reverse('answer-list-create'), self.answer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 2)

    def test_get_answer_list_authenticated(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(reverse('answer-list-create'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_answer_list_unauthenticated(self):
        response = self.client.get(reverse('answer-list-create'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_answer_detail_authenticated(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(reverse('answer-detail', kwargs={'pk': self.answer.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['choice'], self.choice.id)

    def test_get_answer_detail_unauthenticated(self):
        response = self.client.get(reverse('answer-detail', kwargs={'pk': self.answer.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)