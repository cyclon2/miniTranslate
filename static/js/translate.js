$(document).on("change keyup", "#id_ko_memo", function(){
    $.ajax({
        url: "/api/translate",
        data: {
            "q" : $("#id_ko_memo").val()
        },
        success: function(res){
            var data = JSON.parse(res);
            $("#id_result").text(data.result)
        }
    })
})
$(document).on("click", "#id_definitions_ko_btn", function(){
    $.ajax({
        url: "/api/definition/ko",
        data: {
            "q" : $("#id_ko_memo").val()
        },
        success: function(res){
            var data = JSON.parse(res);
            var words = data.result.definitions;
            $("#id_definitions_ko").empty();
            var item ="";
            for (w in words){
                item += "<p>" + words[w]+"</p>"
            }
            $("#id_definitions_ko").append(item)
        }
    })
})
$(document).on("click", "#id_definitions_en_btn", function(){
    $.ajax({
        url: "/api/definition/en",
        data: {
            "q" : $("#id_en_memo").val()
        },
        success: function(res){
            var data = JSON.parse(res);
            var words = data.result[0].lemmatized;
            $("#id_definitions_en").empty();
            var item ="";
            for (w in words){
                item += "<p>" + words[w]+"</p>"
                item += "<p>" + data.result[1].definitions+"</p>"
            }
            $("#id_definitions_en").append(item)
        }
    })
})
