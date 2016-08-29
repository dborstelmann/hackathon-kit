from django.contrib.auth.models import User
from django.db import models


class TestManager(models.Manager):

    def test(self, test):

        return {
            "test_name": test.name
        }


class Test(models.Model):
    '''
    Holds meta information about an Account, not used to login.
    '''
    objects = TestManager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63, blank=False)
