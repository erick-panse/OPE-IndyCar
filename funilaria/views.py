from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm,EmpresaForm,OrdemDeServicoForm,MaterialForm,OrcamentoForm
from django.contrib import messages
from funilaria.models import Cliente,Customer,Empresa,OrdemDeServico,Material,Carrinho,ItemCarrinho,Orcamento
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db import IntegrityError
from django import forms

# Create your views here.
#comentado pra n ficar obrigatorio
def pagina_inicial(request):
    return render(request, 'pagina-inicial.html')

def index(request):
    return render(request, 'index.html')

def quemsomos(request):
    return render(request, 'quemsomos.html')

@login_required(login_url='/login/')
def index (request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def cliente(request):
    msg=messages.get_messages(request)
    if request.POST.get('cpf')!=None:
        cpf=request.POST.get('cpf')
        clientes = Cliente.objects.filter(cpf=cpf).order_by('id')
        return render(request,'busca_clientes.html',context={'clientes':clientes,'msg':msg})
    clientes = Cliente.objects.all().order_by('id')
    return render(request,'clientes.html',context={'clientes':clientes,'msg':msg})

@login_required(login_url='/login/')
def novocliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST or None)
        if form_cliente.is_valid():
            try:
                form_cliente.save()
                messages.success(request,'Cliente cadastrado com sucesso')
            except IntegrityError as e: 
                print('UNIQUE constraint' in str(e.args))
                if 'UNIQUE constraint' in str(e.args): 
                    messages.error(request,'Cliente já cadastrado')
                    return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})
            except Exception as e:
                messages.error(request,e)
            return redirect(cliente)
        else:
            for i in form_cliente.non_field_errors():
                messages.error(request,i)
            return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})
    else:
        form_cliente = ClienteForm()
        return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})

@login_required(login_url='/login/')
def editar_cliente(request,id=None):
    instance_cliente = get_object_or_404(Cliente,id=id)
    form_cliente = ClienteForm(request.POST or None, instance= instance_cliente)
    if form_cliente.is_valid():
        try:
            instance_cliente=form_cliente.save(commit=False)
            instance_cliente.save()
            messages.success(request,'Cliente atualizado com sucesso')
            return redirect(cliente)
        except IntegrityError as e: 
            print('UNIQUE constraint' in str(e.args))
            if 'UNIQUE constraint' in str(e.args): 
                messages.error(request,'Cliente já cadastrado')
                return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente})
        except Exception as e:
            print(e)
            
    for i in form_cliente.non_field_errors():
        messages.error(request,i)
    return render(request,'formulario_cliente.html',context={'form_cliente':form_cliente,'instance_cliente':instance_cliente})

@login_required(login_url='/login/')
def deletar_cliente(request,id=None):
    instance = get_object_or_404(Cliente,id=id)
    try:
        instance.delete()
        messages.success(request,'Cliente deletado com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar o cliente')
    return redirect(cliente)

@login_required(login_url='/login/')
def empresa(request):
    empresas = Empresa.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'empresas.html',context={'empresas':empresas,'msg':msg})

@login_required(login_url='/login/')
def novoempresa(request):
    if request.method == 'POST':
        form_empresa= EmpresaForm(request.POST or None)
        print(form_empresa.is_valid())
        if form_empresa.is_valid():
            try:
                form_empresa.save()
                messages.success(request,'Empresa cadastrada com sucesso')
                return redirect(empresa)
            except IntegrityError as e: 
                print('UNIQUE constraint' in str(e.args))
                if 'UNIQUE constraint' in str(e.args): 
                    messages.error(request,'Empresa já cadastrada')
                    return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})
            except Exception as e:
                messages.error(request,e)
                return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})
        else:
            return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})
    else:
        form_empresa= EmpresaForm()
        return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})

@login_required(login_url='/login/')
def editar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    form_empresa= EmpresaForm(request.POST or None, instance= instance)
    if form_empresa.is_valid():
        try:
            instance=form_empresa.save()
            instance.save()
            messages.success(request,'Empresa atualizada com sucesso')
            return redirect(empresa)
        except IntegrityError as e: 
            print('UNIQUE constraint' in str(e.args))
            if 'UNIQUE constraint' in str(e.args): 
                messages.error(request,'Empresa já cadastrada')
                return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa})
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_empresa.html',context={'form_empresa':form_empresa,'instance':instance})

