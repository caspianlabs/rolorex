from django.db import models


class EarlyAccess(models.Model):
    """
    Model to keep track of users who requested early access.

    This will likely be removed once we move fully into production.
    """
    email_address = models.EmailField()
    sign_up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_address
