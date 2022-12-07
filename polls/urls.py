from django.urls import path

# import relativo
# A partir da pasta onde o arquivo está, import o módulo views
from . import views

urlpatterns = [
    # question_id é um parâmetro passado via URL
    # ou seja, ele pode mudar a qualquer chamado
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]

