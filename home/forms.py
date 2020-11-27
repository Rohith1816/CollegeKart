from product.models import Product
from home.models import Contact
from django.forms import ModelForm

class sale(ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'created']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['slug']