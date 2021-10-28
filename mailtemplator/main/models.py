from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager
import uuid
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'),max_length=30,blank=True,unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

#テンプレートのサンプル==================================
class SampleTemplates(models.Model):
    template_name = models.CharField(_('template_name'), max_length=30, blank=False)
    content = models.CharField(_('content'), max_length=2000, blank=False)
    class Meta:
        verbose_name = _('sampletemplate')
        verbose_name_plural = _('sampletemplates')
        def __str__(self):
            return str(self.template_name)

#ラベル情報==============================================
class Labels(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)#,related_name='L_users'
    label_id = models.UUIDField(
        _('label_id'),
        primary_key = False,
        default = uuid.uuid4,
        editable = False
    )
    label_name =  models.CharField(_('label_name'), max_length=30, blank=False)

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
        def __str__(self):
            return str(self.label_name)

#テンプレート============================================
class Templates(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)#,related_name='T_users'
    label = models.ForeignKey(Labels,on_delete=models.CASCADE)#,related_name='T_labels'
    template_name =  models.CharField(_('template_name'), max_length=30, blank=False)
    content = models.CharField(_('content'), max_length=2000, blank=False)

    class Meta:
        verbose_name = _('Template')
        verbose_name_plural = _('Templates')
        def __str__(self):
            return str(self.template_name)

#メールアドレス============================================
class MailAddresses(models.Model):
    user = models.ForeignKey(Users,models.DO_NOTHING)#,related_name='MA_users'
    mailaddress =  models.EmailField(_('mailaddress_name'),blank=False)
    mailaddress_pw = models.CharField(_('mailaddress_pw'), max_length=2000, blank=False)

    class Meta:
        verbose_name = _('MailAddress')
        verbose_name_plural = _('MailAddresses')
        def __str__(self):
            return str(self.mailaddress)
