from django.db import models

class Resume(models.Model):
    content = models.TextField()
    analysis_results = models.JSONField()

    def __str__(self):
        return f"Resume {self.id}"
