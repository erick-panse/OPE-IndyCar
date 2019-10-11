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