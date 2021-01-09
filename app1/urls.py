from django.urls import path
from . import views
from .views import list_view,update_view,delete_view,detail_view,SignUp


urlpatterns = [
    
    #to add path use path function having arguments as path name of view
    #to make webpage dynamic use <> in path argument to include all the objects
    # path('app1/<int:post_id>/', view4),
    # path('app1/<str:str_id>/', view5),
    
    path('', list_view,name="all_blogs"),
    #path('/<str:slug>/', view6),
    path('<str:slug>/edit/', update_view),
    path('<int:id>/delete/', delete_view),
    path('<str:slug>/details/', detail_view),
 	path('signup/', views.SignUp.as_view(), name='signup'),


]
