from django.db import models
from django.contrib.auth.models import User
from datetime import date

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)  # วันเกิด
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    bmr = models.FloatField(null=True, blank=True)
    tdee = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    # ฟังก์ชันคำนวณอายุ
    @property
    def age(self):
        today = date.today()
        if self.date_of_birth:
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None
