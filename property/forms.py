from django import forms
from .models import PropertyBook 
from django.utils import timezone

class PropertyBookForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkout_date'})) 

    class Meta:
        model = PropertyBook
        fields = ['date_from', 'date_to', 'guest', 'children']

    def __init__(self, *args, **kwargs):
        self.property = kwargs.pop('property', None)  
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date_from = cleaned_data.get("date_from")
        date_to = cleaned_data.get("date_to")

        if date_from and date_to:
            if date_from < timezone.now().date():
                raise forms.ValidationError("You can't book an earlier date ❌")

            if date_to < date_from:
                raise forms.ValidationError("Leaving date must be after arrival date ❌")

            if self.property: 
                reservations = PropertyBook.objects.filter(property=self.property)
                for book in reservations:
                    if (date_from <= book.date_to.date()) and (date_to >= book.date_from.date()):
                        raise forms.ValidationError(
                            f"This room is booked from {book.date_from.date()} to {book.date_to.date()}"
                        )
            else:
                raise forms.ValidationError("Property is required to check availability")

        return cleaned_data
    


