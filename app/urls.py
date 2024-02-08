from django.urls import path,include
from app.views import api_page_list,api_page_post,api_page_detail,api_page_delete,api_page_put,CRUD,MIXS,MIXS_DETAIL
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/crud',CRUD)
router.register('api/mix',MIXS)
router.register('api/detailmix',MIXS_DETAIL)


urlpatterns = [

    path('api/', api_page_list, name='api_page_list'),
    path('api/post', api_page_post, name='api_page_post'),
    path('api/detail/<int:pk>', api_page_detail, name='api_page_detail'),
    path('api/delete/<int:pk>', api_page_delete, name='api_page_delete'),
    path('api/put/<int:pk>', api_page_put, name='api_page_put'),
    path('',include(router.urls)),

]
