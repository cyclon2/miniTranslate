$(document).on('click', '#id_post', function(){
    var content = $('.ql-editor').children().html()
    var title = $('input[name="post_title"]').val()
    if (content.length == 0 || title.length == 0){
        return false
    }
    $.ajax({
        url : '/api/post',
        type: 'POST',
        data : {
            "title" : title,
            "content" : content
        },
        success: function(res){
            location.href="/post/list";
        }
    })
});

$(document).ready(function(){
    var editor = new Quill('#id_writing', {
        modules: {
            toolbar:  [
                ['bold', 'italic', 'underline', 'strike'], 
                ['blockquote', 'code-block'],

                [{ 'header': 1 }, { 'header': 2 }],              
                [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                [{ 'script': 'sub'}, { 'script': 'super' }],     
                [{ 'indent': '-1'}, { 'indent': '+1' }],         
                [{ 'direction': 'rtl' }],                       

                [{ 'size': ['small', false, 'large', 'huge'] }], 
                [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

                [{ 'color': [] }, { 'background': [] }], 
                [{ 'font': [] }],
                [{ 'align': [] }],
                ['clean']             
            ]
        },
        theme: 'snow',
        placeholder: "글쓰기.."
    });
});