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
    path('ideas/update/<int:pk>', views.IdeaUpdate.as_view(), name='idea_update'),
    path('public/', views.public_list, name='list_public'),
    path('ideas/makepublic/<int:idea_id>', views.make_public, name='make_public'),
    path('ideas/makeprivate/<int:idea_id>', views.make_private, name='make_private'),
    path('ideas/<int:idea_id>/add_photo/', views.add_photo, name='add_photo'),
    path('ideas/<int:idea_id>/add_logo', views.add_logo, name='add_logo'),
    path('ideas/<int:idea_id>/remove_logo/', views.delete_logo, name='remove_logo'),
    path('ideas/<int:photo_id>/<int:idea_id>/delete_photo/', views.delete_photo, name='delete_photo'),
    path('ideas/<int:idea_id>/add_employee/', views.add_employee, name='add_employee'),
    path('ideas/<int:idea_id>/<int:employee_id>/delete_employee/', views.delete_employee, name='delete_employee'),
    path('ideas/<int:pk>/update_employee/', views.UpdateEmployee.as_view(), name='update_employee'),
    path('ideas/<int:employee_id>/update_employee_done/', views.update_employee_done, name='update_employee_done'),
    path('ideas/<int:idea_id>/like_idea', views.like_idea, name='like_idea'),
    path('ideas/<int:idea_id>/unlike_idea', views.unlike_idea, name='unlike_idea'),
    #PASSWORD RESET URLS
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Chatroom URLS
    path('chat/', views.chatindex, name='chatindex'),
    path('chat/<str:room_name>/', views.room, name='room'),
]

