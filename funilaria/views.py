from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm,EmpresaForm,OrdemDeServicoForm,MaterialForm,OrcamentoForm,LucrosForm
from django.contrib import messages
from funilaria.models import Cliente,Customer,Empresa,OrdemDeServico,Material,Carrinho,ItemCarrinho,Orcamento
from django.contrib.auth.decorators import login_required
import datetime
from django.db import IntegrityError
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from .models import EstoqueMaximoException 

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
    
    msg=messages.get_messages(request)
    if request.POST.get('cnpj')!=None:
        cnpj=request.POST.get('cnpj')
        empresas = Empresa.objects.filter(cnpj=cnpj).order_by('id')
        return render(request,'busca_empresas.html',context={'empresas':empresas,'msg':msg})
    empresas = Empresa.objects.all().order_by('id')
    return render(request,'empresas.html',context={'empresas':empresas,'msg':msg})

@login_required(login_url='/login/')
def novoempresa(request):
    if request.method == 'POST':
        form_empresa= EmpresaForm(request.POST or None)
        if form_empresa.is_valid():
            try:
                form_empresa.save()
                messages.success(request,'Empresa cadastrada com sucesso')
                return redirect(empresa)
            except IntegrityError as e: 
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
    #igual status
    msg=messages.get_messages(request)
    cpf=request.POST.get('cpf') or None
    try:
        if len(cpf)==15:
            cpf=request.POST.get('cpf') or None
            cnpj=None
        elif len(cpf)==18:
            cpf=None
            cnpj=request.POST.get('cpf') or None
            
        if cpf:
            try:
                cli=Cliente.objects.get(cpf=cpf)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                ordens = OrdemDeServico.objects.filter(cliente=cli)
            except ObjectDoesNotExist as e:
                ordens = []
        elif cnpj:
            try:
                cli=Empresa.objects.get(cnpj=cnpj)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                ordens = OrdemDeServico.objects.filter(cliente=cli)
            except ObjectDoesNotExist as e:
                ordens = []
        else:
            return redirect(ordem_de_servico)
    except:
        ordens = OrdemDeServico.objects.all().order_by('id')
    return render(request,'os.html',context={'ordens':ordens,'msg':msg})

@login_required(login_url='/login/')
def nova_os(request):
    entrada=datetime.date.today().strftime("%d/%m/%Y")
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

@login_required(login_url='/login/')
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
    msg=messages.get_messages(request)
    if request.POST.get('descricao')!=None:
        descricao=request.POST.get('descricao')
        materiais = Material.objects.filter(descricao=descricao).order_by('id')
        return render(request,'busca_materiais.html',context={'materiais':materiais,'msg':msg})
    materiais = Material.objects.all().order_by('id')
    
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
    cpf_cnpj=request.POST.get('cpf-cnpj') or None
    if cpf_cnpj:
        if len(cpf_cnpj)==14:
            cpf=cpf_cnpj
            cnpj=None
        elif len(cpf_cnpj)==18:
            cnpj=cpf_cnpj
            cpf=None
        else:
            messages.error(request,'dados inválidos')
            return redirect(pagina_inicial)

        if cpf:
            try:
                cli=Cliente.objects.get(cpf=cpf)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                ordens = OrdemDeServico.objects.filter(cliente=cli)
            except ObjectDoesNotExist:
                ordens=[]
        elif cnpj:
            try:
                cli=Empresa.objects.get(cnpj=cnpj)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                ordens = OrdemDeServico.objects.filter(cliente=cli)
            except ObjectDoesNotExist:
                ordens=[]
        else:
            return redirect(pagina_inicial)
        return render(request,'status.html',context={'ordens':ordens,'msg':msg})
    return redirect(pagina_inicial)

##################################################################################################################
@login_required(login_url='/login/')
def materiais_orcamento(request):
    materiais = Material.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'materiais.html',context={'materiais':materiais,'msg':msg})

@login_required(login_url='/login/')
def materiais_orcamento_editar(request,id_orcamento):
    orcamento=Orcamento.objects.get(id=id_orcamento)
    materiais = Material.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'materiais_editar_orcamento.html',context={'materiais':materiais,'msg':msg,'orcamento':orcamento})

@login_required(login_url='/login/')
def editar_carrinho(request,id,orcamento_id=None):
    if orcamento_id:
        orcamento=Orcamento.objects.get(id=orcamento_id)
        carrinho=Carrinho.objects.get(id=id)
    else:
        orcamento=None
    return render(request,'editar_carrinho.html',context={'carrinho':carrinho,'orcamento':orcamento})

@login_required(login_url='/login/')
def carrinho(request):
    usuario=request.user
    try:
        carrinho = Carrinho.objects.get(usuario=usuario, finalizado=False)
    except:
        carrinho=None
    return render(request,'carrinho.html',context={'carrinho':carrinho})

