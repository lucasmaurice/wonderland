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
        name = query_params.get('name', None)

        if name is not None:
            entity = Entity.objects.filter(name=name)
            serializer = EntitySerializer(entity, many=True)
            return Response(serializer.data)

        entity = Entity.objects.all()
        serializer = EntitySerializer(entity, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HumanList(APIView):
    ''' List all Human. '''

    def get(self, request, format=None):
        humans =        serializer = EntitySerializer(data=request.data)
        address = request.data
        print(address)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = HumanSerializer(humans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        entSerializer = EntitySerializer(data=request.data)
        if entSerializer.is_valid():
            entSerializer.save()

            # print("ID: ", entSerializer.data['id'])
            # print("REQUEST: ", request)

            entity = Entity.objects.get(id=entSerializer.data['id'])
            # print("Entity: ", entity)

            gender = ""
            operator = False

            if 'gender' in request.data:
                gender = request.data['gender']
            if 'operator' in request.data:
                operator = request.data['operator']

            try:
                human = Human(  entity=entity,
                                gender=gender,
                                operator=operator)
                human.save()
            except:
                return Response("Error while creating human", status=status.HTTP_400_BAD_REQUEST)

            return Response("Human "+entity.name+" as been created", status=status.HTTP_201_CREATED)
        return Response(entSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OperatorList(APIView):
    ''' Get the operator position. '''

    def get(self, request, format=None):
        operators = Human.objects.filter(operator=True)
        if operators is not None:
            serializer = HumanSerializer(operators, many=True)
            return Response(serializer.data)
        return Response('No operators found', status=status.HTTP_404_NOT_FOUND)

class ObjectList(APIView):
    ''' List all Object. '''

    def get(self, request, format=None):
        objects = Object.objects.all()
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        entSerializer = EntitySerializer(data=request.data)
        if entSerializer.is_valid():
            entSerializer.save()
            entity = Entity.objects.get(id=entSerializer.data['id'])

            categorie = ""
            probability = 0

            if 'categorie' in request.data:
                categorie = request.data['categorie']
            if 'probability' in request.data:
                probability = request.data['probability']

            try:
                obj = Object(   entity=entity,
                                categorie=categorie,
                                probability=probability)
                obj.save()
            except:
                return Response("Error while creating object", status=status.HTTP_400_BAD_REQUEST)

            return Response("object "+entity.name+" as been created", status=status.HTTP_201_CREATED)
        return Response(entSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
