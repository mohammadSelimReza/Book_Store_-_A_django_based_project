from .models import BookReview
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['comment_body']
        widgets = {
            'comment_body': forms.Textarea(attrs={
                'class': 'w-full px-2 py-2 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400',
                'placeholder': 'Share your review here...',
                'rows': 4,
            }),
        }