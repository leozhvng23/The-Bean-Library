let variety_list = "";
let process_list = "";
let notes_list = "";

function makeList(){
    variety_list = bean.variety.toString();
    process_list = bean.process.toString();
    notes_list = bean.notes.toString();
    console.log(variety_list, process_list, notes_list);
    $("#varietyInput").val(variety_list);
    $("#processInput").val(process_list);
    $("#notesInput").val(notes_list);
}

function edit() {
    let name = $("#nameInput").val();
    let image = $("#imageInput").val();
    let roaster = $("#roasterInput").val();
    let description = $("#descriptionInput").val();
    let variety = $("#varietyInput").val().split(',');
    let process = $("#processInput").val().split(',');
    let notes = $("#notesInput").val().split(',');
    let elevation = $("#elevationInput").val();
    let roast = $("#roastInput").val();    

    let data_to_save = {
        "id": bean.id,
        "name": name,
        "image": image,
        "roaster": roaster,
        "variety": variety,
        "process": process,
        "elevation": elevation,
        "roast": roast,
        "notes": notes,
        "description": description
    }
    $.ajax({
        type: "POST",
        url: "/edit_entry",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_save),
        success: function(result){
            window.location ='/view/' + result["id"];
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
};

$(document).ready(function(){

    makeList();

    $("#searchForm").submit(function(e){
        console.log("search form");
        e.preventDefault();
        let search_text = $("#form_input").val();
        if (search_text.trim()==""){
            $("#form_input").val("");
            $("#form_input").focus();
        } else {
            window.location.href = "/search_results/" + search_text;
        }
    })

    $("#editForm").submit(function(e){
        console.log("edit form");
        e.preventDefault();
        edit();
    })

    $('#editDiscard').click(function(){
        if (confirm('Are you sure?')){
            window.location.href = "/view/" + bean.id;
        } else {
            console.log('no')
        }
    })


})