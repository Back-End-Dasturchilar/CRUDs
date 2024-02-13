from django.shortcuts import render, get_object_or_404
from .models import Post
from rest_framework import status, generics, mixins
from .serializers import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

# API_VIEW
# @api_view(http_method_names=['GET'])
# def get(request: Request):
#     a = Post.objects.all()
#     serializer = PostSerializers(a, many=True)
#     response = {"message": "Get all posts succesfully", "data": serializer.data}
#     return Response(data=response, status=status.HTTP_200_OK)
#
#
# @api_view(http_method_names=["POST"])
# def post(request: Request):
#     data = request.data
#     serializer = PostSerializers(data=data)
#     if serializer.is_valid():
#          serializer.save()
#          response = {"message": "New post created succesfuly", "data": serializer.data}
#          return Response(data=response, status=status.HTTP_201_CREATED)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['PUT'])
# def put(request: Request, pk: int):
#     post = get_object_or_404(Post, pk=pk)
#     data = request.data
#     serializer = PostSerializers(instance=post, data=data)
#     if serializer.is_valid():
#             serializer.save()
#             response = {"message": "Updated succesfuly", "data": serializer.data}
#             return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["DELETE"])
# def delete(request: Request, pk: int):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     response = {"message": "Post deleted"}
#     return Response(data=response, status=status.HTTP_204_NO_CONTENT)
#
#
# Generics
# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
#
# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
#
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
#
# class PostDestroyAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
# MIXIN
# class BooksListCreateAPIView(generics.GenericAPIView,
#                              mixins.ListModelMixin,
#                              mixins.CreateModelMixin):
#     serializer_class = PostSerializers
#     queryset = Post.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, *kwargs)
#
#
# class BooksUpdateRetrieveDestroyAPIView(generics.GenericAPIView,
#                                         mixins.RetrieveModelMixin,
#                                         mixins.UpdateModelMixin,
#                                         mixins.DestroyModelMixin):
#     serializer_class = PostSerializers
#     queryset = Post.objects.all()
#
#     def retrieve(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def destroy(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# 

