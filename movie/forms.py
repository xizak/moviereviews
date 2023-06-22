from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm, Textarea
from django.forms.utils import ErrorList
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["watchAgain"].widget.attrs.update({"class": "form-check-input"})

    class Meta:
        model = Review
        fields = ["text", "watchAgain"]
        labels = {
            "watchAgain": "Watch Again",
        }
        widgets = {
            "text": Textarea(attrs={"rows": 4}),
        }
