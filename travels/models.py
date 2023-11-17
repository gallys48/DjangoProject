from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

def gen_slug(s):
  new_slug = slugify(s, allow_unicode=True)
  return new_slug

class Travel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255, verbose_name="Заголовок поста")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст поста")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    start_of_the_trip = models.DateField( verbose_name="Дата начала путешествия")
    end_of_the_trip = models.DateField( verbose_name="Дата окончания путешествия")
    expense = models.CharField(max_length=255, verbose_name="Затраченные средства")
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Страна путешествия", default='')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания поста")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время редактирования поста")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован?")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name="Категория поста")

    def __str__(self):
        return self.title
    
    @property
    def get_duration(self):
        dt=self.end_of_the_trip-self.start_of_the_trip
        return dt.days
    
    def get_absolute_url(self):
        return reverse("travel", kwargs={"travel_slug": self.slug})
    
    def get_my_travels_url(self):
        return reverse("my_travel", kwargs={"travel_slug": self.slug})
    
    def get_update_url(self):
        return reverse("travel_update", kwargs={"travel_slug": self.slug})
    
    def get_delete_url(self):
        return reverse("travel_delete", kwargs={"travel_slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пост о путешествии'
        verbose_name_plural = 'Посты о путешествии'
        ordering = ['-time_create', 'title']

class Category(models.Model):
    title=models.CharField(max_length=100 , db_index=True, verbose_name="Название категории") 
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='avatars/%Y/%m/%d/', 
        default='avatars/default.jpg',)
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:

        db_table = 'app_profiles'
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = gen_slug(self.user.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'profile_slug': self.slug})
    def get_my_profile_url(self):
        return reverse('my_profile_detail', kwargs={'profile_slug': self.slug})
    def get_update_profile_url(self):
        return reverse("profile_edit", kwargs={"profile_slug": self.slug})
    def get_travels_url(self):
        return reverse("usertravels", kwargs={"profile_user": self.user.id, "profile_name": self.user.username})
    def get_my_travels_url(self):
        return reverse("my_usertravels", kwargs={"my_slug": self.slug})
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Country(models.Model):
    title=models.CharField(max_length=100 , db_index=True, verbose_name="Название страны") 
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("country", kwargs={"country_slug": self.slug})

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

