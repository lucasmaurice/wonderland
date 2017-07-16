from datetime import datetime
# import manage as main

from api.models import Entity, Room, Human, Object
from api.serializers import EntitySerializer, HumanSerializer
from api.serializers import ObjectSerializer, RoomSerializer
from api.serializers import EntityInRoomSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

class EntityList(APIView):
    ''' List all Entity or create a new entity. '''

    def get(self, request, format=None):
        query_params = self.request.query_params
        entity = query_params.get('entity', None)

        if str(entity) == 'human':
            humans = Human.objects.all()
            serializer = HumanSerializer(humans, many=True)
            return Response(serializer.data)
        if str(entity) == 'object':
            objects = Object.objects.all()
            serializer = ObjectSerializer(objects, many=True)
            return Response(serializer.data)

        entities = Entity.objects.all()
        serializer = EntitySerializer(entities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EntitySerializer(data=request.data)
        address = request.data
        print(address)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HumanList(APIView):
    ''' List all Human. '''

    def get(self, request, format=None):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObjectList(APIView):
    ''' List all Object. '''

    def get(self, request, format=None):
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomList(APIView):
    '''
    List all Room.
    '''
    def get(self, request, format=None):
        query_params = self.request.query_params
        name = query_params.get('name', None)
        if name is not None:
            print("Room name: ",name)
            room = Room.objects.filter(room_name=name)
            if room is not None:
                entity = Entity.objects.filter(room=room)
                serializer = EntityInRoomSerializer(entity, many=True)
                return Response(serializer.data)
            return Response("No Room found", status=status.HTTP_404_NOT_FOUND)

        print("Room name: none")


        rooms = Room.objects.all()
        serializers = RoomSerializer(rooms, many=True)
        return Response(serializers.data)
