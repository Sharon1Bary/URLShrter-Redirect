from django.db import models

"""
    The DB table we used - URL.
"""


class URL(models.Model):
    url = models.CharField(max_length=255)
    url_data = models.JSONField(null=True)
