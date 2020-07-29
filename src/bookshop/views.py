from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView)
from bookshop.serializer import EventSerializer
from bookshop.models import Event, CHOICE_DELTA
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from logging import getLogger
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

logger = getLogger('django')

class ListEvent(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user_event=self.request.user)

class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def create(self, request):
        test = EventSerializer(data=request.data)
        if test.is_valid():
            test.save(user_event=request.user)
        return Response('Done')

class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user_event=self.request.user)

class GetEvent(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request,date):
        date = date.split('-')
        response = {}
        if len (date) == 1:
            response = Event.objects.filter(
                Q(date_stop__year=date[0])).order_by('date_stop')
        elif len(date) == 2:
            response = Event.objects.filter(
            Q(date_stop__year=date[0]) & Q(date_stop__month=date[1])).order_by('date_stop')
        elif len(date) == 3:
            response = Event.objects.filter(
                Q(date_stop__year=date[0]) & Q(date_stop__month=date[1]) & Q(date_stop__day=date[2])).order_by('date_stop')
        serializer = EventSerializer(response,many=True)
        return Response (serializer.data)

class Sign(APIView):
    def post(self,request):
        user = authenticate(
            request,
            username = request.data["username"],
            password = request.data["password"]
        )
        if user is None:
            user = User.objects.create(
                username=request.data["username"],
                email=request.data["email"],
                password=request.data["password"]
            )
        token = Token.objects.get_or_create(user=user)

class GetToken(APIView):
    def post(self,request):
        user = authenticate(
            request,
            username = request.data["username"],
            password = request.data["password"]
        )
        user = User.objects.get_or_create(
            username=request.data["username"],
            email=request.data["email"],
            password=request.data["password"]
        )
        token = Token.objects.get_or_create(user=user[0])
        send_mail(
            "this is your token",
            f"token: {token[0].key}",
            "siarheibazyliuk@gmail.com",
            [request.data["email"]],
            fail_silently=True
        )

        return Response("please receive your token")
