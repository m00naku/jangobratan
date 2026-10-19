from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),

    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),

    path('students/', views.students_view, name='students'),
    path('student/add/', views.student_add_view, name='student_add'),
    path('student/<int:student_id>/', views.student_detail_view, name='student_detail'),
    path('student/edit/<int:student_id>/', views.student_edit_view, name='student_edit'),
    path('student/delete/<int:student_id>/', views.student_delete_view, name='student_delete'),

    path('groups/', views.groups_view, name='groups'),
    path('group/<int:group_id>/', views.group_detail_view, name='group_detail'),
    path('group/add/', views.group_add_view, name='group_add'),
    path('group/delete/<int:group_id>/', views.group_delete_view, name='group_delete'),
    path('group/edit/<int:group_id>/', views.group_edit_view, name='group_update'),
]