from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics
from apex.models import Notepad
from .serializer import Noteserializer ,Userserializer ,Loginserializer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.contrib.auth.views import LoginView
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate


class CreateNote(generics.CreateAPIView):
    queryset =Notepad.objects.all()
    serializer_class =Noteserializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
class ListNote(generics.ListAPIView):
   queryset =Notepad.objects.all()
   serializer_class =Noteserializer

listnote =ListNote.as_view()
class Notedetails(generics.RetrieveAPIView):
    queryset =Notepad.objects.all()
    serializer_class =Noteserializer
    lookup_field = 'pk'
notedetails =Notedetails.as_view()
class UdateNote(generics.UpdateAPIView):
    queryset =Notepad.objects.all()
    serializer_class =Noteserializer
 

    def perform_update(self, serializer):
        return super().perform_update(serializer)
updatenote  = UdateNote.as_view()

class DeleteNote(generics.DestroyAPIView):
    queryset =Notepad.objects.all()
    serializer_class =Noteserializer
    lookup_field ='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
delete =DeleteNote.as_view()

class signup(generics.CreateAPIView):
    queryset =User.objects.all()
    serializer_class =Userserializer

    def perform_create(self, serializer):
        username =serializer.validated_data.get('username')
        email =serializer.validated_data.get('email')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error':'username already exist'},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error':'email already exist'},status=status.HTTP_400_BAD_REQUEST)
        return super().perform_create(serializer)
class login(GenericAPIView):
    serializer_class =Loginserializer

    def post(self,request):
        serializer =self.get_serializer(data =request.data)
        serializer.is_valid(raise_exception =True)
        username =serializer.validated_data['username']
        password =serializer.validated_data['password']
        user  = authenticate(username=username,password=password)
        if user:
           return JsonResponse({"message":"login successfully"},status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)