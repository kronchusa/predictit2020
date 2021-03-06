from django.urls import include, path

from .views import HomepageView, MyMapView, RegisterView, SaveStatesAPIView, LoadStatesAPIView, StatsView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('my_map', MyMapView.as_view(), name='my_map'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='registration'),
    path('save/', SaveStatesAPIView.as_view(), name='save_api'),
    path('load/', LoadStatesAPIView.as_view(), name='load_api'),
    path('stats/', StatsView.as_view(), name='stats')
]