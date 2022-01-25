"""stryvs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('register/', user_views.user_register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('product-register/', store_views.product_register, name="product-register"),
    path('store?<int:id>&<str:transaction>&<str:action>/', store_views.store, name = "store"),
    path('details?<int:product_id>&<str:action>/', store_views.details, name = "product-details"),
    path('profile?<int:owner_id>&<int:product_id>/', user_views.Profile_, name='profile'),
    path('details/Rent?<int:product_id>', store_views.Rent, name="Rent"),
    path('store/update_product?<int:product_id>&<str:action>/', store_views.UpdateProduct , name = "product-update"),
    path('my_transactions?<str:product_id>/', user_views.transactions, name="Trasacts"),
    path('manage_appointments?<str:flag>&<int:appointment_id>/', user_views.manage_appointments, name="manage-appointments"),
    path('store/make_appointments?<int:product_id>/', user_views.make_appointment, name="make-appointments"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
