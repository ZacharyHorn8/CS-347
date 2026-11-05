# chat/schemas.py
class MessageIn(ModelSchema):
    class Meta:
        model = Message
        fields = ["content"]


class MessageOut(ModelSchema):
    room: RoomOut

    class Meta:
        model = Message
        fields = ["id", "author", "content", "created_at"]

