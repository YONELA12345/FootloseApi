from rest_framework.authtoken.models import Token  # Asegúrate de importar Token desde DRF
from django.db.models           import Q

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
import json, random, hashlib
from rest_framework.views import APIView
from apps.users.models import Staff, StaffRole
from apps.users.serializers import onget_role_serializer, onget_staff_serializer, role_serializer, staff_serializer
# Create your views here.
class auth_login_viewset(ObtainAuthToken):
    authentication_classes=[]
    permission_classes=[]

    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                return Response({'error': 'Missing username or password'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not user.check_password(password):
            return Response(status=status.HTTP_204_NO_CONTENT)

        token, created = Token.objects.get_or_create(user=user)
        token.delete()

        token.key = token.generate_key()
        token.save()

        response = {
            'id': user.id,
            'token': token.key,
            'type': 'staff' if user.is_staff else 'client'
        }

        if user.is_staff:
            try:
                response.update({
                    "staff":onget_staff_serializer(
                        Staff.objects.get(user=user.id),
                    ).data
                })
            except Staff.DoesNotExist:
                pass

        return Response(response)



class auth_register_staff_viewset(ObtainAuthToken):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    authentication_classes=[]
    permission_classes=[]

    def post(self, request, *args, **kwargs):
        if (len(User.objects.filter(username=request.data['username']))>0):
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            user=User(
                username=request.data['username'],
                password=request.data['password'],
                is_staff=True
            )
            user.set_password(request.data['password'])
            user.save()

            print("Se guardo")

            serializer=staff_serializer(
                data=request.data,
                context={
                    'user':user,
                    "role":request.data['role'],
                }
            )

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                user.delete()
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
class party_role_viewset(APIView):

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    authentication_classes=[]
    permission_classes=[]

    def get(self, request):
        f = Q()
        if 'role' in request.GET:
            f &= Q(pk = request.GET['role'])
        return Response(
            onget_role_serializer(
                StaffRole.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

    def post(self, request):
        serializer = role_serializer(
            data=request.data,
        )

        print(request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        role = StaffRole.objects.get(id=request.data["id"])
        serializer = role_serializer(
            role,
            data=request.data,
            
        )

        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        role = StaffRole.objects.get(id=request.data["id"])
        role.deleted = not role.deleted
        role.save(update_fields=['deleted'])

        return Response(status=status.HTTP_202_ACCEPTED)

class party_staff_viewset(APIView):

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    authentication_classes=[]
    permission_classes=[]

    def get(self, request):
        f = Q()
        if 'staff' in request.GET:
            f &= Q(pk = request.GET['staff'])
        return Response(
            onget_staff_serializer(
                Staff.objects.filter(f).order_by('-id'),
                many = True
            ).data
        )

    def post(self, request):
        serializer = role_serializer(
            data=request.data,
        )

        print(request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        role = StaffRole.objects.get(id=request.data["id"])
        serializer = role_serializer(
            role,
            data=request.data,
            
        )

        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        role = StaffRole.objects.get(id=request.data["id"])
        role.deleted = not role.deleted
        role.save(update_fields=['deleted'])

        return Response(status=status.HTTP_202_ACCEPTED)