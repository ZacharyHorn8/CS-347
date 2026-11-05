# chat/schemas.py
from ninja import ModelSchema
from .models import Message, Room

class RoomOut(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "name", "topic", "created_at"]

class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = ["content"]

