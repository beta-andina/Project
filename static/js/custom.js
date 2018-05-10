// Add your custom JS code here

$('#busquedProyecto').keyup(function(e){
 consulta = $("#busquedProyecto").val();
 $.ajax({
 data: {'nombre': consulta},
 url: '/movimientos/busqueda/',
 type: 'get',
 success : function(data) {
         console.log(data[0].nombre);
 },
 error : function(message) {
         console.log(message);
      }
 });
});