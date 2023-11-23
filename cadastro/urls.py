from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoa_fisica/lista/', views.pf_lista, name='lista_pessoa_fisica'),
    path('pessoa_fisica/form/', views.pf_form, name='novo_form_pessoa_fisica'),
    path('pessoa_fisica/novo/', views.pf_novo, name='novo_pessoa_fisica'),
    path('pessoa_fisica/editar/<int:id>/', views.pf_editar, name='editar_pessoa_fisica'),
    path('pessoa_fisica/update/<int:id>/', views.pf_update, name='update_pessoa_fisica'),
    path('pessoa_fisica/delete/<int:id>/', views.pf_delete, name='delete_pessoa_fisica'),

    path('pessoa_juridica/lista/', views.listaPessoaJuridica, name='lista_pessoa_juridica'),
    path('pessoa_juridica/novo/', views.novoPessoaJuridica, name='novo_pessoa_juridica'),
    path('pessoa_juridica/update/<int:id>/', views.updatePessoaJuridica, name='update_pessoa_juridica'),
    path('pessoa_juridica/delete/<int:id>/', views.deletePessoaJuridica, name='delete_pessoa_juridica'),
]