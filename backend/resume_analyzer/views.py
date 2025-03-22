from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Resume
from .ai import analyze_resume
from .serializers import ResumeSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ResumeUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        content = file.read().decode('utf-8')
        analysis_results = analyze_resume(content)
        resume = Resume.objects.create(content=content, analysis_results=analysis_results)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
