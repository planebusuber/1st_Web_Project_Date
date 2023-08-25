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

# 장소페이지에서 관광지를 클릭했을 때 보여줄 페이지
class PlacePlace(ListView):
    models = Place  # 모델은 place를 사용
    template_name = "date/place.html"   # 템플릿을 설정

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
    models = Cafe   # 모델은 cafe를 사용
    template_name = "date/place.html"   # 템플릿을 설정

    #가져올 데이터를 설정
    def get_queryset(self):
        # 주소창으로 받아온 데이터
        q = self.kwargs["q"]
        # 주소창으로 받아온 데이터로 리스트 조회
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


# 리뷰의 리스트들을 보여주는 뷰
class ReviewList(ListView):
    model = Review # 모델을 Review로 설정
    paginate_by = 5 # 한 페이지에 5개 까지 보여지게 함
    ordering = ['-created_at'] # 게시글 최신순 정렬
    template_name = "date/review_list.html" # 템플릿 지정


# 리뷰 생성을 위한 view 작성(CBV)
class ReviewCreate(CreateView):
    # model은 Review 모델을 사용
    model = Review
    # Forms.py에서 작성한 ReviewWrite를 통째로 사용
    form_class = ReviewWrite
    # 템플릿 지정
    template_name = "date/review_form.html"

    # 요청이 유효할 경우의 함수 작성
    def form_valid(self, form):
        current_user = self.request.user
        # 사용자가 로그인한 상태라면
        if current_user.is_authenticated:
            # current_user를 author에 저장
            form.instance.author = current_user
            # cafe_num을 q1에 저장, 리뷰 상세페이지의 주소로 활용하기 위함
            form.instance.cafe_num = (self.kwargs["q1"])
            # rest_num을 q2에 저장, 리뷰 상세페이지의 주소로 활용하기 위함
            form.instance.rest_num = (self.kwargs["q2"])
            # place_num을 q3에 저장, 리뷰 상세페이지의 주소로 활용하기 위함
            form.instance.place_num = (self.kwargs["q3"])
            # 태그와 관련된 작업을 하기 전에 form_valid() 결과값을 response에 저장
            response = super().form_valid(form)
            # 저장된 response 값을 반환
            return response

        # 그 외의 경우 대문페이지로 이동
        else:
            return redirect("/")

    # 성공할 경우 my_review 라는 주소를 가진 페이지로 이동
    def get_success_url(self):
        return reverse('my_review')

# 리뷰 상세페이지 구현(CBV)
class ReviewDetail(DetailView):
    # model은 Review 모델을 사용
    model = Review
    # 템플릿 지정
    template_name = "date/review_detail.html"

    # 작성된 리뷰를 불러오기 위해 함수 작성
    def get_context_data(self, **kwargs):
        # get_context_data 메서드를 호출하여 초기 컨텍스트를 가져옴
        context = super().get_context_data()

        pk = (self.kwargs["pk"])
        # review에 Review모델에 작성된 내용을 pk를 기준으로 읽어들임
        review = Review.objects.get(pk=pk)

        # 추천이 다 다르게 진행되기 때문에 해당 정보를 불러오기 위해 번호 정보를 지정
        # Review모델에서 선언한 cafe_num, rest_num, place_num 활용
        cafe = review.cafe_num
        rest = review.rest_num
        place = review.place_num

        # context를 통해 카페, 식당, 관광지의 정보와 별점 평가된 정보를 불러옴
        context["cafe_detail_list"] = Cafe.objects.get(cafe_num=cafe)
        context["rest_detail_list"] = Rest.objects.get(rest_num=rest)
        context["place_detail_list"] = Place.objects.get(place_num=place)
        context["form"] = Star(instance=review)

        # context를 반환
        return context

# 리뷰 수정 view 작성(FBV)
def ReviewUpdate(request, pk):
    # 이전 글의 데이터를 받아 옴
    review = get_object_or_404(Review, pk=pk)

    # 글을 수정하기 위해 페이지에 접속 후 제출을 눌렀을 때, POST 방식을 사용한다는 전제를 두고 있기 때문에
    # form = ReviewWrite(request.POST, instance = post)로 활용
    if request.method == "POST":
        form = ReviewWrite(request.POST, instance = review)

        # form이 유효할 경우
        if form.is_valid():
            review = form.save(commit=False)
            # 수정된 내용을 저장
            review.save()
            # 수정하기를 눌렀던 상세페이지로 돌아가게 함
            return redirect('review_detail', pk = review.pk)

    # 글을 수정하기 위해 페이지에 처음 접속했을 때(url로 get방식을 활용하기 때문에,
    # form = ReviewWrite(instance = review)에 request.POST를 집어넣을 필요가 없음
    else:
        form = ReviewWrite(instance = review)
        return render(request, 'date/review_update.html', {"form" : form})

# 내가 작성한 리뷰만 볼 수 있는 View(CBV)
class MyReview(ListView):
    # model은 Review 모델을 사용
    model = Review
    # 페이지네이션 기능 사용(Django에 탑재된 기능, import 필요)
    paginate_by = 5
    # 템플릿 설정
    template_name = "date/my_review.html"

    # 내가 작성한 리뷰를 불러오기 위해 함수 작성
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # current_user : 현재 로그인된 사용자를 나타내는 속성
        current_user = self.request.user
        # 작성자가 현재 로그인된 사용자인 Review의 정보만 담아올 수 있게 함
        context["review_list"] = Review.objects.filter(author=current_user).order_by('-created_at')
        # context 값 출력
        return context

# 리뷰 삭제를 위한 view 작성(FBV)
def ReviewDelete(request, pk):
    # review의 내용을 담아옴
    review = get_object_or_404(Review, pk=pk)

    # 해당 삭제요청을 한 사용자와 작성자가 일치하는 경우
    if request.user.is_authenticated and request.user == review.author:
        # 리뷰를 삭제하고 리뷰의 상세페이지로 리다이렉트
        review.delete()
        return redirect("/myreview/")
    # 그 외의 경우에는 권한 거부 예외를 발생시킴
    else:
        PermissionDenied