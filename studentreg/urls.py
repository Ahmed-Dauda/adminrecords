
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.home, name = 'home'),
    path('edit/<int:post_id>/', views.edit_view, name = 'edit'),
    path('delete/<int:delete_id>/', views.delete_view, name = 'delete'),
    path('signin', views.signin_view, name = 'signin'),
    path('prep', views.prep_view, name = 'prep'),
    path('editprep/<int:post_id>/', views.editprep_view, name = 'editprep'),
    path('deleteprep/<int:delete_id>/', views.deleteprep_view, name = 'deleteprep'),
    path('add', views.add_view, name = 'add'),
    #path('editall/<int:post_id>/', views.editall_view, name = 'editall'),
    path('pdf', views.generatepdf, name = 'generatepdf'),
    path('gen', views.generate, name = 'generate'),
    path('pdf_id/', views.render_pdf_view_id, name = 'pdf_id'),
    path('pdf_render/<int:pk>/', views.salat_render_pfd, name = 'pdf_render'),
    

]
