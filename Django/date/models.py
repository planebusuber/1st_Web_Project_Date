from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class Addr(models.Model):
    addr_name = models.CharField(max_length = 10,primary_key = True)

    class Meta:
        managed = False
        db_table = 'addr'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cafe(models.Model):
    cafe_num = models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    cafe_img = models.IntegerField()
    cafe_addr = models.CharField(max_length=40)
    cafe_menu = models.CharField(max_length=50)
    cafe_time = models.CharField(max_length=75)
    cafe_detail = models.CharField(max_length=120)


    def __str__(self):
        return f"[{self.cafe_num}] {self.cafe_name}"

    class Meta:
        managed = False
        db_table = 'cafe'


class DateTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Place(models.Model):
    place_num = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=50)
    place_img = models.IntegerField()
    place_addr = models.CharField(max_length=40)
    place_time = models.CharField(max_length=400)
    place_detail = models.CharField(max_length=300)


    def __str__(self):
        return f"[{self.place_num}] {self.place_name}"

    class Meta:
        managed = False
        db_table = 'place'



class Rest(models.Model):
    rest_num = models.AutoField(primary_key=True)
    rest_name = models.CharField(max_length=50)
    rest_img = models.IntegerField()
    rest_addr = models.CharField(max_length=40)
    rest_menu = models.CharField(max_length=150)
    rest_time = models.CharField(max_length=400)
    rest_detail = models.CharField(max_length=700)


    def __str__(self):
        return f"[{self.rest_num}] {self.rest_name}"

    class Meta:
        managed = False
        db_table = 'rest'


class Review(models.Model): # Review 작성 모델
    title = models.CharField(max_length=50)
    content = models.TextField() # 글내용, 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # 작성일, 날짜 + 시간
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cafe_num = models.IntegerField(default=0)
    rest_num = models.IntegerField(default=0)
    place_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Comment(models.Model): # 댓글 기능 모델
    post = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
    content = models.TextField() # 게시글
    created_at = models.DateTimeField(auto_now_add=True) # 작성일자
    modified_at =models.DateTimeField(auto_now=True) # 수정일자

