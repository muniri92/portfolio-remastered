"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from portfolio_api.views import AboutAPI, PortfolioAPI, EducationAPI, ExperienceAPI
from portfolio_app.views import ClassView
from portfolio_app.views import ContactView
admin.autodiscover()

urlpatterns = [
    url(r'^api/about$', AboutAPI.as_view()),
    url(r'^api/portfolio$', PortfolioAPI.as_view()),
    url(r'^api/education$', EducationAPI.as_view()),
    url(r'^api/experience$', ExperienceAPI.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^', ClassView.as_view(template_name="portfolio_app/index.html"), name="home"),
    url(r'^hireme/$', ContactView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
