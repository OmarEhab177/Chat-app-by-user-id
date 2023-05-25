import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        self.other_user_id = self.scope["url_route"]["kwargs"]["other_user_id"]

        sorted_user_ids = sorted([self.user_id, self.other_user_id])
        self.room_group_name = f"chat_{sorted_user_ids[0]}_{sorted_user_ids[1]}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message')
        if message:
            # Send the message to the room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'user_id': str(self.user_id)
                }
            )

    async def chat_message(self, event):
        message = event['message']
        sender_user_id = event['user_id']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_id': sender_user_id
        }))
