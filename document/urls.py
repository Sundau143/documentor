from django.contrib.auth import views as auth_views
from document import views
from django.urls import path, include

urlpatterns = [
    path('document/', views.documents_view, name='document_list'),
    path('document/create/', views.create_document, name='create_document'),
    path('remove_document/<int:document_id>/', views.remove_document, name='remove_document'),
    path('edit_document/<int:document_id>/', views.edit_document, name='edit_document'),
    path('document/<int:document_id>/', views.view_document, name='view_document'),
    path('tinymce/', include('tinymce.urls')),
    path('document/<int:document_id>/create_comment/', views.create_comment, name='create_comment'),
    #path('document/<int:document_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]