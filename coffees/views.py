from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EntryList(ListView):
	model = Post


	def get(self, request):
		posts = Post.objects.all()
		print(posts)
		return HttpResponse(posts)
		

class EntryDetail(DetailView):
	queryset = Post.objects.all()


class EntryCreateView(CreateView):
    model = Post
    fields = ['Name', 'Body', 'Author']

class EntryUpdateView(UpdateView):
    model = Post
    fields = ['Name', 'Body', 'Author']

class EntryDeleteView(DeleteView):
	model = Post
	success_url = reverse_lazy('home')

class AuthView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		return Response()
