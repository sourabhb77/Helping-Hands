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
    product_max_quantity = models.IntegerField(default= 1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    # product_Image = models.FileField(upload_to="documents/", validators=[validate_file_extension])

    Category = models.CharField(
        choices = requirementCategory.choices,
        default = 'Medicines',
         max_length=20
    )

    def __str__(self):
        return self.product_name

    