def pegarItem(carrinho,material,usuario):
    for i in carrinho.itens.all():
        if i.material==material and i.usuario==usuario:
            return i
    i = ItemCarrinho.objects.create(material=material,usuario=usuario)
    i.adicionar()
    i.save()
    return i


@login_required(login_url='/login/')
def add_no_carrinho_lista_materiais(request, id):
    item = get_object_or_404(Material, id=id)
    m=Material.objects.get(id=id)
    if m.quantidade_estoque>0:
        carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
        if carrinho_qs.exists():
            order = carrinho_qs[0]
            item_carrinho=pegarItem(order,m,request.user)
            # verifica se o item ja está no carrinho
            if order.itens.filter(material__id=item.id).exists():
                try:
                    item_carrinho.adicionar()
                    item_carrinho.save()
                    messages.info(request, "Quantidade atualizada")
                    return redirect(carrinho)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect(material)
            else:
                #item_carrinho.adicionar()
                try:
                    order.itens.add(item_carrinho)
                    messages.info(request, "Material adicionado ao carrinho")
                    return redirect(carrinho)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect(material)
        else:
            carrinho_obj = Carrinho.objects.create(usuario=request.user)
            item_carrinho = ItemCarrinho.objects.create(material=m,usuario=request.user)
            try:
                item_carrinho.adicionar()
                carrinho_obj.itens.add(item_carrinho)
                messages.info(request, "Material adicionado ao carrinho")
                return redirect(carrinho)
            except EstoqueMaximoException:
                messages.error(request, "Material indisponível")
            return redirect(material)
    else:
        messages.error(request, "Material indisponível") 
        return redirect(material)

@login_required(login_url='/login/')
def add_no_carrinho_(request, id):
    item = get_object_or_404(Material, id=id)
    m=Material.objects.get(id=id)
    if m.quantidade_estoque>0:
        carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
        if carrinho_qs.exists():
            order = carrinho_qs[0]
            item_carrinho=pegarItem(order,m,request.user)
            # verifica se o item ja está no carrinho
            if order.itens.filter(material__id=item.id).exists():
                try:
                    item_carrinho.adicionar()
                    item_carrinho.save()
                    messages.info(request, "Quantidade atualizada")
                    return redirect(carrinho)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect(materiais_orcamento)
            else:
                try:
                    item_carrinho.adicionar()
                    order.itens.add(item_carrinho)
                    messages.info(request, "Material adicionado ao carrinho")
                    return redirect(carrinho)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect(materiais_orcamento)
        else:
            carrinho_obj = Carrinho.objects.create(usuario=request.user)
            try:
                item_carrinho.adicionar()
                carrinho_obj.itens.add(item_carrinho) 
                messages.info(request, "Material adicionado ao carrinho")
                return redirect(carrinho)
            except EstoqueMaximoException:
                messages.error(request, "Material indisponível")
            return redirect(materiais_orcamento)
    else:
        messages.error(request, "Material indisponível")
        return redirect(materiais_orcamento)


@login_required(login_url='/login/')
def add_no_editar_carrinho(request, id_material, id_carrinho, orcamento_id):
    item = get_object_or_404(Material, id=id_material)
    orcamento=Orcamento.objects.get(id=orcamento_id)
    m=Material.objects.get(id=id_material)
    if m.quantidade_estoque>0:
        carrinho_qs = Carrinho.objects.filter(id=id_carrinho)
        if carrinho_qs.exists():
            order = carrinho_qs[0]
            item_carrinho=pegarItem(order,m,request.user)
            if order.itens.filter(material__id=item.id).exists():
                try:
                    item_carrinho.adicionar()
                    item_carrinho.save()
                    messages.info(request, "Quantidade atualizada")
                    return redirect('editar_carrinho', id=order.id, orcamento_id=orcamento.id)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)
            else:
                try:
                    #item_carrinho.adicionar()
                    order.itens.add(item_carrinho)
                    messages.info(request, "Material adicionado ao carrinho")
                    return redirect('editar_carrinho', id=order.id, orcamento_id=orcamento.id)
                except EstoqueMaximoException:
                    messages.error(request, "Material indisponível")
                return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)
        else:
            carrinho_obj = Carrinho.objects.create(usuario=request.user)
            item_carrinho=pegarItem(order,m,request.user)
            try:
                carrinho_obj.itens.add(item_carrinho)
                item_carrinho.adicionar()
                messages.info(request, "Material adicionado ao carrinho")
                return redirect('editar_carrinho', id=order.id, orcamento_id=orcamento.id)
            except EstoqueMaximoException:
                messages.error(request, "Material indisponível")
            return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)
    else:
        messages.error(request, "Material indisponível")
        return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)

