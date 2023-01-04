from django.db import models

# Create your models here.
# passing in argument inherits all the built-in base functionality from the model class
class Item(models.Model):
    # creating the traits of the class in making items for the todo app
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # do this so that we see item name instead of the item object
    def __str__(self):
        return self.name
