function enterToClick(element, clickElement){
    element.addEventListener('keyup', (event) => { 
        if (event.key == "Enter"){clickElement.click()}
    })
}

function clickToFocus(element, focusElement){
    element.addEventListener('click', (event) => { 
        setTimeout(()=>{focusElement.focus()}, 0)
    }, false)
}

function setNextFocus(currentElement, focusElement){
    currentElement.addEventListener('keydown', (event) => {
        if (!event.shiftKey && event.keyCode === 9){ event.preventDefault(); setTimeout(()=>{focusElement.focus()},0) }
    }, false)
}

function setPrevFocus(currentElement, focusElement){
    currentElement.addEventListener('keydown', (event) => {
        if (event.shiftKey && event.keyCode === 9){ event.preventDefault(); setTimeout(()=>{focusElement.focus()},0) }
    }, false)
}

function escapeToAction(element, action){
    element.addEventListener('keydown', (event)=> {
        if (event.key === "Escape") {
            action()
        } })    
}

function initialAccesibility(){
    let footerLabels = document.querySelectorAll("footer label")
    let headerInteractiveIcons = document.querySelectorAll("header .active-hide")
    
    let modalHtu = document.getElementsByClassName('modal__howToUse')[0]
    let htuButtons = modalHtu.querySelectorAll(".button_box .button__model")
    let hasButtons = Boolean(htuButtons.length)
    let firstButtonHtu = htuButtons[0]
    let lastButtonHtu = htuButtons[htuButtons.length-1]
    let closeButtonHtu = modalHtu.querySelector(".modal__close-button")
    let descriptionHtu = modalHtu.querySelector(".section__description")
    
    let modalCm = document.getElementsByClassName('modal__contactMe')[0]
    let descriptionCm = modalCm.querySelector(".section__description")
    let closeButtonCm = modalCm.querySelector(".modal__close-button")
    
    for (let label of footerLabels) {
        enterToClick(label, label)
        if (label.getAttribute("for") === "howToUse"){
            if (hasButtons) {
                clickToFocus(label, firstButtonHtu)
            } else {
                clickToFocus(label, descriptionHtu)
            }
        }
        if (label.getAttribute("for") === "contactMe"){
            clickToFocus(label, descriptionCm)
        }
    }
    
    if (hasButtons){
        for (buttonHtu of htuButtons){
            let linkInButton = buttonHtu.getElementsByTagName("a")[0]
            enterToClick(buttonHtu, linkInButton)
        }
        setNextFocus(lastButtonHtu, closeButtonHtu)
    } else {
        setNextFocus(descriptionHtu, closeButtonHtu)
    }
    
    enterToClick(closeButtonHtu, closeButtonHtu)

    setNextFocus(descriptionCm, closeButtonCm)
    enterToClick(closeButtonCm, closeButtonCm)

    for (let iIcon of headerInteractiveIcons) {
        enterToClick(iIcon, iIcon)
    }

    escapeToAction(modalHtu, ()=>{closeButtonHtu.click()} )
    escapeToAction(modalCm, ()=>{closeButtonCm.click()} )
}

initialAccesibility()