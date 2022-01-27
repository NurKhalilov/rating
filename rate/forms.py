from .models import Rating, Salesperson
from django import forms



class RateAddForm(forms.ModelForm):
    class Meta:
        model = Rating
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'rating'}),
            'salesperson': forms.Select(attrs={'placeholder': 'Choose the name of salesman'}),
        }
        fields = "__all__"

    def __init__(self, *args, region_id=None, **kwargs):
        super(RateAddForm, self).__init__(*args, **kwargs)
        self.fields['salesperson'].label = "Сотрудник: "
        self.fields['phone'].label = "Сотовый номер"
        self.fields['rating'].label = "Рейтинг: "
        if region_id:
            self.fields['salesperson'].queryset = Salesperson.objects.filter(region=region_id)
