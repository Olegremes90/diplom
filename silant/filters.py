from django_filters import rest_framework as filters
from .models import Machine, Complaint, TO



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass
class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass
class MachineFilter(filters.FilterSet):
    number = NumberInFilter(field_name='service_model', lookup_expr='in')
    transmisia = CharFilterInFilter(field_name='model_transmisia', lookup_expr='in')
    engine = CharFilterInFilter(field_name='model_engine', lookup_expr='in')
    technic = CharFilterInFilter(field_name='model_technic', lookup_expr='in')
    lead = CharFilterInFilter(field_name='lead_model',  lookup_expr='in')
    steerable_bridge = CharFilterInFilter(field_name='model_steerable_bridge', lookup_expr='in')
    class Meta:
        model = Machine
        fields = ['number', 'transmisia', 'engine', 'technic', 'lead', 'steerable_bridge']


class ComplaintFilter(filters.FilterSet):
    usel = CharFilterInFilter(field_name='usel', lookup_expr='in')
    recovery = CharFilterInFilter(field_name='recovery', lookup_expr='in')
    service = CharFilterInFilter(field_name='service_org', lookup_expr='in')
    class Meta:
       model = Complaint
       fields = ['usel', 'recovery', 'service']


class TOFilter(filters.FilterSet):
    machine = CharFilterInFilter(field_name='car', lookup_expr='in')
    vid_to = CharFilterInFilter(field_name='vid_to', lookup_expr='in')
    company = CharFilterInFilter(field_name='service_company', lookup_expr='in')

    class Meta:
        model = TO
        fields = ['machine', 'vid_to', 'company']