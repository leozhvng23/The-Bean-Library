function set_background_color(){
    const colorThief = new ColorThief();
    const img = document.querySelector('img');
    if (img.complete) {
      dominantColor = colorThief.getColor(img);
    } else {
      image.addEventListener('load', function() {
        dominantColor = colorThief.getColor(img);
      });
    }
    dominantColor.push('0.4')
    $('body').css('background-color', dominantColor);
    $('.image').css('background-color', dominantColor);
}

$(document).ready(function(){
    set_background_color();
    $("#searchForm").submit(function(e){
        console.log("form");
        e.preventDefault();
        let search_text = $("#form_input").val();
        if (search_text.trim()==""){
            $("#form_input").val("");
            $("#form_input").focus();
        } else {
            window.location.href = "/search_results/" + search_text;
        }
    })
})