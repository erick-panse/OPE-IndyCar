function confirmarAcao(){
    let confirmacao = confirm('Os dados excluidos não podem ser recuperados\nDeseja continuar ?');
    if (!confirmacao){
        event.preventDefault();
    }
}

$(document).ready(function(){
    $('.date').mask('00/00/0000');
    $('#cpf').mask('000.000.000-00', {reverse: true});
    $('#cpfPGinicial').mask('000.000.000-00', {reverse: true});
    $('#cpfListaCliente').mask('000.000.000-00', {reverse: true});
    $('#cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('#placa').mask('SSS-0000');
    $('.money').mask('000.000.000,00');
    var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
    },
      spOptions = {
        onKeyPress: function(val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
        }
    };
    $('#tel').mask(SPMaskBehavior, spOptions);
    
});
function MontaPesquisa() {

    if ($("#cnpj").val() != "")
        resultado = ({ "cnpj": $("#cnpj").val().replace(/[^\d]+/g,'') });
    else
        return
    };


function calcularTotal(){
    let mao_de_obra = document.getElementById('valor_mao_de_obra').value;
    let carrinho = document.getElementById('carrinho_total').value;

    if (mao_de_obra == '' || mao_de_obra == null){
        mao_de_obra=0;
    }
    if (carrinho == '' || carrinho == null){
        carrinho=0;
    }

    let total = document.getElementById('total_a_pagar');
    total.value=parseFloat(mao_de_obra)+parseFloat(carrinho);
}

function validar_material(){
    let descricao = document.getElementById('descricao').value;
    let qtd_estoque = document.getElementById('quantidade_estoque').value;
    let valor = document.getElementById('valor').value;

    if(descricao == ""){
        alert("Preencha o campo Descrição.");
        descricao.focus();
        return false;
    }

    if(qtd_estoque == ""){
        alert("Preencha o campo Quantidade em estoque.");
        qtd_estoque.focus();
        return false;
    }

    if(valor == ""){
        alert("Preencha o campo Valor.");
        valor.focus();
        return false;
    }
}

function validar_cliente(){
    let nome = document.getElementById('nome').value;
    let cpf = document.getElementById('cpf').value;
    let endereco = document.getElementById('endereco').value;
    let bairro = document.getElementById('bairro').value;
    let email = document.getElementById('email').value;
    let telefone = document.getElementById('tel').value;

    if(nome == ""){
        alert("Preencha o campo Nome.");
        valor.focus();
        return false;
    }

    if(cpf == "" || cpf.length <= 10){
        alert("Preencha o campo CPF corretamente.");
        cpf.focus();
        return false;
    }

    if(endereco == ""){
        alert("Preencha o campo Endereço.");
        endereco.focus();
        return false;
    }

    if(bairro == ""){
        alert("Preencha o campo Bairro.");
        bairro.focus();
        return false;
    }

    if(email == "" || email.indexOf('@')  == -1){
        alert("Preencha o campo Email corretamente.");
        email.focus();
        return false;
    }

    if(telefone == "" || telefone.length < 10){
        alert("Preencha o campo telefone corretamente.");
        telefone.focus();
        return false;
    }

}

function validar_empresa(){
    let nome = document.getElementById('nome').value;
    let cnpj = document.getElementById('cnpj').value;
    let endereco = document.getElementById('endereco').value;
    let bairro = document.getElementById('bairro').value;
    let email = document.getElementById('email').value;
    let telefone = document.getElementById('tel').value;

    if(nome == ""){
        alert("Preencha o campo Nome.");
        valor.focus();
        return false;
    }

    if(cnpj == "" || cnpj.length <= 13){
        alert("Preencha o campo CNPJ corretamente.");
        cnpj.focus();
        return false;
    }

    if(endereco == ""){
        alert("Preencha o campo Endereço.");
        endereco.focus();
        return false;
    }

    if(bairro == ""){
        alert("Preencha o campo Bairro.");
        bairro.focus();
        return false;
    }

    if(email == "" || email.indexOf('@')  == -1){
        alert("Preencha o campo Email corretamente.");
        email.focus();
        return false;
    }

    if(telefone == "" || telefone.length < 10){
        alert("Preencha o campo telefone corretamente.");
        telefone.focus();
        return false;
    }

}

function validar_ordem(){
    let marca = document.getElementById('marca').value;
    let modelo = document.getElementById('modelo').value;
    let cor = document.getElementById('cor').value;
    let placa = document.getElementById('placa').value;
    let ano = document.getElementById('ano').value;
    let cidade = document.getElementById('cidade').value;
    let reparo_OS = document.getElementById('inputReparo').value;
    let prazo_entrega = document.getElementById('prazo_entrega').value;
    let data_finalizacao = document.getElementById('data_finalizacao').value;

    if(marca == ""){
        alert("Preencha o campo marca.");
        marca.focus();
        return false;
    }

    if(modelo == ""){
        alert("Preencha o campo Modelo.");
        modelo.focus();
        return false;
    }

    if(cor == ""){
        alert("Preencha o campo Cor.");
        cor.focus();
        return false;
    }

    if(placa == "" || placa.length <= 6){
        alert("Preencha o campo Placa corretamente.");
        placa.focus();
        return false;
    }

    if(ano == ""){
        alert("Preencha o campo Ano.");
        ano.focus();
        return false;
    }

    if(cidade == ""){
        alert("Preencha o campo Cidade.");
        cidade.focus();
        return false;
    }

    if(reparo_OS == ""){
        alert("Preencha o campo Reparos necessários.");
        reparo_OS.focus();
        return false;
    }

    if(prazo_entrega == ""){
        alert("Preencha o campo Prazo de entrega.");
        prazo_entrega.focus();
        return false;
    }

    if(data_finalizacao == ""){
        alert("Preencha o campo Data de finalização.");
        data_finalizacao.focus();
        return false;
    }
    
}

function validar_orcamento(){
    let servicos = document.getElementById('servicos').value;
    let mao_de_obra = document.getElementById('valor_mao_de_obra').value;
    let previsao_entrega = document.getElementById('previsao_entrega').value;

    if(servicos == ""){
        alert("Preencha o campo Serviços necessários.");
        servicos.focus();
        return false;
    }

    if(mao_de_obra == ""){
        alert("Preencha o campo Valor de mão de obra.");
        smao_de_obra.focus();
        return false;
    }

    if(previsao_entrega == ""){
        alert("Preencha o campo Previsão de entrega.");
        previsao_entrega.focus();
        return false;
    }

}