@login_required(login_url='/login/')
def deletar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    try:
        instance.delete()
        messages.success(request,'Empresa deletada com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar a empresa')
    return redirect(empresa)

@login_required(login_url='/login/')
def ordem_de_servico(request):
    ordens = OrdemDeServico.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'os.html',context={'ordens':ordens,'msg':msg})

@login_required(login_url='/login/')
def nova_os(request):
    #testando a consulta entre datas
    start_date = date(2011, 4, 1)
    end_date = date.today()
    print(OrdemDeServico.objects.filter(data_finalizacao__range=(start_date,end_date)))
    #testando a consulta entre datas
    entrada=date.today().strftime("%d/%m/%Y")
    if request.method == 'POST':
        form_os= OrdemDeServicoForm(request.POST or None)
        if form_os.is_valid():
            try:
                form_os.save()
                messages.success(request,'Ordem de serviço cadastrada com sucesso')
                return redirect(ordem_de_servico)
            except Exception as e:
                messages.error(request,e)
                return render(request,'formulario_os.html',context={'form_os':form_os,'entrada':entrada})
        else:
            return render(request,'formulario_os.html',context={'form_os':form_os,'entrada':entrada})
    else:
        form_os= OrdemDeServicoForm()
        return render(request,'formulario_os.html',context={'form_os':form_os,'entrada':entrada})


def editar_os(request,id=None):
    instance = get_object_or_404(OrdemDeServico,id=id) 
    form_os= OrdemDeServicoForm(request.POST or None, instance=instance)
    cliente = form_os.instance.cliente
    entrada=instance.entrada.strftime("%d/%m/%Y") if instance else None
    if form_os.is_valid():
        try:
            instance=form_os.save()
            instance.save()
            messages.success(request,'Ordem de Serviço atualizada com sucesso')
            return redirect(ordem_de_servico)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_os.html',context={'form_os':form_os,'instance':instance,'cliente':cliente,'entrada':entrada})

@login_required(login_url='/login/')
def deletar_os(request,id=None):
    instance = get_object_or_404(OrdemDeServico,id=id)
    try:
        instance.delete()
        messages.success(request,'Ordem  de Serviço deletada com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar a Ordem de Serviço')
    return redirect(ordem_de_servico)

@login_required(login_url='/login/')
def material(request):
    materiais = Material.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'materiais.html',context={'materiais':materiais,'msg':msg})

@login_required(login_url='/login/')
def novo_material(request):
    if request.method == 'POST':
        form_material= MaterialForm(request.POST or None)
        if form_material.is_valid():
            try:
                form_material.save()
                messages.success(request,'Material cadastrado com sucesso')
                return redirect(material)
            except Exception as e:
                messages.error(request,e)
        else:
            return render(request,'formulario_material.html',context={'form_material':form_material})
    else:
        form_material= MaterialForm()
        return render(request,'formulario_material.html',context={'form_material':form_material})

@login_required(login_url='/login/')
def editar_material(request,id=None):
    instance = get_object_or_404(Material,id=id)
    form_material= MaterialForm(request.POST or None, instance= instance)
    if form_material.is_valid():
        try:
            instance=form_material.save()
            instance.save()
            messages.success(request,'Material atualizado com sucesso')
            return redirect(material)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_material.html',context={'form_material':form_material,'instance':instance})

@login_required(login_url='/login/')
def deletar_material(request,id=None):
    instance = get_object_or_404(Material,id=id)
    try:
        instance.delete()
        messages.success(request,'Material deletado com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar o material')
    return redirect(material)

def status_ordem(request):
    msg=messages.get_messages(request)
    cpf=request.POST.get('cpf') or None
    #pelo jeito colocar Empresa exclui as empresas
    clientes = Cliente.objects.filter(cpf=cpf).order_by('id')
    print(clientes[0])
    print(OrdemDeServico.objects.all()[0].cliente)
    print(clientes[0]==OrdemDeServico.objects.all()[0].cliente)
    ordens=[]
    return render(request,'busca_ordens.html',context={'ordens':ordens,'msg':msg})


##################################################################################################################
def carrinho(request):
    usuario=request.user
    carrinho = Carrinho.objects.get(usuario=usuario, finalizado=False)
    return render(request,'carrinho.html',context={'carrinho':carrinho})

