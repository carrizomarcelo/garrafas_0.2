$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
                },
            dataSrc: "",
            },
        columns: [
            { "data": "id"},
            { "data": "nro_dni"},
            { "data": "apellido"},
            { "data": "nombre"},
            { "data": "imgdni"},
            { "data": "imgdni"}
            ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/core/personas/edit/'+row.id+'/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/core/personas/delete/'+row.id+'/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
    },
],
initComplete: function(settings, json) {
  }
});
});