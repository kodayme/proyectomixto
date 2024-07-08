$(document).ready(function () {
    $("#aviso").hide();
    $("#aviso").fadeIn(1000).delay(2000).fadeOut(1000);
    $("#aviso_de_registro").hide();
    $("#aviso_de_registro").fadeIn(1000).delay(2000).fadeOut(1000);
    $("#aviso2").hide();
    $("#aviso2").fadeIn(1000).delay(2000).fadeOut(1000);
    $("#blurring").hide().fadeIn(3000);
    $("#cate").hide();
    $("#blur").hide().fadeIn(3000);
    // $("#desplazo").hide();
    // $("#desplazo").slideToggle(500);
    // $("#anim").animate({marginTop: "0px"},1000, "easeOutBounce");


    $("#contacto").animate({marginLeft: "0px"},500,"easeOutCubic");
    // $("#contacto").animate({marginTop: "0px"},1000, "easeOutBounce");

    $("#desplazo").toggle(function () {

        $("#cate").slideDown(300);

    },function () {
        $("#cate").fadeOut(300)
    });

    $("#contacto").toggle(function () {
        $("#formulario").stop().animate({marginLeft: "300px"},500, "easeOutBounce");
    },function () {
        $("#formulario").stop().animate({marginLeft: "-550px"},500, "easeOutCubic");
    });
// ==================================================ANIMACIÓN DE LOS SERVICIOS==================================================================
    $("#animacion").animate({marginLeft:"100"},1000, "easeOutBounce");
    $("#animacion2").animate({marginTop:"10"},1000, "easeOutCubic");
    $("#animacion3").animate({marginLeft:"100px"},1000, "easeOutCubic");
    $("#animacion4").animate({marginTop:"10px"},900, "easeOutBounce");
// ================================================================================================================================================

    $("#usuarios").animate({marginLeft: "0"},1500, "easeOutBounce");
    $("#regis").animate({marginTop: "0"},1250,"easeOutCubic");
    $("#usuario").animate({marginLeft: "0"},1000, "easeOutCubic");
});
