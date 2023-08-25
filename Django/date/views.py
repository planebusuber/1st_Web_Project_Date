from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, DetailView
from date.models import Cafe, Rest, Place, Review, Addr
from .forms import ReviewWrite, Star
import random
from django.core.exceptions import PermissionDenied #권한 없는 유저 거르기

#메인페이지 구성을 위한 뷰
class MainPage(ListView):
    model = Cafe    #cafe 모델사용
    template_name = "date/main_area.html"   #템플릿사용

    #가져올 데이터 설정
    def get_context_data(self, **kwargs):
        context =super().get_context_data()
        #주소 설정을 위한 데이터
        context["addr_names"] = Addr.objects.all()
        #추천코스중 카페를 구성하기 위한 데이터
        #카페데이터중 랜덤으로 하나를 가져옴
        cafe_max = Cafe.objects.all().count()
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_1"] = Cafe.objects.all()[cafe_ran]
        cafe_ran = random.randint(0, cafe_max-1)
        context["cafe_recommed_2"] = Cafe.objects.all()[cafe_ran]
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_3"] = Cafe.objects.all()[cafe_ran]

        #추천코스중 식당을 구성하기 위한 데이터
        #식당데이터중 랜덤으로 하나를 가져옴
        rest_max = Rest.objects.all().count()
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_1"] = Rest.objects.all()[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_2"] = Rest.objects.all()[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_3"] = Rest.objects.all()[rest_ran]

        #추천코스중 관광지를 구성하기 위한 데이터
        #관광지데이터중 랜덤으로 하나를 가져옴
        place_max = Place.objects.all().count()
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_1"] = Place.objects.all()[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_2"] = Place.objects.all()[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_3"] = Place.objects.all()[place_ran]

        #별점높은 순으로 정렬후 3개를 가져옴
        context["review_top"] = Review.objects.all().order_by('-score')[:3]

        return context


class ReviewList(ListView):
    model = Review
    paginate_by = 5
    ordering = ['-created_at'] # 게시글 최신순 정렬
    template_name = "date/review_list.html"

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

#메인페이지에서 주소를 클릭했을 때 보여질 뷰
class SelectPage(ListView):
    models = Cafe   #모델은 cafe를 사용
    template_name = "date/main_area.html"   #템플릿설정

    def get_queryset(self):
        cafe_list = Cafe.objects.all()

        return cafe_list

    #가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context =super().get_context_data()
        # 주소창으로 받아온 데이터
        q = self.kwargs["q"]
        #주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()

        # 추천코스중 카페를 구성하기 위한 데이터
        # 카페 데이터중 설정된 주소에 맞는 데이터를 랜덤으로 가져옴
        cafe_max = Cafe.objects.filter(cafe_addr__contains=q).count()

        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_1"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]
        cafe_ran = random.randint(0, cafe_max-1)
        context["cafe_recommed_2"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]
        cafe_ran = random.randint(0,cafe_max-1)
        context["cafe_recommed_3"] = Cafe.objects.filter(cafe_addr__contains=q)[cafe_ran]

        # 추천코스중 식당을 구성하기 위한 데이터
        # 식당 데이터중 설정된 주소에 맞는 데이터를 랜덤으로 가져옴
        rest_max = Rest.objects.filter(rest_addr__contains=q).count()
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_1"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_2"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]
        rest_ran = random.randint(0, rest_max-1)
        context["rest_recommed_3"] = Rest.objects.filter(rest_addr__contains = q)[rest_ran]

        # 추천코스중 관광지를 구성하기 위한 데이터
        # 관광지 데이터중 설정된 주소에 맞는 데이터를 랜덤으로 가져옴
        place_max = Place.objects.filter(place_addr__contains=q).count()
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_1"] = Place.objects.filter(place_addr__contains=q)[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_2"] = Place.objects.filter(place_addr__contains=q)[place_ran]
        place_ran = random.randint(0, place_max-1)
        context["place_recommed_3"] = Place.objects.filter(place_addr__contains=q)[place_ran]


        return context

