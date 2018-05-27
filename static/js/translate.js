$(document).ready(function(){
    getWordRank();
});

$(document).on("change keyup", "#id_ko_memo", function(){
    var text_data = $("#id_ko_memo").val();
    $("#id_ko_memo").val(text_data.substring(0,5000));
    text_data = $("#id_ko_memo").val();
    var data = {
        "q" : text_data,
    };
    $("#id_word_count").text(text_data.length);
    if($("#id_checkbox_kr_to_en").is(":checked")){
        data['from'] = "ko";
        data['to'] = "en";
    }
    $.ajax({
        url: "/api/translate",
        data: data,
        success: function(res){
            var data = JSON.parse(res);
            $("#id_result").text(data.result)
        }
    });
});
$(document).on("focusout", "#id_ko_memo", function(){ 
    var data = $("#id_ko_memo").val();
    if($("#id_checkbox_kr_to_en").is(":checked") || data.length == 0){
        return false;
    }
    $.ajax({
        url: "/api/words",
        type: "POST",
        data: {
            "sentence" : data
        },
        success: function(res){
            console.log("[POST] SUCCESS to store");
            $.ajax({
                url:'/api/word',
                success: function(res){ 
                    getWordRank()
                }
            });
        }
    });  
});

function getWordRank(){
    $.ajax({
        url:'/api/word',
        success: function(res){ 
            $("#id_my_word_list").empty()
            var item = "";
            for(var d in res.data){
                var word = res.data[d];
                item += "<p>";
                item += "<div class='side-word-count'>"+ word[3] +"</div>";
                item += "<div class='side-word'>"+ word[1] +"</div>";
                item += "<div class='side-word-meaning'>"+ word[2] +"</div>";
                item += "</p>"
            }
            $("#id_my_word_list").append(item);
        }
    });
}

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
                    var dictid = words[w][1][0];
                    var meaning = words[w][1][1];
                    item += "<p>";
                    item += "<span class='word-title'>"+ word +"</span>";
                    item += "<span class='word-meaning'>"+ meaning +"</span>";
                    item +="<button class='word-store-btn' data-id='"+dictid+"'>추가</button>"
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

$(document).on("click", "#id_sentence_store_btn", function(){
    var raw = $("#id_ko_memo").val();
    var translated = $("#id_result").text();
    if( raw == "" || translated == ""){
        return;
    } 
    $.ajax({
        type:"POST",
        url:'/api/sentence',
        data: { 
            "raw": raw, 
            "translated": translated
        },
        success: function(res){ 
            alert("성공적으로 저장되었습니다.")
        }
    });
});

$(document).on("click", ".sentence-delete-btn", function(){
    var id = $(this).data('id');
    var _this = $(this);
    $.ajax({
        type:"DELETE",
        url:'/api/sentence/'+id,
        success: function(res){ 
            _this.closest(".sentence-container").remove()
            alert("성공적으로 삭제되었습니다.");
        }
    });
});

$(document).on("click", ".word-delete-btn", function(){
    var id = $(this).data('id');
    var _this = $(this);
    $.ajax({
        type:"DELETE",
        url:'/api/word/'+id,
        success: function(res){ 
            _this.closest(".word-container").remove()
            alert("성공적으로 삭제되었습니다.");
        }
    });
});


$(document).on("click", ".word-store-btn", function(){
    var word = $(this).parent().find(".word-title").text();
    var dictid = $(this).data('id');
    $.ajax({
        type:"PATCH",
        url:'/api/word',
        data : {
            'word': word,
            'dictid': dictid
        },
        success: function(res){ 
            alert("성공적으로 추가되었습니다.");
        }
    });
});