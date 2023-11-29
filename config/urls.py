"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", home_page, name="homepage"),
    path("admin/", admin.site.urls),
    path("ilovethisguy/", ilovethisguy),
    path("hey/", hey_name, name="hey_name"),
    path("age_in_2050", age_in, name="age_in"),
    path("order_total", order_total, name= "order_total"),
    path("warmup-2/font-times/", font_times, name= "font"),
    path("logic-2/no-teen-sum/", teen_sum, name="teen"),
    path("string-2/xyz-there/", xyz, name="xyz"),
    path("list-2/centered-average/", centered_average, name="center")
]
