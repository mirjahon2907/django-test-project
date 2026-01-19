from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'projects'

router = DefaultRouter()
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('',include(router.urls) , name="reviews"),
    path('skills/',Skills.as_view() , name="skills"),
    path('skills/<int:pk>', SkillDetail.as_view(), name="skill_detail"),
    path('profiles/', Profiles.as_view(), name="profile"),
    path('profiles/<int:pk>', ProfileDetail.as_view(), name="profile_detail"),
    path('tags/', Tags.as_view(), name="tags"),
    path('tags/<int:pk>', TagDetail.as_view(), name="tag_detail"),
    path('messages/', Messages.as_view(), name="messsages"),
    path('messages/<int:pk>', MessageDetail.as_view(), name="message_detail"),
    # path('users/create_user', create_user, name="create_user"),
    # path('users/<str:username>', get_user, name="user_messages"),
    # path('users/<str:username>/got', user_got_messages, name="user_got_messages"),
    # path('users/<str:username>/sent', user_sent_messages, name="user_sent_messages"),
]