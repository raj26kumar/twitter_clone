from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager






class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("user must have a username")

        user = self.model(email = self.normalize_email(email),
            username=username
            )
        user.set_password(password)
        user.save(usingself._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                    email=self.normalize_email(email),
                    password=password,
                    username=username
                )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    email                = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username             = models.CharField(max_length=30,unique=True)
    date_joined          = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login           = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin             = models.BooleanField(default=False)
    is_active            = models.BooleanField(default=True)
    is_staff             = models.BooleanField(default=False)
    is_superuser         = models.BooleanField(default=False)
    user = models.OneToOneField("self", on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    # def gravatar_url(self):
    #     return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()


    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label ):
        return True


class Tweet(models.Model):
    content       = models.CharField(max_length = 140)
    user          = models.ForeignKey(Account,on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
