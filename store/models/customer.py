from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone     = models.CharField(max_length=12)
    email     = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customers.objects.get(email=email)
        except:
            return False



    def isExistsEmail(self):
        if Customers.objects.filter(email = self.email):
            return True
        return False
    def isExistPhone(self):
        if Customers.objects.filter(phone = self.phone):
            return True
        return False


