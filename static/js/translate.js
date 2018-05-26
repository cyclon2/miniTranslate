$(document).on("change keyup", "#id_ko_memo", function(){
    var text_data = $("#id_ko_memo").val();
    $("#id_word_count").text(text_data.length);
    $.ajax({
        url: "/api/translate",
        data: {
            "q" : text_data
        },
        success: function(res){
            var data = JSON.parse(res);
            $("#id_result").text(data.result)
        }
    })
});
$(document).on("click", "#id_definitions_ko_btn", function(){
    $.ajax({
        url: "/api/definition/ko",
        data: {
            "q" : $("#id_ko_memo").val()
        },
        beforeSend: function(){
            $("#id_definitions_ko_loader").show();
        },
        success: function(res){
            var data = JSON.parse(res);
            var words = data.result.definitions;
            $("#id_definitions_ko").empty();
            var item ="";
            for (w in words){
                if(words[w] != null && words[w][0] != ""){
                    var word = words[w][0];
                    var meaning = words[w][1];
                    item += "<p>";
                    item += "<span class='word-title'>"+ word +"</span>";
                    item += "<span class='word-meaning'>"+ meaning +"</span>";
                    item += "</p>"
                }
            }
            $("#id_definitions_ko").append(item);
            $("#id_definitions_ko_loader").hide();
        }
    })
});
// $(document).on("click", "#id_definitions_ko_btn", function(){
//     $.ajax({
//         url: "/api/definition/ko",
//         data: {
//             "q" : $("#id_ko_memo_detail").val()
//         },
//         success: function(res){
//             var data = JSON.parse(res);
//             var words = data.result.definitions;
//             $("#id_definitions_ko_detail").empty();
//             var item ="";
//             for (w in words){
//                 if(words[w][0] != ""){
//                     var word = words[w][0];
//                     var meaning = words[w][1];
//                     item += "<div>";
//                     item += "<span class='word-title'>"+ word +"</span>";
//                     item += "<span class='word-meaning'>"+ meaning +"</span>";
//                     item += "</div>"
//                 }
//             }
//             $("#id_definitions_ko_detail").append(item)
//         }
//     })
// });
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
});