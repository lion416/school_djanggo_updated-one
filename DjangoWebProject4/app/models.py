"""
Definition of models.
"""

from django.db import models
class AccountInfo(models.Model):
    student_name = models.CharField(max_length=200)
    student_password = models.CharField(max_length=200)

    def _str_(self):
        return self.student_name
