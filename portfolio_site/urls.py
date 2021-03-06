
from django.contrib import admin
from django.urls import path , include
from exchangeRate import views as erViews
from quote_generator import views
from portfolio import views as portfolioViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quote/',views.home, name = 'quotes'),
    path('exchange/', erViews.home, name= 'exchagne'),
    path('', portfolioViews.home, name='home'),
    path('blog/',include('blog.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
