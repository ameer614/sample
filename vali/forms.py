from .models import Productmodel
from django import forms
# class ProductCreateForm(forms.Form):
#     name = forms.CharField(max_length=60)
#     price=forms.IntegerField()
#     description=forms.CharField()

#     def clean_price(self):
#         price = self.cleaned_data['price']
#         if price<0:
#             raise forms.ValidationError("invalid input")
#         return price

class Mform(forms.ModelForm):

    class Meta:
        model=Productmodel
        fields=['name','price','description','category','image']

