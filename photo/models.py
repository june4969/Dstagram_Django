from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



#모델은 항상 models.Model을 상속받은 클래스 형태로 생성하기, Photo 모델 필드

#필드 5개 생성
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


