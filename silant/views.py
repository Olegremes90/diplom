from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Machine
from .serializers import *
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MachineFilter, ComplaintFilter, TOFilter
class MachineList(APIView):



    """
    List all todos, or create a new todo.
    """

    def get(self, request, format=None):
        user_request = request.user.id
        print(user_request)
        filter_backends = (DjangoFilterBackend,)
        filterset_class = MachineFilter
        permission_class = (IsAuthenticated,)
        auto = Machine.objects.filter(client_model__user_id=user_request).order_by('-date_otgruzka')
        print(auto)
        serializer = MachineSerializer(auto, many=True)
        return Response({'Machine': serializer.data})
class MachineNumber(APIView):

    def post(self, request, format=None):
        machine = Machine.objects.filter(number_machine=request.data)
        serializer = MachineSerializer(machine, many=True)
        return Response({'Machine': serializer.data})


class MachineDetail(ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TOFilter
    serializer_class = TOSerializer
    """
    Retrieve, update or delete a todo instance.
    """

    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            raise Http404

    def get_queryset(self, format=None):
        pk = self.kwargs['pk']
        todo = self.get_object(pk)
        print(todo)
        queryset = TO.objects.filter(car_id__number_machine=todo).order_by('-data_to')
        print(queryset)
        return queryset


class ListTO(ListAPIView):
    serializer_class = TOSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MachineFilter
    def get_queryset(self):
        queryset = Machine.objects.filter(car_id=self.request.data)
        return queryset


class TOList(APIView):
    serializer_class = TOSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MachineFilter
    def get(self, request, format=None):
        TO_list = TO.objects.all()
        serializer_to = TOSerializer(TO_list, many=True)
        return Response(serializer_to.data)

    def post(self, request, format=None):
        print(request.data)
        to_list = TO.objects.filter(car_id=request.data)
        print(to_list)
        serializer = TOSerializer(to_list, many=True)
        return Response({'TO': serializer.data})


class ServiceCompanyList(APIView):
    def get(self, request):
        company_list = Service.objects.all()

        serializer_service = ServiceSerializer(company_list, many=True)
        return Response({'Service': serializer_service.data})




class Vidi_TOList(APIView):
    def get(self, request):
        vidi_list =Vidi_TO.objects.all()
        serializer_vidi = ServiceSerializer(vidi_list, many=True)

        return Response({'Vidi_TO': serializer_vidi.data})

class TOApiUpdate(UpdateAPIView):
    queryset = TO.objects.all()
    serializer_class = TOUpdateSerializer


class ComplaintList(APIView):
    def post(self, request, format=None):
        complaint_list = Complaint.objects.filter(car_complaint=request.data).order_by('-date_refusal')
        serializer = ComplaintSerializer(complaint_list, many=True)
        return Response({'Complaint': serializer.data})


class UselList(APIView):
    def get(self, request):
        usel_list = Usel_Refusal.objects.all()
        serializer_usel = ServiceSerializer(usel_list, many=True)
        return Response({'Usels': serializer_usel.data})

class RecoveryList(APIView):
    def get(self, request):
        recovery_list = Recovery.objects.all()
        serializer_recovery = RecoverySerializer(recovery_list, many=True)
        return Response({'Recovery': serializer_recovery.data})

class ComplaintApiUpdate(UpdateAPIView):
        queryset = Complaint.objects.all()
        serializer_class = ComplaintUpdateSerializer
class ServiceApiUpdate(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BridgeApiUpdate(UpdateAPIView):
    queryset = Steerable_Bridge.objects.all()
    serializer_class = SteerableBridgeSerializer

class TransmisiaApiUpdate(UpdateAPIView):
    queryset = Transmisia.objects.all()
    serializer_class = TransmisiaSerializer

class EngineApiUpdate(UpdateAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer

class TechnicaApiUpdate(UpdateAPIView):
    queryset = Technica.objects.all()
    serializer_class = TechicSerializer

class LeadApiUpdate(UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class VidApiUpdate(UpdateAPIView):
    queryset = Vidi_TO.objects.all()
    serializer_class = Vidi_TOSerializer

class UselApiUpdate(UpdateAPIView):
    queryset = Usel_Refusal.objects.all()
    serializer_class = UselSerializer

class RecoveryApiUpdate(UpdateAPIView):
    queryset = Recovery.objects.all()
    serializer_class = RecoverySerializer
@api_view(['POST'])
def new_machine(request):
    if request.method == 'POST':
        serializer = AddMachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_TO(request):
    if request.method == 'POST':
        serializer = TOADDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_complaint(request):
    if request.method == 'POST':
        serializer = ComplaintADDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_bridge(request):
    if request.method == 'POST':
        serializer = SteerableBridgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def filter_data(request):
    machines = Machine.objects.all()
    serializer = MachineSerializer(machines, many=True)

    filterset_fields = ('number_machine',)
    return Response({'Machine': serializer.data})

@api_view(['POST'])
def new_service(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_transmisia(request):
    if request.method == 'POST':
        serializer =TransmisiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_engine(request):
    if request.method == 'POST':
        serializer = EngineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_technic(request):
    if request.method == 'POST':
        serializer = TechicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def new_lead(request):
    if request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def new_vid(request):
    if request.method == 'POST':
        serializer = Vidi_TOSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def new_usel(request):
    if request.method == 'POST':
        serializer = UselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def new_recovery(request):
    if request.method == 'POST':
        serializer = RecoverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TechnicList(APIView):
    def get(self, request):
        company_list = Technica.objects.all()

        serializer_service = TechicSerializer(company_list, many=True)
        return Response({'Technic': serializer_service.data})

class EngineList(APIView):
    def get(self, request):
        list = Engine.objects.all()

        serializer_engine = EngineSerializer(list, many=True)
        return Response({'Engine': serializer_engine.data})


class TransimisiaList(APIView):
    def get(self, request):
        company_list = Transmisia.objects.all()

        serializer_service = TransmisiaSerializer(company_list, many=True)
        return Response({'Transmisia': serializer_service.data})


class LeadList(APIView):
    def get(self, request):
        company_list = Lead.objects.all()
        serializer_service = LeadSerializer(company_list, many=True)
        return Response({'Lead': serializer_service.data})


class SteerableBridgeList(APIView):
    def get(self, request):
        company_list = Steerable_Bridge.objects.all()

        serializer_service = SteerableBridgeSerializer(company_list, many=True)
        return Response({'Steerable_bridge': serializer_service.data})


class ClientList(APIView):
    def get(self, request):
        company_list = Client.objects.all()
        serializer_service = ClientSerializer(company_list, many=True)
        return Response({'Clients': serializer_service.data})



class UpdateMachine(UpdateAPIView):
    queryset = Machine.objects.all()
    serializer_class = AddMachineSerializer


class GroupList(APIView):
    def get(self, request):
        print(request.user)
        permission_class = (IsAuthenticated,)
        group = Group.objects.filter(user=request.user)
        serializer_group = GroupSerializer(group, many=True)
        return Response([{'Group': serializer_group.data}])



class AutoList(ListAPIView):
    serializer_class = MachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MachineFilter
    def get_queryset(self):
        queryset = Machine.objects.filter(client_model__user_id=self.request.user.id)
        return queryset


class ListComplaint(ListAPIView):
    serializer_class = ComplaintSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplaintFilter
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Complaint.objects.filter(car_complaint_id=pk)
        return queryset

class LeadDetail(ListAPIView):
    serializer_class = LeadSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Lead.objects.filter(title=param)
        print(queryset)
        return queryset

class EngineDetail(ListAPIView):
    serializer_class = LeadSerializer
    def get_queryset(self):
        param = self.kwargs['title']

        print(param)
        queryset = Engine.objects.filter(title=param)
        print(queryset)
        return queryset

class TechnicDetail(ListAPIView):
    serializer_class = TechicSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Technica.objects.filter(title=param)
        print(queryset)
        return queryset


class BridgeDetail(ListAPIView):
    serializer_class = SteerableBridgeSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Steerable_Bridge.objects.filter(title=param)
        print(queryset)
        return queryset

class TransmisiaDetail(ListAPIView):
    serializer_class = TransmisiaSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Transmisia.objects.filter(title=param)
        print(queryset)
        return queryset

class ServiceDetail(ListAPIView):
    serializer_class = ServiceSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Service.objects.filter(title=param)
        print(queryset)
        return queryset

class VidDetail(ListAPIView):
    serializer_class = Vidi_TOSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Vidi_TO.objects.filter(title=param)
        print(queryset)
        return queryset

class UselDetail(ListAPIView):
    serializer_class = UselSerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Usel_Refusal.objects.filter(title=param)
        print(queryset)
        return queryset

class RecoveryDetail(ListAPIView):
    serializer_class = RecoverySerializer
    def get_queryset(self):
        param = self.kwargs['title']
        print(param)
        queryset = Recovery.objects.filter(title=param)
        print(queryset)
        return queryset