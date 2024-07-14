from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TextData

@api_view(['POST'])
def save_text(request):
    # 요청에서 'content' 데이터를 가져옴
    content = request.data.get('content')
    if content:
        # 새로운 TextData 객체를 생성하고 저장
        text_data = TextData.objects.create(content=content)
        return Response({'message': '텍스트가 저장되었습니다.'})
    return Response({'error': '내용이 비어있습니다.'})

@api_view(['GET'])
def get_latest_text(request):
    # 가장 최근에 저장된 텍스트를 가져옴
    latest_text = TextData.objects.last()
    if latest_text:
        return Response({'content': latest_text.content})
    return Response({'message': '저장된 텍스트가 없습니다.'})