#장소페이지에서 초기화면을 보여주기위한 뷰
class PlaceList(ListView):
    models = Cafe   #모델은 cafe를 사용
    template_name = "date/place.html"   #템플릿 설정

    #가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context =super().get_context_data()
        #주소 설정을 위한 데이터
        context["addr_names"] = Addr.objects.all()

        return context
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

#장소페이지에서 카페를 클릭했을 때 보여줄 페이지
class PlaceCafe(ListView):
    models = Cafe   #모델은 cafe를 사용
    template_name = "date/place.html"   #템플릿 설정

    def get_queryset(self):
        cafe_list = Cafe.objects.all()

        return cafe_list

    #가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        #주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        #카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        #카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 1

        return context

#장소페이지에서 식당을 클릭했을 때 보여줄 페이지
class PlaceRest(ListView):
    models = Rest   #모델은 rest를 사용
    template_name = "date/place.html"   #템플릿을 설정

    def get_queryset(self):
        rest_list = Rest.objects.all()

        return rest_list

    #가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        # 카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        # 카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 2
        return context

#장소페이지에서 식당을 클릭했을 때 보여줄 페이지
class PlacePlace(ListView):
    models = Place  #모델은 place를 사용
    template_name = "date/place.html"   #템플릿을 설정

    def get_queryset(self):
        place_list = Place.objects.all()

        return place_list

    # 가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        # 카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        # 카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 3

        return context

#장소페이지에서 카페와 장소를 클릭했을 때 보여줄 뷰
class PlaceCafeLoc(ListView):
    models = Cafe   #모델은 cafe를 사용
    template_name = "date/place.html"   #템플릿을 설정

    #가져올 데이터를 설정
    def get_queryset(self):
        #주소창으로 받아온 데이터
        q = self.kwargs["q"]
        #주소창으로 받아온 데이터로 리스트 조회
        cafe_list_loc = Cafe.objects.filter(cafe_addr__contains=q)

        return cafe_list_loc

    #가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        # 카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        # 카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 1

        return context

#장소페이지에서 식당과 장소를 클릭했을 때 보여줄 뷰
class PlaceRestLoc(ListView):
    models = Rest   #모델은 rest를 사용
    template_name = "date/place.html"   #템플릿을 설정

    #가져올 데이터를 설정
    def get_queryset(self):
        #주소창으로 받아온 데이터
        q = self.kwargs["q"]
        # 주소창으로 받아온 데이터로 리스트 조회
        rest_list_loc = Rest.objects.filter(rest_addr__contains=q)

        return rest_list_loc

    # 가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        # 카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        # 카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 2

        return context

#장소페이지에서 관광지와 장소를 클릭했을 때 보여줄 뷰
class PlacePlaceLoc(ListView):
    models = Place  #모델은 place를 사용
    template_name = "date/place.html"   #템플릿을 설정

    # 가져올 데이터를 설정
    def get_queryset(self):
        # 주소창으로 받아온 데이터
        q = self.kwargs["q"]
        # 주소창으로 받아온 데이터로 리스트 조회
        place_list_loc = Place.objects.filter(place_addr__contains=q)

        return place_list_loc

    # 가져올 데이터를 설정
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # 주소를 설정하기 위한 데이터
        context["addr_names"] = Addr.objects.all()
        # 카페,식당,관광지를 구분하기 위한 데이터
        context["crp_check"] = 1
        # 카페,식당,관광지를 클릭했는지 구분하기 위한 데이터
        context["check"] = 3
        return context

class CafeDetail(ListView):
    models = Cafe
    template_name = "date/place_detail.html"

    def get_queryset(self):
        q = self.kwargs["q"]

        cafe_list = Cafe.objects.filter(cafe_name__contains=q)

        return cafe_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        q = self.kwargs["q"]

        context["cafe_detail_list"] = Cafe.objects.get(cafe_name=q)
        context["check"] = 1

        return context
