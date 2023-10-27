from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
class MachineSerializer(serializers.ModelSerializer):
    title_lead = serializers.CharField(source='lead_model.title', read_only=True)
    title_technic = serializers.CharField(source='model_technic.title', read_only=True)
    title_engine = serializers.CharField(source='model_engine.title', read_only=True)
    title_transmisia = serializers.CharField(source='model_transmisia.title', read_only=True)
    title_bridge = serializers.CharField(source='model_steerable_bridge.title', read_only=True)
    title_client = serializers.CharField(source='client_model.title', read_only=True)
    title_service = serializers.CharField(source='service_model.title', read_only=True)

    class Meta:
        model = Machine
        fields = ('id', 'number_machine', 'title_technic', 'title_engine', 'number_engine', 'title_transmisia',
                  'number_transmisia', 'title_lead', 'number_lead', 'title_bridge', 'number_steerable_bridge', 'contract_postavka', 'date_otgruzka', 'consignee',
                  'adress', 'complectation', 'title_client', 'title_service')


class TOSerializer(serializers.ModelSerializer):
    car_number = serializers.CharField(source='car.number_machine', read_only=True)
    to_vid = serializers.CharField(source='vid_to.title', read_only=True)
    company = serializers.CharField(source='service_company.title', read_only=True)

    class Meta:
        model = TO
        fields = ('id', 'car_number', 'to_vid', 'data_to', 'narabotka', 'number_zakaza', 'data_zakaza', 'company')

class TOADDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TO
        fields = '__all__'

class TOUpdateSerializer(serializers.ModelSerializer):
    car_title = serializers.CharField(source='car.number_machine', read_only=True)
    class Meta:
        model = TO
        fields = ('id', 'car_title', 'vid_to', 'data_to', 'narabotka', 'number_zakaza', 'data_zakaza', 'service_company' )

class ComplaintADDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
class ComplaintSerializer(serializers.ModelSerializer):
    usel_title = serializers.CharField(source='usel.title', read_only=True)
    recovery_title = serializers.CharField(source='recovery.title', read_only=True)
    car_title = serializers.CharField(source='car_complaint.number_machine', read_only=True)
    service_title = serializers.CharField(source='service_org.title', read_only=True)




    class Meta:
        model = Complaint
        fields = ('id', 'date_refusal', 'working_off', 'usel_title', 'description', 'recovery_title', 'spare_parts', 'date_recovery', 'downtime', 'car_title', 'service_title' )
class ComplaintUpdateSerializer(serializers.ModelSerializer):
    car_title = serializers.CharField(source='car_complaint.number_machine', read_only=True)
    class Meta:
        model = Complaint
        fields = ('id',  'date_refusal', 'working_off', 'usel', 'description', 'recovery', 'spare_parts', 'date_recovery', 'downtime', 'car_title', 'service_org')
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('id','title', 'descrip')


class Vidi_TOSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vidi_TO
        fields = ('id','title', 'descrip')

class UselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usel_Refusal
        fields = '__all__'

class RecoverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Recovery
        fields = ('id', 'title', 'descrip')

class TechicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technica
        fields = ('id', 'title', 'descrip')


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'title', 'descrip')


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('id', 'title', 'descrip')


class TransmisiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmisia
        fields = ('id', 'title', 'descrip')


class SteerableBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steerable_Bridge
        fields = ('id', 'title', 'descrip')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'title', 'descrip')
class AddMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'