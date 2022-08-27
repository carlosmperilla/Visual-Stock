function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function showOrCollapse(element, collapse){
    if (collapse) {
        element.classList.add('collapse')
    } else {
        element.classList.remove('collapse')
    }
}

var errorscontent = document.getElementsByClassName('errors-content')[0]
var errorsbox = document.getElementsByClassName('ul__stock-add--errors')[0]
var columnoptions = document.getElementById('columnoptions')
var buttonform = document.querySelectorAll('[form="form__stock-add"]')[0]

function fillErrorsBox(errors){
    Object.keys(errors).forEach(
        (key) => {
            var liFather = document.createElement('li')
            var ul = document.createElement('ul')

            liFather.innerHTML = key

            errorsbox.appendChild(liFather)
            liFather.appendChild(ul)

            errors[key].forEach(
                (error) => {
                    var liChild = document.createElement('li')
                    liChild.innerHTML = error["message"]
                    ul.appendChild(liChild)
                }
            )
        })
    }

function fillDataList(column_names){
    column_names.forEach(
        column_name => {
            var option = document.createElement('option')
            option.innerHTML = column_name
            columnoptions.appendChild(option)        
        }
    )  
}

function ProcesarDatos(){
    var form = new FormData(document.getElementById('form__stock-add'));
    const request = new Request(
    window.location,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: form,
        mode: 'same-origin' // Do not send CSRF token to another domain.
    }
        );
   
    function jsonRequest(){
        fetch(request).then(
                (response) => {
                    return response.json()
                }
            ).then(
                (data) => {
                    if (data.column_names) {
                        var first_step = document.getElementsByClassName("form__first_step")[0]
                        var second_step = document.getElementsByClassName("form__second_step")[0]
                        var name_column = document.getElementById("id_name_column")
                        fillDataList(data.column_names)
                        showOrCollapse(first_step, collapse=true)
                        showOrCollapse(second_step, collapse=false)
                        
                        buttonform.setAttribute("onclick", "ProcesarDatosDos()")
                        name_column.focus()
                    } else {
                        var errors = JSON.parse(data.errors)
                        fillErrorsBox(errors)
                        showOrCollapse(errorscontent, collapse=false)
                    }
                }
            )
    }

    errorsbox.innerHTML = ""
    showOrCollapse(errorscontent, collapse=true)
    jsonRequest()

}

function ProcesarDatosDos(){
    
    var form = new FormData(document.getElementById('form__stock-add'));
    form.append("second_step", "true");
    const request = new Request(
    window.location,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: form,
        mode: 'same-origin' // Do not send CSRF token to another domain.
    }
        );

    function jsonRequest(){
        fetch(request).then(
            (response) => {
                return response.json()
            }
        ).then(
            (data) => {
                console.log(data)
                if (data.redirect_url) {
                    console.log(data.redirect_url)
                    window.location.href = data.redirect_url
                } else {
                    if (data.errors){
                        var errors = JSON.parse(data.errors)
                        fillErrorsBox(errors)
                        showOrCollapse(errorscontent, collapse=false)
                    }
                }
            }
        )
    }

    errorsbox.innerHTML = ""
    showOrCollapse(errorscontent, collapse=true)
    jsonRequest()
}    