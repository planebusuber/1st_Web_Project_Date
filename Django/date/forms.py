from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    # 폼 이름은 CommentForm
    class Meta:
        # 모델은 Comment 모델을 사용
        model = Comment
        # 필드는 content 필드만 필요
        fields = ("content",)