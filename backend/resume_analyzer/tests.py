from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Resume
from .ai import analyze_resume

class ResumeUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_resume(self):
        url = reverse('resume-upload')
        with open('test_resume.txt', 'rb') as resume_file:
            response = self.client.post(url, {'file': resume_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('content', response.data)
        self.assertIn('analysis_results', response.data)

    def test_analyze_resume(self):
        content = "Sample resume content"
        analysis_results = analyze_resume(content)
        self.assertIsInstance(analysis_results, dict)
