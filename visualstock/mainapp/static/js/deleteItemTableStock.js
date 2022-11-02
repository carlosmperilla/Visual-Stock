const csrftoken = getCookie('csrftoken');

const contentTable = document.getElementsByClassName("content-table")[0];
const deleteCheckboxes = contentTable.getElementsByClassName("delete--item");
const deleteCounter = document.getElementsByClassName("delete--counter")[0];

let removableIdItems = [];
let removableItems = [];
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

function checkToAction(checkbox, action){
    checkbox.addEventListener("change", (e) => {
            action(e.target)
    });
}

function changeDeleteCounter(checkboxItem){
    let isChecked = checkboxItem.checked
    if (isChecked) {
        deleteCounter.innerText++
    } else {
        deleteCounter.innerText--
    }
}

function pushOrPopRemovableIdItem(removableItem){
    let idItem = parseInt(removableItem.id.replace("item-", ""))
    if (removableItem.checked) {
        removableItems.push(removableItem.closest("tr"));
        removableIdItems.push(idItem);
    } else {
        removableItems = removableIdItems.filter(item => item !== removableItem.closest("tr"));
        removableIdItems = removableIdItems.filter(id => id !== idItem);
    }
}

function trackRemovableItems(){
    for (let deleteCheckbox of deleteCheckboxes) {
        enterToClick(deleteCheckbox, deleteCheckbox);
        checkToAction(deleteCheckbox, changeDeleteCounter);
        checkToAction(deleteCheckbox, pushOrPopRemovableIdItem);
    }
}

function postData(){
    const request = new Request(
        url_delete_products,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(removableIdItems),
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.error !== null) {
            location.reload(true);
        } else if ((content.error === null) && (removableIdItems.length !== 0)){
            successData();
        }
    })();
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

    textDialogModal.innerHTML = "Se han eliminado los productos correctamente. "+
                                "Sera redirigido al modo de visualización en <span class='time--redirection'>3</span> segundos.<br><br>"+
                                "Presione cancelar si desea seguir eliminando.";
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

function removeCurrentItems(){
    for(let removableItem of removableItems){
        removableItem.style.transition = ".7s";
        removableItem.style.opacity = "0";

        setTimeout(() => removableItem.remove(), 750);
    }
}

function successData(){
    showDialogModal();
    intervalDialogModalCounter = setInterval(cuentaRegresiva, 1000, dialogModalCounter)
    timeoutRedirection = setTimeout(runRedirection, 3000)
    dialogModal.focus()
    removableIdItems = [];
    removeCurrentItems();
    deleteCounter.innerText = "0";
}

function deleteItems(){
    let totalRemovableItem = removableIdItems.length;
    if (totalRemovableItem <= 0){
        return null;
    }
    let confirmRemove = window.confirm(`¿Desea eliminar ${totalRemovableItem} productos?`)
    if (confirmRemove) {
        postData();
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
trackRemovableItems();
dialogModal = createDialogModal();
dialogModalCounter = dialogModal.getElementsByClassName("time--redirection")[0];