from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm): # UserCreationForm을 상속받는 UserForm 클래스 생성
    email = forms.EmailField(label="이메일") # 이메일 필드를 생성해서 메일 주소를 입력 받도록 함

    class Meta:
        model = User # User 모델과 연결
        fields = ("username", "password1", "password2", "email") # 폼에서 사용할 필드 구성