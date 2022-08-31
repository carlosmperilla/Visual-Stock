function getFormDeleteStock(target){
    target.classList.add("collapse")

    let parent = target.parentNode
    let child = parent.firstChild;

    while(child) {
        if (child.nodeType === 1){
            if (child.classList.contains("stock-card__name")) {
                var cardName = child;
            }
            if (child.classList.contains("form__stock-delete")) {
                var formDelete = child;
            }
            if (child.classList.contains("stock-card__cancel_delete")) {
                var cancelButton = child;
            }
        }
        
        child = child.nextElementSibling;
    }

    cardName.style.fontSize = "0";

    formDelete.classList.remove("collapse")
    cancelButton.classList.remove("collapse")

}

function cancelDeleteStock(target){
    target.classList.add("collapse")

    let parent = target.parentNode
    let child = parent.firstChild;

    while(child) {
        if (child.nodeType === 1){
            if (child.classList.contains("stock-card__name")) {
                var cardName = child;
            }
            if (child.classList.contains("form__stock-delete")) {
                var formDelete = child;
            }
            if (child.classList.contains("stock-card__delete-button")) {
                var deleteButton = child;
            }
        }
        
        child = child.nextElementSibling;
    }

    cardName.style.fontSize = null;

    formDelete.classList.add("collapse")
    deleteButton.classList.remove("collapse")
}