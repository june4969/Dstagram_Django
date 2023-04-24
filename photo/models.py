from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# 성별 선택할 수 있도록
GENDER_C = (
    ('선택안함', '선택안함'),
    ('여성', '여성'),
    ('남성', '남성'),
)
class User(AbstractUser):
    gender = models.CharField(max_length=10, choices=GENDER_C, default='N')
    birthdate = models.DateField(null=True, blank=True)
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') #참조역할(작성자정보), user는 디폴트 on_delete는 동작 지정,models.CASCADE는 하위개체도 같이 삭제함
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated']

    def __str__(self): #작성자의 이름과 글 작성일을 합친 문자열 반환
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])


class Question(models.Model): #초이스는 어느 질문에 속하는 것인지
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


