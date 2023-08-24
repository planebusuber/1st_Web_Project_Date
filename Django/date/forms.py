from .models import Comment, Review
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .widgets import starWidget


class CommentForm(forms.ModelForm):
    # 폼 이름은 CommentForm
    class Meta:
        # 모델은 Comment 모델을 사용
        model = Comment
        # 필드는 content 필드만 필요
        fields = ("content",)

class UserForm(UserCreationForm):
    # username , password 1 , password 2를 기본적으로 입력 받는다.
    # 추가적으로 email을 받을 것인데, 기본값은 아니기에 수동으로 잡아줘야함.
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

# Review 작성 폼
class ReviewWrite(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ "title",
                   "content",
                    "score",
                   ]
        # widgets = {
        #     'score': starWidget,
        # }

class Star(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ "score" ]
        widgets = {
            'score' : starWidget
        }
