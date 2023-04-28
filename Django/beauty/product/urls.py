
from django.urls import path,include
from product import views

urlpatterns = [
  path('',views.index,name='product'),
  path('about/',views.about,name='product'),
  path('contact/',views.contact,name='contact'),
  path('view/',views.view,name='view'),
  path('add/',views.add,name='product'),
  path('update<str:id>/',views.update,name='update'),
  path('delete<str:id>/',views.delete,name='delete'),
  path('name/',views.name_view,name='name'),
  path('age/',views.age_view,name='age'),
  path('msg/',views.msg_view,name='msg'),
  path('results/',views.results_view,name='results')
]
