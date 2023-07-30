from django.urls import path
from . import views
from django.conf.urls.static import static
from todo import settings
app_name="task"

urlpatterns = [
    path('', views.taskdetails,name="task_details"),
    path('delete/<int:slug>/', views.deletetask,name="delete"),
    path('update/<int:slug>/', views.update,name="update"),
    
    
    path('create-view/', views.TodoCreateView.as_view(),name="create_view"),
    path('list-view/', views.TodoListView.as_view(),name="list_view"),
    path('detail-view/<int:pk>/', views.TodoDetailView.as_view(),name="detail_view"),
    path('update-view/<int:pk>/', views.TodoUpdateView.as_view(),name="update_view"),
    path('delete-view/<int:pk>/', views.TodoDeleteView.as_view(),name="delete_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
