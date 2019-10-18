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
    $('.money').mask('000000.00', {reverse: true});
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
        $('#descricao').css({'border':'1px solid red'});
        return false;
    }

    if(qtd_estoque == ""){
        $('#quantidade_estoque').css({'border':'1px solid red'});
        return false;
    }

    if(valor == ""){
        $('#valor').css({'border':'1px solid red'});
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
        $('#nome').css({'border':'1px solid red'});
        return false;
    }

    if(cpf == "" || cpf.length <= 10){
        $('#cpf').css({'border':'1px solid red'});
        return false;;
    }

    if(endereco == ""){
        $('#endereco').css({'border':'1px solid red'});
        return false;
    }

    if(bairro == ""){
        $('#bairro').css({'border':'1px solid red'});
        return false;
    }

    if(email == "" || email.indexOf('@')  == -1){
        $('#email').css({'border':'1px solid red'});
        return false;
    }

    if(telefone == "" || telefone.length < 10){
        $('#tel').css({'border':'1px solid red'});
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
        $('#nome').css({'border':'1px solid red'});
        return false;
    }

    if(cnpj == "" || cnpj.length <= 13){
        $('#cnpj').css({'border':'1px solid red'});
        return false;
    }

    if(endereco == ""){
        $('#endereco').css({'border':'1px solid red'});
        return false;
    }

    if(bairro == ""){
        $('#bairro').css({'border':'1px solid red'});
        return false;
    }

    if(email == "" || email.indexOf('@')  == -1){
        $('#email').css({'border':'1px solid red'});
        return false;
    }

    if(telefone == "" || telefone.length < 10){
        $('#tel').css({'border':'1px solid red'});
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

    if(marca == ""){
        $('#marca').css({'border':'1px solid red'});
        return false;
    }

    if(modelo == ""){
        $('#modelo').css({'border':'1px solid red'});
        return false;
    }

    if(cor == ""){
        $('#cor').css({'border':'1px solid red'});
        return false;
    }

    if(placa == "" || placa.length <= 6){
        $('#placa').css({'border':'1px solid red'});
        return false;
    }

    if(ano == ""){
        $('#ano').css({'border':'1px solid red'});
        return false;
    }

    if(cidade == ""){
        $('#cidade').css({'border':'1px solid red'});
        return false;
    }

    if(reparo_OS == ""){
        $('#inputReparo').css({'border':'1px solid red'});
        return false;
    }

    if(prazo_entrega == ""){
        alert("Digite um Prazo de entrega válido.")
        return false;
    }
    
}

function validar_orcamento(){
    let servicos = document.getElementById('servicos').value;
    let mao_de_obra = document.getElementById('valor_mao_de_obra').value;
    let previsao_entrega = document.getElementById('previsao_entrega').value;

    if(servicos == ""){
        $('#servicos').css({'border':'1px solid red'});
        return false;
    }

    if(mao_de_obra == ""){
        alert("Digite um valor de mão de obra.")
        mao_de_obra.focus();
        return false;
    }

    if(previsao_entrega == ""){
        alert("Digite um Prazo de entrega válido.")
        return false;
    }

}

//Cadastrar Empresas e Pessoas

