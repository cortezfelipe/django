function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// Clicando em icone de filtrar na tabela
$('#filter-table-link').on('click', function () {
    $('#filter-modal').modal('show')
})

// Bind form de filtro
$(function() { 
    $('#filter-modale').on('submit', function(e) { 
        e.preventDefault(); 
        $('#delete-modal').modal('hide')
        $('#filter-modale').submit()

    });
});