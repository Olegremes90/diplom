"""
URL configuration for SilantProject project.

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
from django.urls import path, include, re_path
from silant import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/todo/', views.MachineList.as_view(), name='todo_list'),
    path('api/todo/<int:pk>', views.MachineDetail.as_view(), name='todo_detail'),
    path('api/TO/', views.TOList.as_view(), name='to_list'),
    path('api/TO/<int:pk>', views.TOApiUpdate.as_view(), name='update_list'),
    path('api/service/', views.ServiceCompanyList.as_view(), name='service_list'),
    path('api/vidi/', views.Vidi_TOList.as_view(), name='vidi_list'),
    path('api/complaint/', views.ComplaintList.as_view(), name='complaint_list'),
    path('api/usel/', views.UselList.as_view(), name='usel_list'),
    path('api/recovery/', views.RecoveryList.as_view(), name='recovery_list'),
    path('api/complaint/', views.ComplaintList.as_view(), name='complaint_list'),
    path('api/complaint/<int:pk>', views.ComplaintApiUpdate.as_view(), name='update_complaint'),
    path('api/client/', views.ClientList.as_view(), name='client_list'),
    path('api/engine/', views.EngineList.as_view(), name='engine_list'),
    path('api/transmisia/', views.TransimisiaList.as_view(), name='transmisia_list'),
    path('api/steerablebridge/', views.SteerableBridgeList.as_view(), name='steerable_list'),
    path('api/lead/', views.LeadList.as_view(), name='lead_list'),
    path('api/technica/', views.TechnicList.as_view(), name='technic_list'),
    path('api/machine/', views.new_machine, name='machine_list'),
    path('api/to/add/', views.new_TO, name='to-add'),
    path('api/complaint/add/', views.new_complaint, name='complaint_add'),
    path('api/machine/<int:pk>', views.UpdateMachine.as_view(), name='update_machine'),
    path('api/group/', views.GroupList.as_view(), name='group_list'),
    path('api/auto/', views.filter_data),
    path('api/bridge/add/', views.new_bridge),
    path('api/transmisia/add/', views.new_transmisia),
    path('api/service/add/', views.new_service),
    path('api/engine/add/', views.new_engine),
    path('api/technic/add/', views.new_technic),
    path('api/lead/add/', views.new_lead),
    path('api/usel/add/', views.new_usel),
    path('api/recovery/add/', views.new_recovery),
    path('api/vid/add', views.new_vid),
    path('api/complaint-filter/<int:pk>', views.ListComplaint.as_view()),
    # URLs for class-based views (ModelViewSets)
    # http://localhost:8000/general/users/
    # http://localhost:8000/general/groups/
    path('api/machine-list', views.AutoList.as_view()),
    path('api/lead-detail/<str:title>/', views.LeadDetail.as_view()),
    path('api/engine-detail/<str:title>/', views.EngineDetail.as_view()),
    path('api/technica-detail/<str:title>/', views.TechnicDetail.as_view()),
    path('api/transmisia-detail/<str:title>', views.TransmisiaDetail.as_view()),
    path('api/bridge-detail/<str:title>', views.BridgeDetail.as_view()),
    path('api/service-detail/<str:title>', views.ServiceDetail.as_view()),
    path('api/engine-detail/<str:title>', views.EngineDetail.as_view()),
    path('api/vid-detail/<str:title>', views.VidDetail.as_view()),
    path('api/update-service/<int:pk>', views.ServiceApiUpdate.as_view()),  #
    path('api/usel-detail/<str:title>', views.UselDetail.as_view()),
    path('api/recovery-detail/<str:title>', views.RecoveryDetail.as_view()),
    path('api/machine-number/', views.MachineNumber.as_view()),
    path('api/update-engine/<int:pk>', views.EngineApiUpdate.as_view()),
    path('api/update-lead/<int:pk>', views.LeadApiUpdate.as_view()),
    path('api/update-vid/<int:pk>', views.VidApiUpdate.as_view()),
    path('api/update-technica/<int:pk>', views.TechnicaApiUpdate.as_view()),
    path('api/update-bridge/<int:pk>', views.BridgeApiUpdate.as_view()),
    path('api/update-transmisia/<int:pk>', views.TransmisiaApiUpdate.as_view()),
    path('api/update-usel/<int:pk>', views.UselApiUpdate.as_view()),
    path('api/update-recovery/<int:pk>', views.RecoveryApiUpdate.as_view()),
    # Include default login and logout views for use with the browsable API.
    # Optional, but useful if your API requires authentication and you want to use the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API to generate auth token from user. Note that the URL part of the pattern can be whatever you want to use.
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
