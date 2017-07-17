from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Entity, Human, Object, Room, Door

# class Pose(models.Model)
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_name',
                  'x1', 'x2', 'x3', 'x4',
                  'y1', 'y2', 'y3', 'y4'
                  )


class DoorSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    class Meta:
        model = Door
        fields = ('id', 'room', 'x', 'y')


class EntitySerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    def create(self, validated_data):
        return Entity.objects.create(**validated_data)
    def update(self, entity, validated_data):
        entity.name = validated_data.get('name', entity.name)
        entity.room = validated_data.get('room', entity.room)
        entity.x = validated_data.get('x', entity.x)
        entity.y = validated_data.get('y', entity.y)
        entity.z = validated_data.get('z', entity.z)

        entity.save()
        return entity

    class Meta:
        model = Entity
        fields = ('id', 'name', 'room', 'time', 'x', 'y','z')


class EntityInRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('id', 'name', 'x', 'y','z')


class HumanSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)
    class Meta:
        model = Human
        fields = ('id', 'entity', 'gender', 'operator')

# class HumanEntitySerializer(serializers.ModelSerializer):
#     entity = EntitySerializer(read_only=True)
#     class Meta:
#         model = Human
#         fields = ('id', 'entity.name')

class ObjectSerializer(serializers.ModelSerializer):
    entity = EntitySerializer(read_only=True)
    class Meta:
        model = Object
        fields = ('id', 'entity', 'categorie', 'probabilty')
