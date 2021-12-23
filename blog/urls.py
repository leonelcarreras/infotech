from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from posts.views import(avatars, index, blog, loginPage, 
logoutUser, post, registerPage, search, createOrder)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('logout/', logoutUser, name="logout"),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post-detail'),
    path('accounts/', include('allauth.urls')),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('avatars/', avatars),
    path('create_order/', createOrder, name="create_order"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)