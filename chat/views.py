from rest_framework.response import Response
from rest_framework.views import APIView
from .pusher import pusher_client

# Create your views here.
class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message']
        })
        
        # 從 request.data 取得資料
        username = request.data['username']
        message = request.data['message']
        
        return Response(f"{username} 說了 {message}")