@login_required(login_url='/login/')
def remover_do_carrinho(request, id_material, id_carrinho):
    item = get_object_or_404(Material, id=id_material)
    carrinho_qs = Carrinho.objects.filter(id=id_carrinho)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        item_carrinho=pegarItem(order,item,request.user)
        if order.itens.filter(material__id=item.id).exists():
            for i in range(item_carrinho.quantidade):
                item_carrinho.remover()
            order.itens.remove(item_carrinho)
            messages.info(request, "Material removido do carrinho")
        else:
            messages.error(request, "Material não faz parte do carrinho")
        return redirect(materiais_orcamento)
    else:
        messages.error(request, "Nenhum carrinho encontrado")
        return redirect(materiais_orcamento)

@login_required(login_url='/login/')
def remover_do_editar_carrinho(request, id_material, id_carrinho, orcamento_id):
    item = get_object_or_404(Material, id=id_material)
    carrinho_qs = Carrinho.objects.filter(id=id_carrinho)
    orcamento=Orcamento.objects.get(id=orcamento_id)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        item_carrinho=pegarItem(order,item,request.user)
        if order.itens.filter(material__id=item.id).exists():
            for i in range(item_carrinho.quantidade):
                item_carrinho.remover()
            order.itens.remove(item_carrinho)
            messages.info(request, "Material removido do carrinho")
        else:
            messages.error(request, "Material não faz parte do carrinho")
        return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)
    else:
        messages.error(request, "Nenhum carrinho encontrado")
        return redirect('materiais_orcamento_editar',id_orcamento=orcamento.id)

@login_required(login_url='/login/')
def tirar_do_carrinho(request, id):
    item = get_object_or_404(Material, id=id)
    carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        # verifica se o item ja está na carrinho
        if order.itens.filter(material__id=item.id).exists():
            item_carrinho = pegarItem(order,m,request.user)
            if item_carrinho.quantidade > 1:
                item_carrinho.remover()
                item_carrinho.save()
                messages.info(request, "Quantidade atualizada")
            else:
                item_carrinho.remover()
                order.itens.remove(item_carrinho)
                messages.info(request, "Material removido da carrinho")
            return redirect(materiais_orcamento)
        else:
            messages.error(request, "Material não faz parte do carrinho")
            return redirect(materiais_orcamento)
    else:
        messages.error(request, "Nenhum carrinho encontrado")
        return redirect(materiais_orcamento)

@login_required(login_url='/login/')
def tirar_do_carrinho_(request, id):
    item = get_object_or_404(Material, id=id)
    carrinho_qs = Carrinho.objects.filter(usuario=request.user,finalizado=False)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        if order.itens.filter(material__id=item.id).exists():
            item_carrinho = pegarItem(order,item,request.user)
            if item_carrinho.quantidade > 1:
                item_carrinho.remover()
                item_carrinho.save()
                messages.info(request, "Quantidade atualizada")
            else:
                item_carrinho.remover()
                order.itens.remove(item_carrinho)
                messages.info(request, "Material removido do carrinho")
            return redirect(carrinho)
        else:
            messages.error(request, "Material não faz parte do carrinho")
            return redirect(materiais_orcamento)
    else:
        messages.error(request, "Nenhum carrinho encontrado")
        return redirect(materiais_orcamento)


@login_required(login_url='/login/')
def tirar_do_editar_carrinho(request, id_material, id_carrinho, orcamento_id):
    item = get_object_or_404(Material, id=id_material)
    orcamento=Orcamento.objects.get(id=orcamento_id)
    m=Material.objects.get(id=id_material)
    carrinho_qs = Carrinho.objects.filter(id=id_carrinho)
    if carrinho_qs.exists():
        order = carrinho_qs[0]
        item_carrinho = pegarItem(order,item,request.user)
        # verifica se o item ja está na carrinho
        if order.itens.filter(material__id=item.id).exists():
            #item_carrinho = ItemCarrinho.objects.filter(material=item,usuario=request.user).first()
            if item_carrinho.quantidade > 1:
                item_carrinho.remover()
                item_carrinho.save()
                messages.info(request, "Quantidade atualizada")
            else:
                item_carrinho.remover()
                order.itens.remove(item_carrinho)
                messages.info(request, "Material removido do carrinho")
            return redirect('editar_carrinho', id=order.id, orcamento_id=orcamento.id)
        else:
            messages.error(request, "Material não faz parte do carrinho")
            return redirect(materiais_orcamento)
    else:
        messages.error(request, "Nenhum carrinho encontrado")
        return redirect(materiais_orcamento)

