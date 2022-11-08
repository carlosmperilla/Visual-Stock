const csrftoken = getCookie('csrftoken');

const contentTable = document.getElementsByClassName("content-table")[0];
const table = contentTable.getElementsByTagName("table")[0];
const editableCells = contentTable.querySelectorAll("td[contenteditable]");

let editedRows = [];
let editedProducts = [];

let intervalDialogModalCounter, timeoutRedirection;
let dialogModal;

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

function setAvailability(editedRow, quantity) {
    let availability = editedRow.getElementsByClassName("product--available")[0];
    if (quantity > 0) {
        availability.innerText = "✓";
        availability.classList.replace("noavailable", "available");
    } else {
        availability.innerText = "X";
        availability.classList.replace("available", "noavailable");
    }
}

function hideDialogModal(){
    dialogModal.style.opacity = "0";
    dialogModal.style.zIndex = "-1";
}

function showDialogModal(){
    dialogModal.style.zIndex = "1";
    dialogModal.style.opacity = "";
}

function stopRedirection(){
    clearInterval(intervalDialogModalCounter);
    clearTimeout(timeoutRedirection);
    hideDialogModal(dialogModal);
    setTimeout(() => {dialogModalCounter.innerText = "3"}, 1100)
}

function runRedirection(){
    clearInterval(intervalDialogModalCounter);
    window.location.href = window.location.href.split("?")[0];
}

function createDialogModal(){
    dialogModal = document.createElement("div");
    let textDialogModal = document.createElement("span");
    let cancelButton = document.createElement("button");

    dialogModal.appendChild(textDialogModal);
    dialogModal.appendChild(cancelButton);
    document.body.appendChild(dialogModal);

    textDialogModal.innerHTML = "Se han realizado los cambios correctamente. "+
                                "Sera redirigido al modo de visualización en <span class='time--redirection'>3</span> segundos.<br><br>"+
                                "Presione cancelar si desea seguir editando.";
    cancelButton.innerText = "Cancelar";

    dialogModal.classList.add("dialog--modal");
    cancelButton.classList.add("cancel-button");

    dialogModal.tabIndex = "0";
    cancelButton.tabIndex = "0";

    cancelButton.addEventListener('click', stopRedirection)

    hideDialogModal(dialogModal);

    return dialogModal

}

function cuentaRegresiva(element) {
    if (element.innerText > 0){
        element.innerText--
    }
}

function saveItems() {
    
    editedRows.forEach((editedRow) => {
        let id = parseInt(editedRow.querySelector("input[type='hidden']").value);
        let name = editedRow.getElementsByClassName("product--name")[0].innerText;
        let price = parseFloat(editedRow.getElementsByClassName("product--price")[0].innerText);
        let quantity = parseInt(editedRow.getElementsByClassName("product--quantity")[0].innerText);
        let category = editedRow.getElementsByClassName("product--category")[0];
        let editedProduct = {id, name, price, quantity};

        setAvailability(editedRow, quantity);
        
        if (category){
            editedProduct["category"] = category.innerText;
        }
        
        editedProducts.push(editedProduct);
    })

    postData();
    editedProducts = [];
}

function postData(){
    const request = new Request(
        url_edit_products,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(editedProducts),
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.error !== null) {
            location.reload(true);
        } else if ((content.error === null) && (editedRows.length !== 0)){
            successData();
        }
    })();
    
}

function successData(){
    showDialogModal();
    intervalDialogModalCounter = setInterval(cuentaRegresiva, 1000, dialogModalCounter)
    timeoutRedirection = setTimeout(runRedirection, 3000)
    dialogModal.focus()
    editedRows = [];
}

function trackEditedRow(){
    for (let editableCell of editableCells) {
        editableCell.addEventListener('input', (e) =>{
            let editedRow = e.target.parentElement;
            if (editedRows.indexOf(editedRow) === -1){
                editedRows.push(editedRow);
            }
        });
    }
}

function reloadBackNavigation(){
    let perEntries = performance.getEntriesByType("navigation")
    if (perEntries[0].type === "back_forward") {
        location.reload(true);
    }
}

reloadBackNavigation();
contentTable.style.paddingTop = "25px";
trackEditedRow();
dialogModal = createDialogModal();
dialogModalCounter = dialogModal.getElementsByClassName("time--redirection")[0];

