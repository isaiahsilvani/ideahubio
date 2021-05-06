from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_idea', views.IdeaCreate.as_view(), name='create_idea'),
    path('accounts/signup/', views.signup, name='signup'),
    path('ideas/', views.IdeaList.as_view(), name='list_ideas'),
    path('ideas/<int:idea_id>', views.ideas_detail, name='detail'),
    path('ideas/delete/<int:pk>', views.IdeaDelete.as_view(), name='idea_delete'),
    #PASSWORD RESET URLS
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

