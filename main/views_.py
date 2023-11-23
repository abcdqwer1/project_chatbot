from rest_framework import viewsets
from .models import Message
from .models import Conversation
from .serializers import MessageSerializer
from .serializers import ConversationSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ChatbotViewSet(viewsets.ViewSet):
    def create(self, request):
        user_input = request.data.get('user_input', '')
        # GPT 응답 받는기능 추가 필요.
        response_content = f"ChatGPT: {user_input}"
        
        # 대화를 저장
        conversation = Conversation.objects.create(user='ChatGPT', content=response_content)
        serializer = ConversationSerializer(conversation)

        return Response(serializer.data)

# class ChatbotView(View):
#     def get(self, request, *args, **kwargs):
#         conversations = request.session.get('conversations', [])
#         return render(request, 'chat.html', {'conversations': conversations})

#     def post(self, request, *args, **kwargs):
#         prompt = request.POST.get('prompt')
#         if prompt:
#             # 이전 대화 기록 가져오기
#             session_conversations = request.session.get('conversations', [])
#             previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
#             prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

#             model_engine = "text-davinci-003"
#             completions = openai.Completion.create(
#                 engine=model_engine,
#                 prompt=prompt_with_previous,
#                 max_tokens=1024,
#                 n=5,
#                 stop=None,
#                 temperature=0.5,
#             )
#             response = completions.choices[0].text.strip()

#             conversation = {'prompt': prompt, 'response': response}

#             # 대화 기록에 새로운 응답 추가
#             session_conversations.append(conversation)
#             request.session['conversations'] = session_conversations

#         return self.get(request, *args, **kwargs)