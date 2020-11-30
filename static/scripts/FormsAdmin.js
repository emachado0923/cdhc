//Abrir modal
$('#ButtonModal').on('click', () => {
    $('#modalForm').modal('show');
});

//Al cargar la pagina se listaran los datos
$(window).on('load', function () {

});

const ActualizarLista = (values) => {
    $("#table_id > tbody:last-child")
        .append(`
                           <tr>
                            <td>${values.nombreFormulario}</td>
                            <td><a href="${values.urlFormulario}" class="btn btn-warning btn-lg active" role="button" aria-pressed="true"  data-toggle="tooltip" data-placement="right" title="Ir al formulario"><i class="fa fa-eye"></a></td>
                            <td><a href="${values.urlRespuestas}" class="btn btn-success btn-lg active" role="button" aria-pressed="true"  data-toggle="tooltip" data-placement="right" title="Ver Resultados"><i class="fa fa-table"></i></a></td>
                           </tr>`);

};

//Formulario de registro con ajax
$('#formulario').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: "{% url 'api:newForm' %}",
        data: {
            nombreFormulario: $('#nombreFormulario').val(),
            urlFormulario: $('#urlFormulario').val(),
            urlRespuestas: $('#urlRespuestas').val(),
            dataType: "json",
            csrfmiddlewaretoken: '{{csrf_token}}'
        },

        success: function (data) {

            let {message, error, values} = data;

            if (message) {
                ActualizarLista(values);
                $('#modalForm').modal('hide');
            }
            if (error) {
                console.log(data);
                alert('err')
            }

        },
    });
});
