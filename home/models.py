# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Business Profile(models.Model):

    #__Business Profile_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    entity_name = models.CharField(max_length=255, null=True, blank=True)
    legal_name = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.TextField(max_length=255, null=True, blank=True)
    city = models.TextField(max_length=255, null=True, blank=True)
    state = models.TextField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    gstin = models.CharField(max_length=255, null=True, blank=True)
    gst_register_status = models.BooleanField()
    gst_register_status_nature = models.BooleanField()
    bank_account = models.CharField(max_length=255, null=True, blank=True)
    ifsc = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Business Profile_FIELDS__END

    class Meta:
        verbose_name        = _("Business Profile")
        verbose_name_plural = _("Business Profile")



#__MODELS__END
