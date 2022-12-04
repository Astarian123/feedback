from django import forms
from .models import Review

'''class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=150, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name!"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=254)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)'''


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']         #'__all__' will target every field
        #exclude = ['']     # to exclude from fields ex. when __all__ is selected
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating'
        }
        error_messages = {
            "user_name":{
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name!"
            }
        }

