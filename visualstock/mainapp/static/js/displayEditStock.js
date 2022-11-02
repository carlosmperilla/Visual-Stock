function getFormEditStock(target){
    target.classList.add("collapse")

    let parent = target.parentNode
    let cardName = parent.getElementsByClassName("stock-card__name")[0]
    let formEdit = parent.getElementsByClassName("form__stock-edit")[0]
    let cancelButton = parent.getElementsByClassName("stock-card__cancel_edit")[0]

    cardName.style.fontSize = "0";

    formEdit.classList.remove("collapse")
    cancelButton.classList.remove("collapse")

    formEdit.querySelector("input[type='text']").focus()

}

function cancelEditStock(target){
    target.classList.add("collapse")

    let parent = target.parentNode
    let cardName = parent.getElementsByClassName("stock-card__name")[0]
    let formEdit = parent.getElementsByClassName("form__stock-edit")[0]
    let editButton = parent.getElementsByClassName("stock-card__edit-button")[0]

    cardName.style.fontSize = null;

    formEdit.classList.add("collapse")
    editButton.classList.remove("collapse")
}

function getFile(target) {
    let parent_of_parent = target.parentNode.parentNode

    inputFile = parent_of_parent.querySelector("input[type='file']")

    inputFile.click()
    
}

function uploadFilePutNameNoId(target) {
    var parentTarget = target.parentNode
    var selectorFileNameTextBox = ".upload-file__interfaz .upload-file__filename";
    var UploadFileNameField = parentTarget.querySelector(selectorFileNameTextBox);
    UploadFileNameField.innerHTML = target.files[0].name;
}