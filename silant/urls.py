from django.urls import path

from . import views
from rest_framework import routers
from django.urls import path, include, re_path
# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

"""
When using viewsets instead of views, we can automatically generate the URL conf for our API, by simply registering the viewsets with a router class.

If we need more control over the API URLs we can simply drop down to using regular class-based views (APIViews), and writing the URL conf explicitly.
"""

router = routers.DefaultRouter()

# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    # URLs for class-based views (Generics, APIViews)
    # http://localhost:8000/todo/
    # http://localhost:8000/todo/<int:pk>
    path('todo/', views.MachineList.as_view(), name='todo_list'),
    path('todo/<int:pk>', views.MachineDetail.as_view(), name='todo_detail'),
    path('TO/', views.TOList.as_view(), name='to_list'),
    path('TO/<int:pk>', views.TOApiUpdate.as_view(), name='update_list'),
    path('service/', views.ServiceCompanyList.as_view(), name='service_list'),
    path('vidi/', views.Vidi_TOList.as_view(), name='vidi_list'),
    path('complaint/', views.ComplaintList.as_view(), name='complaint_list'),
    path('usel/', views.UselList.as_view(), name='usel_list'),
    path('recovery/', views.RecoveryList.as_view(), name='recovery_list'),
    path('complaint/', views.ComplaintList.as_view(), name='complaint_list'),
    path('complaint/<int:pk>', views.ComplaintApiUpdate.as_view(), name='update_complaint'),
    path('client/', views.ClientList.as_view(), name = 'client_list'),
    path('engine/', views.EngineList.as_view(), name='engine_list'),
    path('transmisia/', views.TransimisiaList.as_view(), name='transmisia_list'),
    path('steerablebridge/', views.SteerableBridgeList.as_view(), name='steerable_list'),
    path('lead/', views.LeadList.as_view(), name='lead_list'),
    path('technica/', views.TechnicList.as_view(), name='technic_list'),
    path('machine/', views.new_machine, name='machine_list'),
    path('to/add/', views.new_TO, name='to-add'),
    path('complaint/add/', views.new_complaint, name='complaint_add'),
    path('machine/<int:pk>', views.UpdateMachine.as_view(), name='update_machine'),
    path('group/', views.GroupList.as_view(), name='group_list'),
    path('auto/', views.filter_data),
    path('bridge/add/', views.new_bridge),
    path('transmisia/add/', views.new_transmisia),
    path('service/add/', views.new_service),
    path('engine/add/', views.new_engine),
    path('technic/add/', views.new_technic),
    path('lead/add/', views.new_lead),
    path('usel/add/', views.new_usel),
    path('recovery/add/', views.new_recovery),
    path('vid/add', views.new_vid),
    path('complaint-filter/<int:pk>', views.ListComplaint.as_view()),
    # URLs for class-based views (ModelViewSets)
    # http://localhost:8000/general/users/
    # http://localhost:8000/general/groups/
    path('general/', include(router.urls)),
    path('machine-list', views.AutoList.as_view()),
    path('lead-detail/<str:title>/', views.LeadDetail.as_view()),
    path('engine-detail/<str:title>/', views.EngineDetail.as_view()),
    path('technica-detail/<str:title>/', views.TechnicDetail.as_view()),
    path('transmisia-detail/<str:title>', views.TransmisiaDetail.as_view()),
    path('bridge-detail/<str:title>', views.BridgeDetail.as_view()),
    path('service-detail/<str:title>', views.ServiceDetail.as_view()),
    path('engine-detail/<str:title>', views.EngineDetail.as_view()),
    path('vid-detail/<str:title>', views.VidDetail.as_view()),
    path('update-service/<int:pk>', views.ServiceApiUpdate.as_view()),#
    path('usel-detail/<str:title>', views.UselDetail.as_view()),
    path('recovery-detail/<str:title>', views.RecoveryDetail.as_view()),
    path('machine-number/', views.MachineNumber.as_view()),
    path('update-engine/<int:pk>', views.EngineApiUpdate.as_view()),
    path('update-lead/<int:pk>', views.LeadApiUpdate.as_view()),
    path('update-vid/<int:pk>', views.VidApiUpdate.as_view()),
    path('update-technica/<int:pk>', views.TechnicaApiUpdate.as_view()),
    path('update-bridge/<int:pk>', views.BridgeApiUpdate.as_view()),
    path('update-transmisia/<int:pk>', views.TransmisiaApiUpdate.as_view()),
    path('update-usel/<int:pk>', views.UselApiUpdate.as_view()),
    path('update-recovery/<int:pk>', views.RecoveryApiUpdate.as_view()),
    # Include default login and logout views for use with the browsable API.
    # Optional, but useful if your API requires authentication and you want to use the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API to generate auth token from user. Note that the URL part of the pattern can be whatever you want to use.
    path('api-token-auth/', rest_views.obtain_auth_token, name='api-token-auth'),
]

