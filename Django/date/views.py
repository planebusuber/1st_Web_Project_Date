from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, CreateView
from django.db import models
from date.models import Cafe, Rest, Place, Review,Addr
from .forms import ReviewWrite
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import random

class MainPage(ListView):
    model = Cafe
    template_name = "date/main_area.html"

    def get_context_data(self, **kwargs):
        context =super().get_context_data()

        context["addr_names"] = Addr.objects.all()

        cafe_max = Cafe.objects.all().count()
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_1"] = Cafe.objects.all()[cafe_ran]
        cafe_ran = random.randint(0, cafe_max-1)
        context["cafe_recommed_2"] = Cafe.objects.all()[cafe_ran]
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_3"] = Cafe.objects.all()[cafe_ran]



        rest_max = Rest.objects.all().count()
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_1"] = Rest.objects.all()[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_2"] = Rest.objects.all()[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_3"] = Rest.objects.all()[rest_ran]

        place_max = Place.objects.all().count()
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_1"] = Place.objects.all()[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_2"] = Place.objects.all()[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_3"] = Place.objects.all()[place_ran]

        return context


class ReviewList(ListView):
    model = Review
    paginate_by = 5
    template_name = "date/review_list.html"


    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
                                  # on_delete = models.CASCADE : 게시글의 작성자가 삭제되었을때 같이 삭제한다


def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):  #현재 유저가 로그인이 된 상태인지 체크하는 if문
        form.instance.author = current_user

        # 태그와 관련된 작업을 하기 전에 form_valid()의 결괏값을 response에 저장
        response = super().form_valid(form)

        # POST 방식으로 전달된 정보 중 name="tags_str"인 데이터를 가져오기
        tags_str = self.request.POST.get("tags_str")

        # 작업이 끝나면 response 변수에 담아두었던
        # CreateView의 form_valid() 결괏값을 return
        return response

    else:
        return redirect("review_list//")

class SelectPage(ListView):
    models = Cafe
    template_name = "date/main_area.html"

    def get_queryset(self):
        cafe_list = Cafe.objects.all()

        return cafe_list

    def get_context_data(self, **kwargs):
        context =super().get_context_data()

        q = self.kwargs["q"]

        context["addr_names"] = Addr.objects.all()

        cafe_max = Cafe.objects.filter(cafe_addr__contains=q).count()

        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_1"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]
        cafe_ran = random.randint(0, cafe_max-1)
        context["cafe_recommed_2"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_3"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]

        rest_max = Rest.objects.filter(rest_addr__contains=q).count()
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_1"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_2"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_3"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]

        place_max = Place.objects.filter(place_addr__contains=q).count()

        place_ran = random.randint(0, place_max-1)
        context["place_recommed_1"] = Place.objects.filter(place_addr__contains=q)[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_2"] = Place.objects.filter(place_addr__contains=q)[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_3"] = Place.objects.filter(place_addr__contains=q)[place_ran]

        return context


class PlaceList(ListView):
    models = Cafe
    template_name = "date/place.html"

    def get_queryset(self):
        cafe_list = Cafe.objects.all()

        return cafe_list


    # def get_context_data(self,*kwargs):
    #     context = super().get_context_data()
    #
    #     context["cafe_list"] = Cafe.objects.all()
    #     context["rest_list"] = Rest.objects.all()
    #     context["place_list"] = Place.objects.all()
    #
    #     return context

class PlaceCafe(ListView):
    models = Cafe
    template_name = "date/place.html"

    def get_queryset(self):
        cafe_list = Cafe.objects.all()

        return cafe_list

class PlaceRest(ListView):
    models = Rest
    template_name = "date/place.html"

    def get_queryset(self):
        rest_list = Rest.objects.all()

        return rest_list

class PlacePlace(ListView):
    models = Place
    template_name = "date/place.html"

    def get_queryset(self):
        place_list = Place.objects.all()

        return place_list

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewWrite
    template_name = "date/review_form.html"

    # def form_valid(self, form):
    #     current_user = self.request.user
    #     if current_user.is_authenticated:
    #         form.instance.author = current_user
    #
    #         # 태그와 관련된 작업을 하기 전에 form_valid() 결과값을 response에 저장
    #         response = super().form_valid(form)
    #
    #         return response
    #
    #     else:
    #         return redirect("/")
    #
    #     # 권한이 있는지 체크하는 함수
    # def test_func(self):
    #     current_user = self.request.user
    #     return current_user.is_authenticated
    def get_success_url(self):
        return reverse('review_list')

def ReviewUpdate(request, pk):
    # 이전 글의 데이터를 받아 옴
    post = get_object_or_404(Review, pk=pk)

    # 글을 수정하기 위해 페이지에 접속 후 제출을 눌렀을 때, POST 방식을 사용한다는 전제를 두고 있기 때문에
    # form = ReviewWrite(request.POST, instance = post)로 활용
    if request.method == "POST":
        form = ReviewWrite(request.POST, instance = post)

        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_list', pk = review.pk)

    # 글을 수정하기 위해 페이지에 처음 접속했을 때(url로 get방식을 활용하기 때문에,
    # form = PhotoForm(instance = post)에 request.POST를 집어넣을 필요가 없음
    else:
        form = ReviewWrite(instance = post)
        return render(request, 'date/review_update.html', {"form" : form})