class RestDetail(ListView):
    models = Rest
    template_name = "date/place_detail.html"
    def get_queryset(self):
        q = self.kwargs["q"]

        rest_list = Rest.objects.filter(rest_name__contains=q)

        return rest_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        q = (self.kwargs["q"])

        context["rest_detail_list"] = Rest.objects.get(rest_name=q)
        context["check"] = 2

        return context
class PlaceDetail(ListView):
    models = Place
    template_name = "date/place_detail.html"
    def get_queryset(self):
        q = self.kwargs["q"]

        place_list = Place.objects.filter(place_name__contains=q)

        return place_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        q = (self.kwargs["q"])

        context["place_detail_list"] = Place.objects.get(place_name=q)
        context["check"] = 3

        return context

class CosPage(ListView):
    models = Cafe
    template_name = "date/cos.html"
    def get_queryset(self):

       list = Cafe.objects.all()

       return list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        q1 = (self.kwargs["q1"])
        q2 = (self.kwargs["q2"])
        q3 = (self.kwargs["q3"])

        context["cafe_detail_list"] = Cafe.objects.get(cafe_num=q1)
        context["rest_detail_list"] = Rest.objects.get(rest_num=q2)
        context["place_detail_list"] = Place.objects.get(place_num=q3)
        print(q1)
        return context

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewWrite
    template_name = "date/review_form.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            form.instance.cafe_num = (self.kwargs["q1"])
            form.instance.rest_num = (self.kwargs["q2"])
            form.instance.place_num = (self.kwargs["q3"])
            # 태그와 관련된 작업을 하기 전에 form_valid() 결과값을 response에 저장
            response = super().form_valid(form)

            return response

        else:
            return redirect("/")

        # 권한이 있는지 체크하는 함수
    # def test_func(self):
    #     current_user = self.request.user
    #     return current_user.is_authenticated
    def get_success_url(self):
        return reverse('my_review')

class ReviewDetail(DetailView):
    model = Review
    template_name = "date/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        pk = (self.kwargs["pk"])

        review = Review.objects.get(pk=pk)

        cafe = review.cafe_num
        rest = review.rest_num
        place = review.place_num

        context["cafe_detail_list"] = Cafe.objects.get(cafe_num=cafe)
        context["rest_detail_list"] = Rest.objects.get(rest_num=rest)
        context["place_detail_list"] = Place.objects.get(place_num=place)
        context["form"] = Star(instance=review)

        return context

def ReviewUpdate(request, pk):
    # 이전 글의 데이터를 받아 옴
    review = get_object_or_404(Review, pk=pk)

    # 글을 수정하기 위해 페이지에 접속 후 제출을 눌렀을 때, POST 방식을 사용한다는 전제를 두고 있기 때문에
    # form = ReviewWrite(request.POST, instance = post)로 활용
    if request.method == "POST":
        form = ReviewWrite(request.POST, instance = review)

        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_detail', pk = review.pk)

    # 글을 수정하기 위해 페이지에 처음 접속했을 때(url로 get방식을 활용하기 때문에,
    # form = ReviewWrite(instance = review)에 request.POST를 집어넣을 필요가 없음
    else:
        form = ReviewWrite(instance = review)
        return render(request, 'date/review_update.html', {"form" : form})


class MyReview(ListView):
    model = Review
    paginate_by = 5
    ordering = ['-created_at']  # 게시글 최신순 정렬
    template_name = "date/my_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        current_user = self.request.user
        context["review_list"] = Review.objects.filter(author=current_user)
        return context

def ReviewDelete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.user.is_authenticated and request.user == review.author:
        # 조건을 만족하면 댓글을 삭제하고 댓글이 달려있던 게시글의 상세페이지로 리다이렉트
        review.delete()
        return redirect("/myreview/")
    else:
        PermissionDenied