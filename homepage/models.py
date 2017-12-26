from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# what happened
def dish_img_path(instance, filename):
    """ retrieve the image of a dish from the restaurant it belongs to"""
    return 'img/{0}/{1}'.format(instance.owner.name, filename)

class Dish(models.Model):
    """
    Meta information about a dish.
    """
    image=models.ImageField(upload_to=dish_img_path)
    owner=models.ForeignKey('Restaurant', default=None, on_delete=models.CASCADE);
    name=models.CharField(max_length=100)
    desc=models.TextField(verbose_name='description', help_text='How does this dish taste?')
    def get_absolute_url(self):
        return reverse('dish-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class DishInstance(models.Model):
    """
    A dish instance
    """
    DISH_STATUS=(
            ('N', 'New dish'),
            ('S', 'Saling'),
            ('O', 'Out saled'),
        )
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    status=models.CharField(max_length=2, choices=DISH_STATUS)
    def __str__(self):
        return 'Instance of ' + self.dish.name

def restaurant_logo_path(instance, filename):
    """ retrieve the image of the logo of a restaurant """
    return 'img/{0}/{1}'.format(instance.name, filename)

class Restaurant(models.Model):
    """
    Meta information about a restaurant.
    """
    name=models.CharField(max_length=10)
    logo=models.ImageField(upload_to=restaurant_logo_path)
    desc=models.TextField(verbose_name='description', help_text='Restaurant description')
    def get_absolute_url(self):
        return reverse('restaurant-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

def validate_grade(grade):
    if (grade < 1 or grade > 5):
        raise ValidationError(_('%(grade) is not 1-5'), params={'grade':grade})

class ResInstance(models.Model):
    """
    A restaurant instance physically
    """
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    location=models.TextField(help_text='Where is this restaurant?')
    telephone=models.CharField(max_length=100, help_text='telephone number')
    grade=models.IntegerField(default=0, validators=[validate_grade])
    def __str__(self):
        return '{0} {1}'.format(self.location, self.restaurant.name)

