from .models import Comment, Review
from django import forms
from .widgets import starWidget

class CommentForm(forms.ModelForm):
    # 폼 이름은 CommentForm
    class Meta:
        # 모델은 Comment 모델을 사용
        model = Comment
        # 필드는 content 필드만 필요
        fields = ("content",)

# Review 작성 폼
class ReviewWrite(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ "title",
                   "content",
                   "score"
                   ]
        widgets = {
            'score': starWidget,
        }