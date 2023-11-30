from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Conversation
from .serializers import ConversationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from drf_spectacular.utils import extend_schema
from dotenv import load_dotenv
from openai import OpenAI
import openai
import os

load_dotenv()
# openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  
)

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    @extend_schema(
        request=ConversationSerializer,
        responses={200: ConversationSerializer},
        description='chatbot 대화기능',)
    @action(detail=False, methods=['post'])
    def chatbot(self, request):
        prompt = request.data.get('prompt')

        if prompt:
            # 이전 대화 기록 가져오기
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            # model_engine = "text-davinci-003"
            completion = client.completions.create(
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
                # model="gpt-3.5-turbo",
                model="text-davinci-003",
            )
            response = completion.choices[0].text.strip()

            conversation = {'user': 'ChatGPT', 'content': response}
            serializer = ConversationSerializer(data=conversation)

            if serializer.is_valid():
                serializer.save()
                # 대화 기록에 새로운 응답 추가
                session_conversations.append({'prompt': prompt, 'response': response})
                request.session['conversations'] = session_conversations
                request.session.modified = True
                return Response(serializer.data, status=201)

            return Response(serializer.errors, status=400)

        return Response({'error': 'Prompt is required'}, status=400)
