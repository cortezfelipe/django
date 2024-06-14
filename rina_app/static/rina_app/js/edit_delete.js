function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// Abrir modal edicao e atribuir valores
$('.edit-item').on('click', function () {
    var pk = $(this).parent().parent().attr("data-id")
    var view = $(this).parent().parent().attr("data-view")
    console.log("cliquei em editar " + pk + " " + view)


    $.ajax({
        url: view,
        type: "POST",
        dataType: "json",
        data: { "id": pk, "action": "get-data" },
        success: function (data) {
            presponse = JSON.parse(data)
            $('#edit-modal').modal('show')
            $('#edit-modal').find('#edit-modal-body-text').html('<p>ID: ' + presponse[0].pk + '</p>')
            $('#form-modal-edit').attr("data-id", pk)
            $('#form-modal-edit').attr("data-view", view)
            $('#form-modal-edit').find('#id_data_id').val(pk);

            fields = presponse[0]['fields']
            for (field in fields) {
                $(`[name="${field}"]`).val(fields[field])
            }

        }
    });
})

// Clicando em icone de deletar na tabela
$('.delete-item').on('click', function () {
    var pk = $(this).parent().parent().attr("data-id")
    var view = $(this).parent().parent().attr("data-view")
    console.log("cliquei em deletar " + pk + " " + view)


    $.ajax({
        url: view,
        type: "POST",
        dataType: "json",
        data: { "id": pk, "action": "get-data" },
        success: function (data) {
            // console.log(data)
            presponse = JSON.parse(data)
            $('#delete-modal').modal('show')
            $('#delete-modal').find('.modal-body').html('<p>Prosseguir com deleção do item?</p><p>ID: ' + presponse[0].pk + '</p>')
            $('#form-modal-delete').find('#data-id-delete').val(pk)
            $('#form-modal-delete').attr("data-id", pk)
        }
    });
})

// Deletando item bind botao
$(function () {
    $('#form-modal-delete').on('submit', function (e) {
        e.preventDefault();
        var pk = $(this).attr("data-id")
        var view = $(this).attr("action")

        console.log(pk + ' ' + view);
        $('#delete-modal').modal('hide')

        $.ajax({
            url: view,
            type: "POST",
            dataType: "json",
            data: { "id": pk, "action": "delete" },
            success: function (data) {
                console.log(data)
                location.reload()
            }
        });
    });
});