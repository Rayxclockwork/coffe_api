from django.urls import path
from .views import EntryList, EntryDetail, EntryCreateView, EntryUpdateView, EntryDeleteView

urlpatterns = [
	path('', EntryList.as_view(), name = 'home'),
	path('detail/<int:pk>/', EntryDetail.as_view(), name = 'detail'),
	path('book/new/', EntryCreateView.as_view(), name='add'),
    path('update/<int:pk>', EntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EntryDeleteView.as_view(), name='delete')
]