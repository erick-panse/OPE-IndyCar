function confirmarAcao(){
    let confirmacao = confirm('Os dados excluidos não podem ser recuperados\nDeseja continuar ?');
    if (!confirmacao){
        event.preventDefault();
    }
}

$(document).ready(function(){
    $('.date').mask('00/00/0000');
    $('#previsao_entrega').mask('00/00/0000');
    $('#data_saida').mask('00/00/0000');
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
    var cpfMascara = function (val) {
        return val.replace(/\D/g, '').length > 11 ? '00.000.000/0000-00' : '000.000.000-009';
     },
     cpfOptions = {
        onKeyPress: function(val, e, field, options) {
           field.mask(cpfMascara.apply({}, arguments), options);
        }
     };
     $('.mascara-cpfcnpj').mask(cpfMascara, cpfOptions);
    
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
        document.getElementById("demo").innerHTML = "Campo vazio!";
        return false;
    } else if (verificar(nome)){
        return false;
    }

    if(cpf == "" || cpf.length <= 10){
        $('#cpf').css({'border':'1px solid red'});
        return false;;
    }

    if(endereco == ""){
        $('#endereco').css({'border':'1px solid red'});
        document.getElementById("demo1").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarEnderecoCliente(endereco)){
        return false;
    }

    if(bairro == ""){
        $('#bairro').css({'border':'1px solid red'});
        document.getElementById("demo2").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarBairroCliente(bairro)){
        return false;
    }

    if(email == ""){
        $('#email').css({'border':'1px solid red'});
        document.getElementById("demo9").innerHTML = "Campo vazio!";
        return false;
    } else if(email.indexOf('@')  == -1){
        document.getElementById("demo9").innerHTML = "E-mail inválido!";
        return false;
    }

    if(telefone == ""){
        $('#tel').css({'border':'1px solid red'});
        document.getElementById("demo13").innerHTML = "Campo vazio!";
        return false;
    }else if(telefone.length < 13){
        document.getElementById("demo13").innerHTML = "Telefone inválido!";
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
        document.getElementById("demo3").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarNomeEmpresa(nome)){
        return false;
    }

    if(cnpj == "" || cnpj.length <= 13){
        $('#cnpj').css({'border':'1px solid red'});
        return false;
    }

    if(endereco == ""){
        $('#endereco').css({'border':'1px solid red'});
        document.getElementById("demo4").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarEnderecoEmpresa(endereco)){
        return false;
    }

    if(bairro == ""){
        $('#bairro').css({'border':'1px solid red'});
        document.getElementById("demo5").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarBairroEmpresa(bairro)){
        return false;
    }

    if(email == ""){
        document.getElementById("demo10").innerHTML = "Campo vazio!";
        return false;
    } else if(email.indexOf('@')  == -1){
        document.getElementById("demo10").innerHTML = "E-mail inválido!";
        return false;
    }

    if(telefone == ""){
        $('#tel').css({'border':'1px solid red'});
        document.getElementById("demo14").innerHTML = "Campo vazio!";
        return false;
    }else if(telefone.length < 14){
        document.getElementById("demo14").innerHTML = "Telefone inválido!";
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
        document.getElementById("demo6").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarMarca(marca)){
        return false;
    }

    if(modelo == ""){
        $('#modelo').css({'border':'1px solid red'});
        return false;
    }

    if(cor == ""){
        $('#cor').css({'border':'1px solid red'});
        document.getElementById("demo8").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarCor(cor)){
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
        document.getElementById("demo7").innerHTML = "Campo vazio!";
        return false;
    } else if (verificarCidade(cidade)){
        return false;
    }

    if(reparo_OS == ""){
        $('#inputReparo').css({'border':'1px solid red'});
        return false;
    }

    if(prazo_entrega == ""){
        document.getElementById("demo11").innerHTML = "Campo vazio!";
        return false;
    }else if(validaData(prazo_entrega)){
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
        document.getElementById("demo12").innerHTML = "Campo vazio!";
        return false;
    }else if(validaDataPreviEntrega(previsao_entrega)){
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
        document.getElementById("demo14").innerHTML = "Campo vazio!";
        return false;
    } else if(verificarUser(username)){
        return false;
    }

    if(nome == ""){
        $('#nomeUsuarioForm').css({'border':'1px solid red'});
        document.getElementById("demo15").innerHTML = "Campo vazio!";
        return false;
    } else if(verificarNomeForm(username)){
        return false;
    }

    if(sobrenome == ""){
        $('#sobrenomeUsuarioForm').css({'border':'1px solid red'});
        document.getElementById("demo16").innerHTML = "Campo vazio!";
        return false;
    } else if(verificarSobrenomeForm(username)){
        return false;
    }

    if(email == ""){
        $('#emailUsuarioForm').css({'border':'1px solid red'});
        document.getElementById("demo17").innerHTML = "Campo vazio!";
        return false;
    } else if(email.indexOf('@')  == -1){
        document.getElementById("demo17").innerHTML = "E-mail inválido!";
        return false;
    }

    if(password1 == ""){
        $('#password1UsuarioForm').css({'border':'1px solid red'});
        document.getElementById("demo18").innerHTML = "Campo vazio!";
        return false;
    }

    if(password2 == ""){
        $('#password2UsuarioForm').css({'border':'1px solid red'});
        document.getElementById("demo19").innerHTML = "Campo vazio!";
        return false;
    } else if(password2 != password1){
        document.getElementById("demo19").innerHTML = "Senhas diferentes!";
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

function mascaraMutuario(o, f) {
    v_obj = o
    v_fun = f
    setTimeout('execmascara()', 1)
}
function execmascara() {
    v_obj.value = v_fun(v_obj.value)
}

function cpfCnpj(v) {
    //Remove tudo o que não é dígito
    v = v.replace(/\D/g, "")
    if (v.length <= 11) { //CPF
        //Coloca um ponto entre o terceiro e o quarto dígitos
        v = v.replace(/(\d{3})(\d)/, "$1.$2")
        //Coloca um ponto entre o terceiro e o quarto dígitos
        //de novo (para o segundo bloco de números)
        v = v.replace(/(\d{3})(\d)/, "$1.$2")
        //Coloca um hífen entre o terceiro e o quarto dígitos
        v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2")
    } else if(v.length<=14) { //CNPJ
        //Coloca ponto entre o segundo e o terceiro dígitos
        v = v.replace(/^(\d{2})(\d)/, "$1.$2")
        //Coloca ponto entre o quinto e o sexto dígitos
        v = v.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
        //Coloca uma barra entre o oitavo e o nono dígitos
        v = v.replace(/\.(\d{3})(\d)/, ".$1/$2")
        //Coloca um hífen depois do bloco de quatro dígitos
        v = v.replace(/(\d{4})(\d)/, "$1-$2")
    }
    return v
}

function verificar(){

    var texto=document.getElementById("nome").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo").innerHTML = "Nome inválido!";
            //document.getElementById("nome").value="";
            $('#nome').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarBairroCliente(){

    var texto=document.getElementById("bairro").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ 0123456789 ,"
        

        var ok=false;
        for (letra2 of letraspermitidas || caracterPermitido ){

            if (letra==letra2){
                document.getElementById("demo2").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo2").innerHTML = "Bairro inválido!";
            //document.getElementById("nome").value="";
            $('#bairro').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarNomeEmpresa(){

    var texto=document.getElementById("nome").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo3").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo3").innerHTML = "Nome inválido!";
            //document.getElementById("nome").value="";
            $('#nome').css({'border':'1px solid red'});
            return true; 
         }

    }

}


function verificarEnderecoCliente(){

    var texto=document.getElementById("endereco").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ 0123456789 ,"
        

        var ok=false;
        for (letra2 of letraspermitidas || caracterPermitido ){

            if (letra==letra2){
                document.getElementById("demo1").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo1").innerHTML = "Endereço inválido!";
            //document.getElementById("nome").value="";
            $('#endereco').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarEnderecoEmpresa(){

    var texto=document.getElementById("endereco").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ 0123456789 ,"
        

        var ok=false;
        for (letra2 of letraspermitidas || caracterPermitido ){

            if (letra==letra2){
                document.getElementById("demo4").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo4").innerHTML = "Endereço inválido!";
            //document.getElementById("nome").value="";
            $('#endereco').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarBairroEmpresa(){

    var texto=document.getElementById("bairro").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ 0123456789 ,"
        

        var ok=false;
        for (letra2 of letraspermitidas || caracterPermitido ){

            if (letra==letra2){
                document.getElementById("demo5").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo5").innerHTML = "Bairro inválido!";
            //document.getElementById("nome").value="";
            $('#bairro').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarMarca(){

    var texto=document.getElementById("marca").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo6").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo6").innerHTML = "Marca inválida!";
            //document.getElementById("nome").value="";
            $('#marca').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarCidade(){

    var texto=document.getElementById("cidade").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo7").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo7").innerHTML = "Cidade inválida!";
            //document.getElementById("nome").value="";
            $('#cidade').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarCor(){

    var texto=document.getElementById("cor").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo8").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo8").innerHTML = "Cor inválida!";
            //document.getElementById("nome").value="";
            $('#cor').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function validaData(stringData)
{
    /******** VALIDA DATA NO FORMATO DD/MM/AAAA *******/
    
    var regExpCaracter = /[^d]/;     //Expressão regular para procurar caracter não-numérico.
    var regExpEspaco = /^s+|s+$/g;  //Expressão regular para retirar espaços em branco.
    
    if(stringData.length != 10)
    {
        document.getElementById("demo11").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    splitData = stringData.split('/');
    
    if(splitData.length != 3)
    {
        document.getElementById("demo11").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    /* Retira os espaços em branco do início e fim de cada string. */
    splitData[0] = splitData[0].replace(regExpEspaco, '');
    splitData[1] = splitData[1].replace(regExpEspaco, '');
    splitData[2] = splitData[2].replace(regExpEspaco, '');
    
    if ((splitData[0].length != 2) || (splitData[1].length != 2) || (splitData[2].length != 4))
    {
        document.getElementById("demo11").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    dia = parseInt(splitData[0],10);
    mes = parseInt(splitData[1],10)-1; //O JavaScript representa o mês de 0 a 11 (0->janeiro, 1->fevereiro... 11->dezembro)
    ano = parseInt(splitData[2],10);
    
    var novaData = new Date(ano, mes, dia);
    
    /* O JavaScript aceita criar datas com, por exemplo, mês=14, porém a cada 12 meses mais um ano é acrescentado à data
         final e o restante representa o mês. O mesmo ocorre para os dias, sendo maior que o número de dias do mês em
         questão o JavaScript o converterá para meses/anos.
         Por exemplo, a data 28/14/2011 (que seria o comando "new Date(2011,13,28)", pois o mês é representado de 0 a 11)
         o JavaScript converterá para 28/02/2012.
         Dessa forma, se o dia, mês ou ano da data resultante do comando "new Date()" for diferente do dia, mês e ano da
         data que está sendo testada esta data é inválida. */
    if ((novaData.getDate() != dia) || (novaData.getMonth() != mes) || (novaData.getFullYear() != ano))
    {
        document.getElementById("demo11").innerHTML = "Data inválida!";
        return true;
    }
}

function validaDataPreviEntrega(stringData)
{
    /******** VALIDA DATA NO FORMATO DD/MM/AAAA *******/
    
    var regExpCaracter = /[^d]/;     //Expressão regular para procurar caracter não-numérico.
    var regExpEspaco = /^s+|s+$/g;  //Expressão regular para retirar espaços em branco.
    
    if(stringData.length != 10)
    {
        document.getElementById("demo12").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    splitData = stringData.split('/');
    
    if(splitData.length != 3)
    {
        document.getElementById("demo12").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    /* Retira os espaços em branco do início e fim de cada string. */
    splitData[0] = splitData[0].replace(regExpEspaco, '');
    splitData[1] = splitData[1].replace(regExpEspaco, '');
    splitData[2] = splitData[2].replace(regExpEspaco, '');
    
    if ((splitData[0].length != 2) || (splitData[1].length != 2) || (splitData[2].length != 4))
    {
        document.getElementById("demo12").innerHTML = "Data fora do padrão DD/MM/AAAA.";
        return true;
    }
    
    dia = parseInt(splitData[0],10);
    mes = parseInt(splitData[1],10)-1; //O JavaScript representa o mês de 0 a 11 (0->janeiro, 1->fevereiro... 11->dezembro)
    ano = parseInt(splitData[2],10);
    
    var novaData = new Date(ano, mes, dia);
    
    /* O JavaScript aceita criar datas com, por exemplo, mês=14, porém a cada 12 meses mais um ano é acrescentado à data
         final e o restante representa o mês. O mesmo ocorre para os dias, sendo maior que o número de dias do mês em
         questão o JavaScript o converterá para meses/anos.
         Por exemplo, a data 28/14/2011 (que seria o comando "new Date(2011,13,28)", pois o mês é representado de 0 a 11)
         o JavaScript converterá para 28/02/2012.
         Dessa forma, se o dia, mês ou ano da data resultante do comando "new Date()" for diferente do dia, mês e ano da
         data que está sendo testada esta data é inválida. */
    if ((novaData.getDate() != dia) || (novaData.getMonth() != mes) || (novaData.getFullYear() != ano))
    {
        document.getElementById("demo12").innerHTML = "Data inválida!";
        return true;
    }
}



function verificarUser(){

    var texto=document.getElementById("userUsuarioForm").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyz 0123456789"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo14").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo14").innerHTML = "Usuário inválido!";
            //document.getElementById("nome").value="";
            $('#userUsuarioForm').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarNomeForm(){

    var texto=document.getElementById("nomeUsuarioForm").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo15").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo15").innerHTML = "Nome inválido!";
            //document.getElementById("nome").value="";
            $('#nomeUsuarioForm').css({'border':'1px solid red'});
            return true; 
         }

    }

}

function verificarSobrenomeForm(){

    var texto=document.getElementById("sobrenomeUsuarioForm").value;

    for (letra of texto){

        letraspermitidas="ABCEDFGHIJKLMNOPQRSTUVXWYZ abcdefghijklmnopqrstuvxwyzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ"
        

        var ok=false;
        for (letra2 of letraspermitidas){

            if (letra==letra2){
                document.getElementById("demo16").innerHTML = "";
                ok=true;
            }
         }

         if (!ok){
            document.getElementById("demo16").innerHTML = "Sobrenome inválido!";
            //document.getElementById("nome").value="";
            $('#sobrenomeUsuarioForm').css({'border':'1px solid red'});
            return true; 
         }

    }

}