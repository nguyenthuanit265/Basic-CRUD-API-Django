from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views_api, views
from django.conf.urls import url

urlpatterns = [
    path('v01/get-all', views_api.get_all),
    path('v01/add', views_api.add),
    path('v01/edit/<int:id>', views_api.get_by_id),
    path('v01/update/<int:id>', views_api.get_update_edit),
    path('v01/delete/<int:id>', views_api.delete_by_id),

    # path('v01/edit/<int:id>', views_api.get_edit),
    # url(
    #     r'^api/v03/view/$',
    #     views_api.get_post_employee,
    #     name='get_post_employee'
    # ),

    # url(
    #     r'^api/v01/user',
    #     views_api.getAll,
    #     name='get_all_user'
    # ),
    # url(
    #     r'^api/v01/user/add/$',
    #     views_api.add,
    #     name='add_user'
    # ),
    # url(
    #     r'^api/v01/user/edit/(?P<pk>[0-9]+)$',
    #     views_api.get_edit,
    #     name='get_edit_user'
    # ),

    # url(
    #     r'^api/v01/user/update',
    #     views_api.update,
    #     name='get_all_user'
    # ),
    #
    # url(
    #     r'^api/v01/user/delete/(?P<pk>[0-9]+)$',
    #     views_api.deleteById,
    #     name='delete_user'
    # ),

    url(
        r'^api/v02/user/(?P<pk>[0-9]+)$',
        views_api.get_delete_update_employee,
        name='get_delete_update_employee'
    ),
    # url(
    #     r'^api/v02/user/$',
    #     views_api.get_post_employee,
    #     name='get_post_employee'
    # )
]
urlpatterns = format_suffix_patterns(urlpatterns)
