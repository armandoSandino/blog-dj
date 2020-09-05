import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView
)

class TestPlantilla(TemplateView):
    template_name = "plantillas/register.html"