def add_no_carrinho(request, id):
    print('add')
    item = get_object_or_404(Material, id=id)
    item_carrinho, created = ItemCarrinho.objects.get_or_create(material=item,usuario=request.user)
    carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        # verifica se o item ja está no carrinho
        if order.itens.filter(material__id=item.id).exists():
            item_carrinho.quantidade += 1
            item_carrinho.save()
            messages.info(request, "Quantidade atualizada +1")
            return redirect(carrinho)
        else:
            order.itens.add(item_carrinho)
            messages.info(request, "Material adicionado a carrinho")
            return redirect(carrinho)
    else:
        order = Carrinho.objects.create(usuario=request.user)
        order.itens.add(item_carrinho)
        messages.info(request, "Material adicionado a carrinho")
        return redirect(carrinho)

def remover_do_carrinho(request, id):
    print('out')
    item = get_object_or_404(Material, id=id)
    carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        # verifica se o item ja está na carrinho
        if order.itens.filter(material__id=item.id).exists():
            item_carrinho = ItemCarrinho.objects.filter(material=item,usuario=request.user).first()
            order.itens.remove(item_carrinho)
            messages.info(request, "Material removido da carrinho")
            return redirect(carrinho)
        else:
            messages.info(request, "Material não faz parte da carrinho")
            return redirect(carrinho)
    else:
        messages.info(request, "Nenhuma carrinho encontrada")
        return redirect(carrinho)

def tirar_do_carrinho(request, id):
    print('-1')
    item = get_object_or_404(Material, id=id)
    carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        # verifica se o item ja está na carrinho
        if order.itens.filter(material__id=item.id).exists():
            item_carrinho = ItemCarrinho.objects.filter(material=item,usuario=request.user).first()
            if item_carrinho.quantidade > 1:
                item_carrinho.quantidade -= 1
                item_carrinho.save()
                messages.info(request, "Quantidade atualizada -1")
            else:
                print('removido')
                order.itens.remove(item_carrinho)
                messages.info(request, "Material removido da carrinho")
            return redirect(carrinho)
        else:
            messages.info(request, "Material não faz parte da carrinho")
            return redirect(carrinho)
    else:
        messages.info(request, "Nenhuma carrinho encontrada")
        return redirect(carrinho)

@login_required(login_url='/login/')
def orcamento(request):
    orcamentos = Orcamento.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'orcamentos.html',context={'orcamentos':orcamentos,'msg':msg})

@login_required(login_url='/login/')
def novo_orcamento(request):
    try:
        carrinho = Carrinho.objects.get(usuario=request.user,finalizado=False)
        if request.method == 'POST':
            print('POST')
            form_orcamento= OrcamentoForm(request.POST,initial={'carrinho':carrinho.id,'usuario':request.user.id})
            print(form_orcamento.is_valid())
            if form_orcamento.is_valid():
                try:
                    carrinho.finalizado=True
                    form_orcamento.finalizado=True
                    carrinho.save()
                    form_orcamento.save()
                    messages.success(request,'Orçamento cadastrado com sucesso')
                    return redirect(orcamento)
                except Exception as e:
                    print(e)
                    messages.error(request,e)
            else:
                print(form_orcamento.errors)
                print(form_orcamento.non_field_errors)
                return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'carrinho':carrinho})
        else:
            form_orcamento= OrcamentoForm(initial={'carrinho':carrinho.id,'usuario':request.user.id})
            print('GET')
        return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'carrinho':carrinho})
    except Exception as e:
        messages.error(request,e)
        return redirect(material) 
    

@login_required(login_url='/login/')
def editar_orcamento(request,id=None):
    instance = get_object_or_404(Orcamento,id=id)
    form_orcamento= OrcamentoForm(request.POST or None, instance=instance)
    if form_orcamento.is_valid():
        try:
            instance=form_orcamento.save()
            instance.save()
            messages.success(request,'Orçamento atualizado com sucesso')
            return redirect(orcamento)
        except Exception as e:
            messages.error(request,e)
    print(instance.resumo)
    return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'instance':instance})

@login_required(login_url='/login/')
def deletar_orcamento(request,id=None):
    instance = get_object_or_404(Orcamento,id=id)
    try:
        instance.delete()
        messages.success(request,'Orçamento deletado com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar o Orçamento')
    return redirect(orcamento) 
##################################################################################################################