from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, SignupPage
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', TaskList.as_view(), name='tasks'),
    path('task/<pk>', TaskDetail.as_view(), name='taskdetail'),
    path('task-create/', TaskCreate.as_view(), name='taskcreate'),
    path('task-update/<pk>', TaskUpdate.as_view(), name='taskupdate'),
    path('task-delete/<pk>', TaskDelete.as_view(), name='taskdelete'),

    path('login/', CustomLoginView.as_view(), name='login', ),
    path('logout/', LogoutView.as_view(next_page='tasks'), name='logout', ),
    path('signup/', SignupPage.as_view(), name='signup', ),
]