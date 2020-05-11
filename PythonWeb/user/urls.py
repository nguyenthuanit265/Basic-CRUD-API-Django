from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views_api, views
from django.conf.urls import url

urlpatterns = [
    # path('basic/', views_api.API_objects.as_view()),
    # path('basic/<int:pk>/', views_api.API_objects_details.as_view()),
    path('show', views.show),
    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),

    # # url(
    # #     r'^api/v03/view/$',
    # #     views_api.get_post_employee,
    # #     name='get_post_employee'
    # # ),
    #
    # url(
    #     r'^api/v01/user',
    #     views_api.get_all,
    #     name='get_all_user'
    # ),
    # url(
    #     r'^api/v01/user/add/$',
    #     views_api.add,
    #     name='add_user'
    # ),
    # # url(
    # #     r'^api/v01/user/edit/(?P<pk>[0-9]+)$',
    # #     views_api.get_edit,
    # #     name='get_edit_user'
    # # ),
    # path('api/v01/user/edit/<int:id>',views_api.get_update_edit),
    # # url(
    # #     r'^api/v01/user/update',
    # #     views_api.update,
    # #     name='get_all_user'
    # # ),
    # #
    # # url(
    # #     r'^api/v01/user/delete/(?P<pk>[0-9]+)$',
    # #     views_api.deleteById,
    # #     name='delete_user'
    # # ),
    #
    # url(
    #     r'^api/v02/user/(?P<pk>[0-9]+)$',
    #     views_api.get_delete_update_employee,
    #     name='get_delete_update_employee'
    # ),
    # url(
    #     r'^api/v02/user/$',
    #     views_api.get_post_employee,
    #     name='get_post_employee'
    # )
]
urlpatterns = format_suffix_patterns(urlpatterns)
