var carrito_compra = {};
var opciones_productos = [];
var l = null;
$(document).ready(function(){
    $("#code-id-producto").on('input',function(e1){
        buscar_producto_por_id($(this).val());
    });
    $("#code-id-producto").keyup(function(key){ if (key.keyCode == 13) {
        if (opciones_productos.length == 0) error_noencontrado(); else { var data = opciones_productos[0]; agregar_producto(data);}
    }});
    $("#car-shop").on("click",".delete-product", function(){
        console.log($(this).parents("tr").attr("data-id"));
        eliminar_producto($(this).parents("tr").attr("data-id"));
        actualizarTotal();

    });
    $("#car-shop").on("click",".sub", function(){
        var cantidad = $(this).parents("tr").find(".quantity");
        if (cantidad.val()<=1) {
            error_menosdeUnProducto();
            cantidad.val(1);
        } else{
            cantidad.val(cantidad.val()-1);
            actualizarPrecio($(this).parents("tr").attr("data-id"));
        }   
    });
    $("#car-shop").on("click",".add", function(){
        var cantidad = $(this).parents("tr").find(".quantity");
        cantidad.val((cantidad.val()-0)+1);
        actualizarPrecio($(this).parents("tr").attr("data-id"));
    });
    $("#car-shop").on("input",".form-control.quantity", function(){
        actualizarPrecio($(this).parents("tr").attr("data-id"));
    });
    $("#menu-toggle").click(function(e) {
        //e.preventDefault();
        if ($("#navbarNav").css("width")=="0px") {
            $("#navbarNav").animate({width: "350px"},50);
            $("#content-sellpoint").animate({marginRight: "350px"},50);
            $("#informacion-compra-div").switchClass(
                "col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12",
                "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12", 50, "easeInOutQuad" );
            //col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12
        }else{
            $("#content-sellpoint").animate({marginRight: "0px"},50);
            $("#navbarNav").animate({width: "0px"},50);
            $("#informacion-compra-div").switchClass("col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12","col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12", 50, "easeInOutQuad" );
        }
    });
});
function llenarTabladeProductosCoincidentes(elementos){
    $(".product-search .table tbody").html("");
    opciones_productos = elementos;
    if (elementos.length > 0) for (var index = 0; index < elementos.length; index++) {
        $(".product-search .table tbody").append('<tr><th scope="row">'+elementos[index].id+'</th><td>'+elementos[index].nombre+'</td><td><button class="btn btn-success" data-id-array="'+index+'">+</button></td></tr>');
    }

}
function buscar_producto_por_id(id){
    var x = new XMLHttpRequest();
    x.open('GET',productos_getbyid +'?id='+ id)
    x.onreadystatechange = function (e){
        if(x.readyState == 4){
            if(x.status === 200){
                x.addEventListener('load', function(e){
                    llenarTabladeProductosCoincidentes(JSON.parse(x.responseText.replace(/\'/g,'"')));
                });'c'
            }
        }
    }
    x.send();
}

function agregar_producto(data){
    if (typeof carrito_compra[data.id] == "undefined") {
        data['cantidad']=1;
        if (carrito_compra.length <= 0) $("#car-shop tbody").html("");
        $("#car-shop tbody").append('<tr data-id="'+data.id+'"><th scope="row"><a>'+data.id+'</a></th> <td>'+data.nombre+'</td> <td>'+parseFloat(data.precio).toFixed(2)+'</td> <td> <div class="form-group"> <div class="input-group mb-3"> <div class="input-group-prepend"> <button type="button" class="btn fas fa-angle-left sub"></button> </div> <input type="number" class="form-control quantity" value="'+data.cantidad+'"> <div class="input-group-append"> <button type="button" class="btn fas fa-angle-right add"></button> </div> </div> </div> </td> <td class="subtotal">'+parseFloat(data.precio).toFixed(2)+'</td> <td> <div class="btn-group"> <button class="btn btndata-danger active mdi mdi-close delete-product"></button</div></td></tr>');
        carrito_compra[data.id] = data;
        actualizarTotal();        
    }else{
        error_yaestaencarro();
    }
}

function eliminar_producto(id){
    var tr_delete = $("tr[data-id="+id+"]");
    tr_delete.css("width","100%");
    tr_delete.css("display","block");
    tr_delete.remove()
    delete carrito_compra[id];
}

function modificarCantidad(id,cantidad){
    if (cantidad>0) {
        carrito_compra[id].cantidad;
        actualizarPrecio(id);
    }else{

    }
}
function actualizarTotal(){
    var total = 0.0;
    for (var index in carrito_compra){ total+=(parseFloat(carrito_compra[index].cantidad) * parseFloat(carrito_compra[index].precio) );}
    $("#subtotal").html(total);
    $("#total").html(parseFloat(total + (total*0.16)).toFixed(2));
}

function actualizarPrecio(id){
    var quantity = Math.abs($("tr[data-id="+id+"] .quantity").val());
    if (isNaN(quantity) || quantity == "")  quantity = 0;
    carrito_compra[id].cantidad = parseFloat(quantity);
    $("tr[data-id="+id+"] .subtotal").text( (carrito_compra[id].cantidad * carrito_compra[id].precio).toFixed(2) );
    actualizarTotal();
}

function error_menosdeUnProducto(){
    swal({
        type: 'error',
        title: 'Solo queda un producto!',
        text: 'No es posible reducir mas la cantidad.',
    });
}

function error_yaestaencarro(){
    swal({
        type: 'error',
        title: 'Ya esta en la lista!',
        text: 'No es posible agregarlo debido a que ya esta en el carrito.',
    });
}

function error_noencontrado(){
    swal({
        type: 'error',
        title: 'No se encontro el producto!',
        text: 'No fue posible encontrar.',
    });
}

function nuevacompra(){
    
}

function vender(){
    $.ajax({
        url: generar_venta,
        type:  'POST',
        data:"compra="+JSON.stringify(opciones_productos),
        success: function(html){
            nuevacompra();
        }
    });
}

/*
  if (data.length > 0) {
$("#result_").html("");
$("#calculator_data").slideUp();
var row = data[0];
$("#code-id-producto").attr("data-id-product",data[0]);
}else{
$("#result_").html("No se encontro");
$("#code-id-producto").attr("data-id-product","");
}

function buscar_praoducto_por_id(id){
    if (id !== "")
        $.ajax({
        url: "{% url 'productos_getbyid' %}",
        type: "GET",
        data: {id : id},
        success: function(data){
            console.log(data);
            jsonvar = JSON.parse(data);
        }
    });
}

$("#menu-toggle").click(function(e) {
    //e.preventDefault();
    if ($("#navbarNav").css("width")=="0px") {
        $("#navbarNav").animate({width: "350px"},50);
        $("#content-sellpoint").animate({marginRight: "350px"},50);
        $("#informacion-compra-div").switchClass(
            "col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12",
            "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12", 50, "easeInOutQuad" );
        //col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12
    }else{
        $("#content-sellpoint").animate({marginRight: "0px"},50);
        $("#navbarNav").animate({width: "0px"},50);
        $("#informacion-compra-div").switchClass(
            "col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12",
            "col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12", 50, "easeInOutQuad" );
    }
});
$('#sidebar-nav a').click(function (e) {
      e.preventDefault()
      $(this).tab('show')
});
$(document).keypress(function(evt){
    if ($(':focus').attr("id") != "code-id-producto" && $("#navbarNav").css("width")!="0px") {
        var patt = /[0-9]|\/|\*|\-|\+/i;
        if (String.fromCharCode(evt.keyCode).match(patt)) {
            $("#code-id-producto").val($("#code-id-producto").val() + String.fromCharCode(evt.keyCode));
            productosId();
        }
    }
});
$(document).keyup(function(evt){
    console.log(evt.keyCode);
    if ($(':focus').attr("id") != "code-id-producto") {
        if (evt.keyCode == 127) {
            $("#code-id-producto").val("");
        }
        if (evt.keyCode == 8) {
            $("#code-id-producto").val( $("#code-id-producto").val().slice(0, -1));
        }
        
    }
});
$("#code-id-producto").on('input',function(e1){
    buscar_producto_por_id($(this).val());
});
var compras = [];
function concuir_compra(){
}
var jsonvar = "";

*/