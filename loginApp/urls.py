from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]