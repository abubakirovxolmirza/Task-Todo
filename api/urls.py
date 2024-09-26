from django.urls import path
from api.views.users import RegisterUserView, CustomTokenObtainPairView
from api.views.todo import TodoListCreateView, TodoDetailView
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    #Todo
    
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]


