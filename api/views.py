from django.shortcuts import redirect
from rest_framework import generics, mixins
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(status.HTTP_400_BAD_REQUEST)


class ArticleGenericView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin
    ):
    
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)   # uses mixins.RetrievModelMixin
        else:
            return self.list(request)   # uses mixins.ListModelMixin
    
    def post(self, request):
        return self.create(request) and redirect('/')   # uses mixins.CreateModelMixin, post/submit and redirect to homepage.
    
    def put(self, request, id=None):
        return self.update(request, id)     # uses mixins.UpdateModelMixin
    
    def delete(self, request, id):
        return self.destroy(request, id)    # uses mixins.DestroyModelMixin
    