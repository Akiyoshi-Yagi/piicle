from django.db import models

# Create your models here.
class Camera(models.Model):
    name = models.CharField("カメラの名前", max_length=255)
    maker = models.CharField("メーカー", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "カメラ"

class Lens(models.Model):
    name = models.CharField("レンズの名前", max_length=255)
    maker = models.CharField("メーカー", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "レンズ"

class User(models.Model):

    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )
    name = models.CharField("ニックネーム", max_length=255)
    gender = models.IntegerField("性別", choices=GENDER_CHOICES, blank=True, null=True)
    birth_day = models.DateField("生年月日", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    introduction = models.TextField("自己紹介")
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, blank=True, null=True)
    lens = models.ForeignKey(Lens, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ユーザー"


class Image(models.Model):

    picture = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, blank=True, null=True)
    lens = models.ForeignKey(Lens, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField("説明")

    class Meta:
        verbose_name_plural = "写真"

    def __str__(self):
        return self.title









