from django.contrib import admin
from .models import Comment, Review
from .models import Cafe,Rest,Place,Addr
# Register your models here.
admin.site.register(Cafe)
admin.site.register(Rest)
admin.site.register(Place)
admin.site.register(Addr)

admin.site.register(Comment) # admin 페이지에서 댓글 기능 관리
admin.site.register(Review) # admin 페이지에서 리뷰 작성 기능

