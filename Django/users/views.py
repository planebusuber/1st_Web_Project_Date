from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import UserForm


def signup(request): # signup 함수 선언
    if request.method == "POST": # 만약 request.method가 POST라면
        form = UserForm(request.POST) # UserForm은 사용자 정보를 입력받는 Form 클래스
        if form.is_valid(): # form의 유효성 검사(필수 데이터 입력과 형식이 올바른지)
            form.save() # 유효하다면 저장
            username = form.cleaned_data.get('username') #'username'을 form에서 가져와 username에 선언
            raw_password = form.cleaned_data.get('password1') #'password1'을 form에서 가져와 raw_password에 선언
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인 상태로 변경
            return redirect('/') # 127.0.0.1:8000/ 페이지로 이동
    else: # request.method가 POST가 아니라면
        form = UserForm() # 유효하지 않은 요청이라면 다시 사용자 정보를 입력하는 폼 생성
    return render(request, 'users/signup.html', {'form': form}) # 폼을 포함한 'users/signup.html'을 렌더링해서 보여줌.