@login_required(login_url='/login/')
def orcamento(request):
    msg=messages.get_messages(request)
    cpf_cnpj=request.POST.get('cpf-cnpj') or None
    if cpf_cnpj:
        if len(cpf_cnpj)==14:
            cpf=cpf_cnpj
            cnpj=None
        elif len(cpf_cnpj)==18:
            cnpj=cpf_cnpj
            cpf=None
        else:
            messages.error(request,'dados inválidos')
            return redirect(orcamento)

        if cpf:
            try:
                cli=Cliente.objects.get(cpf=cpf)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                orcamentos = Orcamento.objects.filter(ordem_de_servico__cliente__id=cli.id)
            except ObjectDoesNotExist:
                orcamentos=[]
        elif cnpj:
            try:
                cli=Empresa.objects.get(cnpj=cnpj)
                cli=Customer.objects.get(nome=cli.nome,endereco=cli.endereco,bairro=cli.bairro,
                email=cli.email,telefone=cli.telefone)
                orcamentos = Orcamento.objects.filter(ordem_de_servico__cliente__id=cli.id)
            except ObjectDoesNotExist:
                orcamentos=[]
        return render(request,'orcamentos.html',context={'orcamentos':orcamentos,'msg':msg})
    else:
        orcamentos=Orcamento.objects.all()
        return render(request,'orcamentos.html',context={'orcamentos':orcamentos,'msg':msg})

@login_required(login_url='/login/')
def novo_orcamento(request):
    try:
        carrinho = Carrinho.objects.get(usuario=request.user,finalizado=False)
    except ObjectDoesNotExist:
            carrinho =Carrinho.objects.create(usuario=request.user,finalizado=False)
    if request.method == 'POST':
        form_orcamento= OrcamentoForm(request.POST,initial={'carrinho':carrinho.id})
        if form_orcamento.is_valid():
            try:
                carrinho.finalizado=True
                form_orcamento.finalizado=True
                carrinho.save()
                form_orcamento.save()
                messages.success(request,'Orçamento cadastrado com sucesso')
                return redirect(orcamento)
            except Exception as e:
                messages.error(request,e)
        else:
            return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'carrinho':carrinho})
    else:
        form_orcamento= OrcamentoForm(initial={'carrinho':carrinho.id})
    return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'carrinho':carrinho})

    

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
    return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'instance':instance})

@login_required(login_url='/login/')
def editar_carrinho_do_orcamento(request,id=None,carrinho_id=None):
    instance = get_object_or_404(Orcamento,id=id)
    if carrinho_id:
        carrinho=carrinho.objects.get(id=carrinho_id)
        instance.carrinho=carrinho
    else:
        carrinho=None
    form_orcamento= OrcamentoForm(request.POST or None, instance=instance)
    if form_orcamento.is_valid():
        try:
            instance=form_orcamento.save()
            instance.save()
            messages.success(request,'Orçamento atualizado com sucesso')
            return redirect(orcamento)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_orcamento.html',context={'form_orcamento':form_orcamento,'instance':instance,'carrinho':carrinho})

@login_required(login_url='/login/')
def deletar_orcamento(request,id=None):
    instance = get_object_or_404(Orcamento,id=id)
    try:
        instance.delete()
        messages.success(request,'Orçamento deletado com sucesso')
    except Exception as e:
        messages.error(request,'Não foi possível deletar o Orçamento')
    return redirect(orcamento) 

def pegarOrcamentosfinalizados():
    o=[]
    for i in Orcamento.objects.all():
        if i.status:
            o.append(i)
    return o


@login_required(login_url='/login/')
def lucros(request):
    form = LucrosForm()
    data_inicial=request.GET.get('data_inicial') or None
    data_final=request.GET.get('data_final') or None
    if data_inicial and data_final:
        data_inicial=datetime.datetime.strptime(data_inicial, "%d/%m/%Y").date()
        data_final=datetime.datetime.strptime(data_final, "%d/%m/%Y").date()
        orc=pegarOrcamentosfinalizados()

        total_gasto=0
        mao_de_obra=0
        for i in orc:
            if i.data_saida >= data_inicial and i.data_saida<=data_final:
                #gasto com materiais
                total_gasto+=i.carrinho.total
                #valor mao de obra
                mao_de_obra+=i.valor_mao_de_obra

        return render(request,'lucros.html',context={'form':form,'total_gasto':total_gasto,
                            'mao_de_obra':mao_de_obra,
                            'total_orcamento':total_gasto+mao_de_obra,
                            'lucros':mao_de_obra-total_gasto
                            })
    else:
        form = LucrosForm()
        return render(request,'lucros.html',context={'form':form,'total_gasto':0,
                            'mao_de_obra':0,
                            'total_orcamento':0,
                            'lucros':0})
##################################################################################################################