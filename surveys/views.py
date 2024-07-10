from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from .models import Survey, Question, Choice, Answer
from .serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer

class SurveyListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of surveys or create a new survey.

    - GET: Returns a list of all surveys. Accessible to authenticated users.
    - POST: Creates a new survey. Accessible only to admin users.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        if Survey.objects.filter(title=serializer.validated_data['title']).exists():
            raise ValidationError({"detail": "A survey with this title already exists."})
        serializer.save()
    
class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a survey.

    - GET: Retrieves a specific survey by ID. Accessible to authenticated users.
    - PUT/PATCH: Updates a specific survey by ID. Accessible only to admin users.
    - DELETE: Deletes a specific survey by ID. Accessible only to admin users.
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
class QuestionListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of questions or create a new question.

    - GET: Returns a list of all questions. Accessible to everyone.
    - POST: Creates a new question. Accessible to authenticated users.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        text = serializer.validated_data.get('text')
        if text and Question.objects.filter(text=text).exists():
            raise ValidationError({"detail": "A question with this text already exists."})
        serializer.save()

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a question.

    - GET: Retrieves a specific question by ID. Accessible to everyone.
    - PUT/PATCH: Updates a specific question by ID. Accessible to authenticated users.
    - DELETE: Deletes a specific question by ID. Accessible to authenticated users.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class ChoiceListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve list of choices or create a new choice.

    - GET: Returns a list of all choices. Accessible to everyone.
    - POST: Creates a new choice. Accessible to authenticated users.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        text = serializer.validated_data.get('text')
        if text and Choice.objects.filter(text=text).exists():
            raise ValidationError({"detail": "A choice with this text already exists."})
        serializer.save()

class ChoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a choice.

    - GET: Retrieves a specific choice by ID. Accessible to everyone.
    - PUT/PATCH: Updates a specific choice by ID. Accessible to authenticated users.
    - DELETE: Deletes a specific choice by ID. Accessible to authenticated users.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class AnswerListCreateView(generics.ListCreateAPIView):
    """
    API view to create an anonymous answer to a question.

    - POST: Creates an anonymous answer to a question. Accessible to everyone.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class AnswerDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of an answer.
    
    - GET: Retrieves details of a specific answer by ID. Accessible to authenticated users.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
