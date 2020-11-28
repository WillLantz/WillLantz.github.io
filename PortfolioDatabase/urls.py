from django.urls import path
from . import views


app_name = 'portfoliodatabase'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('hobbydetail/<int:item_id>', views.hobbydetail, name="hobbydetail"),
    path('portfoliodetail/<int:port_id>', views.portfoliodetail, name="portfoliodetail"),
    path('portadd', views.add_port, name="add_port"),
    path('portupdate/<int:id>', views.update_port, name="update_port"),
    path('delete/<int:id>', views.delete_port, name="port_delete"),
]
