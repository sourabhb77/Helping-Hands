from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import validate_file_extension


class requirementModel(models.Model):
    class requirementCategory(models.TextChoices):
        Medicines = 'Medicines'
        Ventilators = 'Ventilators'
        Beds = 'Beds'
        Other = 'Other'

    posted_at = models.DateTimeField(default = timezone.now)
    product_name = models.CharField(max_length = 20)
    product_description = models.TextField()
    admin = models.ForeignKey(User , on_delete=models.CASCADE)
    # x=User.objects.get(username=admin).first_name
    ngo_name = models.CharField(max_length = 20,default="fehjrj",editable=False)
    product_max_quantity = models.IntegerField(default= 1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    # product_Image = models.FileField(upload_to="documents/", validators=[validate_file_extension])

    category = models.CharField(
        choices = requirementCategory.choices,
        default = 'Medicines',
         max_length=20
    )

    def __str__(self):
        return self.product_name


###### not yet completed
class DonationModel(models.Model):
    doner_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id  = models.ForeignKey(requirementModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    quantity_donated = models.CharField(max_length=20)
    donated_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.donation_name

# class Donation(models.Model):
#     doner_email=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     donation_type=models.CharField(max_length=20)
#     donation_name=models.CharField(max_length=20)
#     donation_quantity=models.CharField(max_length=20)
#     donation_date=models.DateTimeField(default = timezone.now)

#     def __str__(self):
#         return self.donation_name