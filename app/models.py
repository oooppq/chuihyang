from argparse import _MutuallyExclusiveGroup
import pstats
from django.db import models
from django.conf import settings


class Note_top(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Note_middle(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Note_base(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Perfumer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Perfume(models.Model):
    # 선택지 정리
    SEASON_CHOICES = {
        ('summer', 'summer'),
        ('spring', 'spring'),
        ('fall', 'fall'),
        ('winter', 'winter')
    }
    FLAVOR_CHOICES = {
        ('floral', 'floral'),
        ('Woody', 'woody'),
        ('fresh', 'fresh'),
        ('oriental', 'oriental')
    }
    AGE_CHOICES = {
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50 or more', '50 or more')
    }
    GENDER_CHOICES = {
        ('man', 'man'),
        ('woman', 'woman')
    }

    # 디테일 페이지 필수 정보
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True,
                              upload_to='images/')
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    perfumers = models.ManyToManyField(Perfumer)

    notes_top = models.ManyToManyField(Note_top)
    notes_middle = models.ManyToManyField(Note_middle)
    notes_base = models.ManyToManyField(Note_base)

    # 기타 상세 설명? 필요 없으면 지워도 됨
    explain = models.CharField(max_length=200, null=True)

    # 필터 검색 관련
    season = models.CharField(
        choices=SEASON_CHOICES, max_length=20, null=True)
    price = models.IntegerField(null=True)
    flavor = models.CharField(
        choices=FLAVOR_CHOICES, max_length=20, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True)
    age = models.CharField(
        choices=AGE_CHOICES, max_length=20, null=True)
    situation = models.CharField(max_length=50, null=True)        # 수정 필요

    def __str__(self):
        return self.name


class Review(models.Model):
    # 선택지 정리
    POWER_CHOICES = {
        ('good', 'good'),
        ('moderate', 'moderate'),
        ('bad', 'bad'),
    }

    # 필수 정보
    date = models.DateTimeField(auto_now_add=True)
    perfume = models.ForeignKey(
        Perfume, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, on_delete=models.SET_NULL)
    # 세부 정보
    power = models.CharField(
        choices=POWER_CHOICES, max_length=20, null=True)
    type_explain = models.TextField(null=True)  # 타입 ex. 달콤한
    content = models.TextField()
    first_scent = models.TextField(null=True)  # 시향
    put_scent = models.TextField(null=True)  # 착향
    rest_scent = models.TextField(null=True)  # 잔향

    def __str__(self):
        return self.content
