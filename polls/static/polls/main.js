
$(document).ready(function() {

    function createCard(form) {
        $.ajax({
            url : form.attr("action"),
            type : "POST",
            data : form.serialize(),

            success : function(data) {
                console.log(data);
                if (data['result'] == 'success') {
                    $("#company_card_list").append(data['data'] + '<br>');
                } else if(data['result'] == 'error') {
                    error_summary = $("#error_summary")
                    $.each(data['data'], function (key, value) {
                        error_summary.append(key + ': ' + value.join(' ') + '<br>')
                    })
                }
            },
        });
    }

    $("#card_form").on('submit', function(event){
        event.preventDefault();
        createCard($(this));
    });
});