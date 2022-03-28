
function visitPage(id){
    window.location='/view/' + id;
}

function display_list(beans){
    let new_list = $("<div class='row'>");
    $.each(beans, function(i, item){
        let id = item.id;
        let name = item.name;
        let image = item.image;
        let bean_card = $("<div class='col-4'>");
        let bean_image = $("<a href='/view/"+id+"' id='link'><img src='"+image+"' id='explore_image' alt='Product Packaging Design'></a>");
        bean_card.append(bean_image);
        let bean_name = $("<button onclick='visitPage("+id+");' id='listItem' class='h2'>"+name+"</button>");
        /*let bean_name = $("<span id='listText' class='h2'>"+name+"</span>")*/
        bean_card.append(bean_name);
        new_list.append(bean_card);
    })
    $("#beanList").append(new_list);   
}

$(document).ready(function(){
    display_list(beans);
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