var carrito_compra = {};
var opciones_productos = [];

$(document).ready(function(){
    $("#code-id-producto").on('input',function(e1){
        buscar_producto_por_id($(this).val());
    });
    $("#code-id-producto").keyup(function(key){ if (key.keyCode == 13) {
        if (opciones_productos.length == 0) error_menosdeUnProducto(); else {
            var data = opciones_productos[0];
            agregar_producto(data);
        }
    }});
    $("#car-shop").on("click",".delete-product", function(){
        eliminar_producto($(this).parents("tr").attr("data-id"));
        $(this).parents("tr").remove();
    });
    $("#car-shop").on("click",".delete-product", function(){
        eliminar_producto($(this).parents("tr").attr("data-id"));
        $(this).parents("tr").remove();
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
        console.log(this);
        actualizarPrecio($(this).parents("tr").attr("data-id"));
    });
/*
quantity
btn btn-primary fas fa-angle-left remove
add
*/
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
});
var l = null;
 
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

function agregar_producto(data){data
    data['cantidad']=1;
    if (opciones_productos.length == 0) $("#car-shop tbody").html("");data
    $("#car-shop tbody").append('<tr data-id="'+data.id+'"> <th scope="row"><a>'+data.id+'</a></th> <td>'+data.nombre+'</td> <td>'+data.precio+'</td> <td> <div class="form-group"> <div class="input-group mb-3"> <div class="input-group-prepend"> <button type="button" class="btn btn-primary fas fa-angle-left sub"></button> </div> <input type="number" class="form-control quantity" value="'+data.cantidad+'"> <div class="input-group-append"> <button type="button" class="btn btn-primary fas fa-angle-right add"></button> </div> </div> </div> </td> <td class="subtotal">'+data.precio+'</td> <td> <div class="btn-group"> <button class="btn btndata-danger active mdi mdi-close delete-product"></button> </div> </td> </tr>');
    carrito_compra[data.id] = data;
}

function eliminar_producto(id){
    delete carrito_compra[id];
}

function modificarCantidad(id,cantidad){
    if (cantidad>0) {

        carrito_compra[id].cantidad++;
        actualizarPrecio(id);
    }else{

    }
}


function actualizarTotal(){
    

}

function actualizarPrecio(id){
    var cantidad = $("tr[data-id="+id+"]").find(".quantity").val();
    opciones_productos[id].cantidad = cantidad;
    $("tr[data-id="+id+"]").find(".subtotal").text(cantidad*opciones_productos[id].precio);
}

function error_menosdeUnProducto(){
    swal({
        type: 'error',
        title: 'Solo queda un producto!',
        text: 'No es posible reducir mas la cantidad.',
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