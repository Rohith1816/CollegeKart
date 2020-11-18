from product.models import Product
from django.forms import ModelForm

class sale(ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'created']