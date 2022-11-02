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

var first_step = document.getElementsByClassName("form__first_step")[0]
var second_step = document.getElementsByClassName("form__second_step")[0]
var optional_step = document.getElementsByClassName("form__optional_step")[0]
var errorscontent = document.getElementsByClassName('errors-content')[0]
var errorsbox = document.getElementsByClassName('ul__stock-add--errors')[0]
var columnoptions = document.getElementById('columnoptions')
var buttonform = document.querySelectorAll('[form="form__stock-add"]')[0]
var backbutton = document.getElementsByClassName('back-arrow')[0]
var optionalbutton = document.getElementsByClassName('button__optional-columns')[0]
let closeButtonAS = document.querySelector(".modal__addStock .modal__close-button")
let inputs_s_step = second_step.getElementsByTagName("input")
let inputs_opt = optional_step.getElementsByTagName("input")
let allLabelFS = first_step.querySelectorAll('label[tabindex]')
let lastLabelFS = allLabelFS[allLabelFS.length-1]

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

function buttonForTwoStep(){
    buttonform.childNodes[1].innerHTML = "Añadir"
    buttonform.childNodes[2].classList.add("icon-upload")
    buttonform.childNodes[2].classList.remove("button__special-arrow")
    buttonform.setAttribute("onclick", "ProcesarDatosDos()")
}

function buttonForOneStep(){
    buttonform.childNodes[1].innerHTML = "Seguir"
    buttonform.childNodes[2].classList.remove("icon-upload")
    buttonform.childNodes[2].classList.add("button__special-arrow")
    buttonform.setAttribute("onclick", "ProcesarDatos()")
}

function ProcesarDatos(){
    var form = new FormData(document.getElementById('form__stock-add'));
    const request = new Request(
    url_add_stock,
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
                        var name_column = document.getElementById("id_name_column")
                        fillDataList(data.column_names)
                        showOrCollapse(first_step, collapse=true)
                        showOrCollapse(second_step, collapse=false)
                        showOrCollapse(backbutton, collapse=false)
                        showOrCollapse(optionalbutton, collapse=false)
                        
                        buttonForTwoStep()                        
                        
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
    url_add_stock,
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
                if (data.redirect_url) {
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

function BackToStepOne(){
    var firstTextInput = document.querySelector("#form__stock-add .form__first_step input[type='text']");

    buttonForOneStep()
    showOrCollapse(first_step, collapse=false)
    showOrCollapse(second_step, collapse=true)
    showOrCollapse(optional_step, collapse=true)
    showOrCollapse(backbutton, collapse=true)
    showOrCollapse(optionalbutton, collapse=true)
    columnoptions.innerHTML = ""

    firstTextInput.focus()
}

function showOptionalColumns(){
    var firstTextInput = document.querySelector("#form__stock-add .form__optional_step input[type='text']");

    showOrCollapse(second_step, collapse=true)
    showOrCollapse(optional_step, collapse=false)
    optionalbutton.setAttribute("onclick", "hideOptionalColumns()")
    optionalbutton.setAttribute("title", "Ocultar columnas adicionales")
    optionalbutton.style.transform = 'rotate(180deg)'
    
    firstTextInput.focus()
}

function hideOptionalColumns(){
    var firstTextInput = document.querySelector("#form__stock-add .form__second_step input[type='text']");

    showOrCollapse(second_step, collapse=false)
    showOrCollapse(optional_step, collapse=true)
    optionalbutton.setAttribute("onclick", "showOptionalColumns()")
    optionalbutton.setAttribute("title", "Mostrar columnas adicionales")
    optionalbutton.style.transform = ""

    firstTextInput.focus()
}

function openAddStockModal() {
    var AddStockCheck = document.getElementById("addStockCheck");
    var firstTextInput = document.querySelector("#form__stock-add input[type='text']");
    AddStockCheck.checked = true;
    firstTextInput.focus();
}
function uploadFilePutName(target) {
    var selectorFileNameTextBox = "#"+target.id+" ~ .upload-file__interfaz .upload-file__filename";
    var UploadFileNameField = document.querySelector(selectorFileNameTextBox);
    UploadFileNameField.innerHTML = target.files[0].name;
}
function enterForInterfaceButton(){
    var buttons_generic = document.querySelectorAll("#form__stock-add .upload-file__button-load")
    for (let button of buttons_generic){
        enterToClick(button, button)
    }
}

setNextFocus(second_step.lastElementChild, optionalbutton)
setNextFocus(optional_step.lastElementChild, optionalbutton)

setNextFocus(optionalbutton, backbutton)
setNextFocus(backbutton, buttonform)
setNextFocus(buttonform, closeButtonAS)

setNextFocus(closeButtonAS, inputs_s_step[0])
setNextFocus(closeButtonAS, inputs_opt[0])

setPrevFocus(closeButtonAS, buttonform)
setPrevFocus(buttonform, lastLabelFS)
setPrevFocus(buttonform, backbutton)
setPrevFocus(backbutton, optionalbutton)
setPrevFocus(optionalbutton, inputs_s_step[inputs_s_step.length-1])
setPrevFocus(optionalbutton, inputs_opt[inputs_opt.length-1])

enterToClick(closeButtonAS, closeButtonAS)
enterForInterfaceButton()

