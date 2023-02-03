from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(min_value=1)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=1)
