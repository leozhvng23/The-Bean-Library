
function visitPage(id){
    window.location='/view/' + id;
}

function display_list(results){
    if (results[0].length == 0 && results[1].length==0 && results[2].length==0){
        let no_results = $("<div class='beanName'><span class='h2 medium mediumLarge coffee italic'>Sorry, no results found.</span></div>");
        $("#beanList").append(no_results);
    } else {
        let yes_results = $("<div class='beanName'><span class='coffee italic'>("+count+" results found)</span></div>");
        $("#beanList").append(yes_results);
        $.each(results, function(i, field){
            if (field.length > 0) {
                let field_name = fields[i]
                let new_field = $("<div class='beanName'><span class='h2 medium mediumLarge coffee'>Matching records on "+field_name+": </span></div>")
                let new_list = $("<ul style='list-style-type:none' class='paddingTop'>");
                $.each(field, function(i, result){
                    let id = result.id;
                    let name = result.name;
                    let bean_name = $("<li><button onclick='visitPage("+id+");' id='listItem' class='h2'>"+name+"</button></li>");
                    new_list.append(bean_name);
                })
                $("#beanList").append(new_field);
                $("#beanList").append(new_list);
            } 
        })
        
    }
}

$(document).ready(function(){
    display_list(results);
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