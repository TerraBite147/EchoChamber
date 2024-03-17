from django import forms
from .models import Comment, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "comment-textarea rounded"}),
        }


from crispy_forms.layout import Field, Layout, Submit
from crispy_forms.bootstrap import PrependedText, FormActions


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "content", "excerpt", "status"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Title"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Content"}
        )
        self.fields["excerpt"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Excerpt"}
        )

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field("title", css_class="mb-3"),
            Field("category", css_class="mb-3"),
            Field("content", css_class="mb-3"),
            Field("excerpt", css_class="mb-3"),
            Field("status", css_class="mb-3"),
            FormActions(Submit("submit", "Submit", css_class="btn btn-primary")),
        )
