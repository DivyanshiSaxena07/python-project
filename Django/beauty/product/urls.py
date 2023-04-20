
from django.urls import path,include
from product import views

urlpatterns = [
  path('',views.index,name='product'),
  path('about/',views.about,name='product'),
  path('contact/',views.contact,name='contact'),
  path('view/',views.view,name='view'),
  path('add/',views.add,name='product'),
  path('update<str:id>/',views.update,name='update'),
  path('delete<str:id>/',views.delete,name='delete')
]
