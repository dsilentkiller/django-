from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import message, send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permission_classes =(permissions.AllowAny)

    def post(self,request, format =None):
        data = self.request.data

        try:
            send_mail(
                data['location'],
                'Name:'
                +data['name']
                +'\nEmail:'
                +data['email']
                +'\n\nland_area:\n'
                +data['land_area'],
                '[YOUR SENDER EMAIL FROM YOUR SETTINGS]',
                ['[EMAIL YOU ARE SENDING TO]'],
                fail_silently=False
            )

            contact = Contact(name =data['name'],email=data['email'],land_area=data['land_area'],location=data['location'], price=data['price'])
            contact.save()
            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'message failed to send'})

