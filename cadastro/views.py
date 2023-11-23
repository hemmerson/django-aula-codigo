from django.shortcuts import render, redirect, get_object_or_404
from .models import PessoaFisica, PessoaJuridica
from .forms import PessoaJuridicaForm

def index(request):
    return render(request, "index.html")

def pf_lista(request):
    pessoas_fisicas = PessoaFisica.objects.all()
    return render(request, "pf_list.html", {'listapessoafisica': pessoas_fisicas})

def pf_form(request):
    return render(request, "pf_form.html", {'pessoa_fisica': ''})

def pf_novo(request):
    rNome = request.POST.get("nome")
    rEmail = request.POST.get("email")
    rCpf = request.POST.get("cpf")
    rData_nascimento = request.POST.get("data_nascimento")
    PessoaFisica.objects.create(nome = rNome, email = rEmail, cpf = rCpf, data_nascimento = rData_nascimento)
    return redirect(pf_lista)

def pf_editar(request, id):
    pessoa_fisica = PessoaFisica.objects.get(id = id)
    return render(request, "pf_form.html", {'pessoa_fisica':pessoa_fisica})

def pf_update(request, id):
    pessoa = PessoaFisica.objects.get(id = id)
    pessoa.nome = request.POST.get("nome")
    pessoa.email = request.POST.get("email")
    pessoa.cpf = request.POST.get("cpf")
    pessoa.data_nascimento = request.POST.get("data_nascimento")
    pessoa.save()
    return redirect(pf_lista)

def pf_delete(request, id):
    pessoa = PessoaFisica.objects.get(id = id)
    pessoa.delete()
    return redirect(pf_lista)

#========================= Pessoa Jurídica ================================

def listaPessoaJuridica(request):
    listaPJ = PessoaJuridica.objects.all()
    return render(request, 'pj_list.html', {'listapessoajuridica': listaPJ})

def novoPessoaJuridica(request):
    if request.method == 'POST':
        form = PessoaJuridicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaJuridica)
    
    else:
        form = PessoaJuridicaForm()
    return render(request, 'pj_form.html', {'form':form})

def updatePessoaJuridica(request, id):
    pessoaJuridica = get_object_or_404(PessoaJuridica, id = id)

    if request.method == 'POST':
        form = PessoaJuridicaForm(request.POST, instance=pessoaJuridica)
        if form.is_valid():
            form.save()
            return redirect(listaPessoaJuridica)
    else:
        form = PessoaJuridicaForm(instance=pessoaJuridica)
    
    return render(request, 'pj_form.html', {'form':form, 'pessoa_juridica':pessoaJuridica})

def deletePessoaJuridica(request, id):
    pessoaJuridica = get_object_or_404(PessoaJuridica, id = id)

    if request.method == 'POST':
        pessoaJuridica.delete()
        return redirect(listaPessoaJuridica)
    
    return render(request, 'pj_confirm_delete.html', {'pessoa_juridica':pessoaJuridica})