function validarNome() {
    var x = document.getElementById("nome");
    $('#nome').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarCPF() {
    var x = document.getElementById("cpf");
    $('#cpf').css({'border':'1px solid #A9A9A9'});
    return true;
    
} 

function validarCNPJ() {
    var x = document.getElementById("cnpj");
    $('#cnpj').css({'border':'1px solid #A9A9A9'});
    return true;
    
} 

function validarEndereco() {
    var x = document.getElementById("endereco");
    $('#endereco').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarBairro() {
    var x = document.getElementById("bairro");
    $('#bairro').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarEmail() {
    var x = document.getElementById("email");
    $('#email').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarTelefone() {
    var x = document.getElementById("tel");
    $('#tel').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

// Cadastrar Ordem de serviço

function validarMarca() {
    var x = document.getElementById("marca");
    $('#marca').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarModelo() {
    var x = document.getElementById("modelo");
    $('#modelo').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarCor() {
    var x = document.getElementById("cor");
    $('#cor').css({'border':'1px solid #A9A9A9'});
    return true;

}

function validarPlaca() {
    var x = document.getElementById("placa");
    $('#placa').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarAno() {
    var x = document.getElementById("ano");
    $('#ano').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarCidade() {
    var x = document.getElementById("cidade");
    $('#cidade').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarReparoOS() {
    var x = document.getElementById("inputReparo");
    $('#inputReparo').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

// Cadastrar material

function validarDescricao() {
    var x = document.getElementById("descricao");
    $('#descricao').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarQTDestoque() {
    var x = document.getElementById("quantidade_estoque");
    $('#quantidade_estoque').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

function validarValor() {
    var x = document.getElementById("valor");
    $('#valor').css({'border':'1px solid #A9A9A9'});
    return true;
    
}

// Cadastrar Orçamento

function validarServicos() {
    var x = document.getElementById("servicos");
    $('#servicos').css({'border':'1px solid #A9A9A9'});
    return true;
    
}


// FORMULÁRIOS DE USUÁRIO 



//Novo usuário


function validarNovoUsuario(){
    let username = document.getElementById('userUsuarioForm').value;
    let nome = document.getElementById('nomeUsuarioForm').value;
    let sobrenome = document.getElementById('sobrenomeUsuarioForm').value;
    let email = document.getElementById('emailUsuarioForm').value;
    let password1 = document.getElementById('password1UsuarioForm').value;
    let password2 = document.getElementById('password2UsuarioForm').value;
    
    
    if(username == ""){
        $('#userUsuarioForm').css({'border':'1px solid red'});
        return false;
    }

    if(nome == ""){
        $('#nomeUsuarioForm').css({'border':'1px solid red'});
        return false;
    }

    if(sobrenome == ""){
        $('#sobrenomeUsuarioForm').css({'border':'1px solid red'});
        return false;
    }

    if(email == ""){
        $('#emailUsuarioForm').css({'border':'1px solid red'});
        return false;
    }

    if(password1 == ""){
        $('#password1UsuarioForm').css({'border':'1px solid red'});
        return false;
    }

    if(password2 == ""){
        $('#password2UsuarioForm').css({'border':'1px solid red'});
        return false;
    }

}

function validarUserUsuarioForm(){
    var x = document.getElementById("userUsuarioForm");
    $('#userUsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarNomeUsuarioForm(){
    var x = document.getElementById("nomeUsuarioForm");
    $('#nomeUsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarSobrenomeUsuarioForm(){
    var x = document.getElementById("sobrenomeUsuarioForm");
    $('#sobrenomeUsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarEmailUsuarioForm(){
    var x = document.getElementById("emailUsuarioForm");
    $('#emailUsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarPassword1UsuarioForm(){
    var x = document.getElementById("password1UsuarioForm");
    $('#password1UsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarPassword2UsuarioForm(){
    var x = document.getElementById("password2UsuarioForm");
    $('#password2UsuarioForm').css({'border':'1px solid #A9A9A9'});
    return true;
}

// Editar usuário

function validarEditarUsuario(){
    let nome = document.getElementById('userNomeEditar').value;
    let sobrenome = document.getElementById('userSobrenomeEditar').value;
    let email = document.getElementById('userEmailEditar').value;

    if(nome == ""){
        $('#userNomeEditar').css({'border':'1px solid red'});
        return false;
    }

    if(sobrenome == ""){
        $('#userSobrenomeEditar').css({'border':'1px solid red'});
        return false;
    }

    if(email == ""){
        $('#userEmailEditar').css({'border':'1px solid red'});
        return false;
    }
}

function validarNomeEditar(){
    var x = document.getElementById("userNomeEditar");
    $('#userNomeEditar').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarSobrenomeEditar(){
    var x = document.getElementById("userSobrenomeEditar");
    $('#userSobrenomeEditar').css({'border':'1px solid #A9A9A9'});
    return true;
}

function validarEmailEditar(){
    var x = document.getElementById("userEmailEditar");
    $('#userEmailEditar').css({'border':'1px solid #A9A9A9'});
    return true;
}