from ninja import ModelSchema, Schema
from django.db.models import Q
from .models import Message, Room


class RoomOut(ModelSchema):
    class Meta:
        model = Room
        fields = ["id", "name", "topic", "created_at"]


class RoomIn(Schema):
    name: str
    topic: str = ""


class RoomFilter(Schema):
    search: str = None
    topic: str = None
    recent: bool = False

    def filter(self, queryset):
        if self.search:
            queryset = queryset.filter(
                Q(name__icontains=self.search) |
                Q(topic__icontains=self.search)
            )
        if self.topic:
            queryset = queryset.filter(topic__icontains=self.topic)
        if self.recent:
            queryset = queryset.order_by("-created_at")
        return queryset


class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = ["content"]


class MessageOut(ModelSchema):
    room: RoomOut

    class Meta:
        model = Message
        fields = ["id", "author", "content", "created_at"]


class Conflict(Schema):
    message: str
    existing_id: int
