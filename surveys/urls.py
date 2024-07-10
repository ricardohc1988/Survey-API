from django.urls import path
from .views import SurveyListCreateView, SurveyDetailView, QuestionListCreateView, QuestionDetailView, ChoiceListCreateView, ChoiceDetailView, AnswerListCreateView, AnswerDetailView

urlpatterns = [
    path('surveys/', SurveyListCreateView.as_view(), name='survey-list-create'),
    path('surveys/<int:pk>/', SurveyDetailView.as_view(), name='survey-detail'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('choices/', ChoiceListCreateView.as_view(), name='choice-list-create'),
    path('choices/<int:pk>/', ChoiceDetailView.as_view(), name='choice-detail'),
    path('answers/', AnswerListCreateView.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
]