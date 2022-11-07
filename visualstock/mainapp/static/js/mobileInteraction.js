let burgerButtonMenu = document.querySelector("header .burger-button--content button")
let navMenu = document.querySelector("header nav")
let backupListItems = document.getElementsByClassName("li__backup")

function openMenu() {
    burgerButtonMenu.classList.toggle("icon-menu3")
    burgerButtonMenu.classList.toggle("icon-menu4")
    burgerButtonMenu.classList.toggle("show--nav__menu")
    navMenu.classList.toggle("show--nav__menu")
}

function createAvaliableLink(url, isDownloadLink){
    let link = document.createElement('a');
    link.href = url;
    if (isDownloadLink){
        link.setAttribute("download", "")
    }
    document.body.appendChild(link); // Required for Firefox
    link.click();
    link.remove(); 
}

function clickBackupAdvise(event) {
    let confirmBackupAction, linkByClick
    if (event.target.tagName === "A") {
        if (window.innerWidth <= 650){
            event.preventDefault()
        }
        
        return null
    }
    event.preventDefault()
    
    linkByClick = event.target.getElementsByTagName("a")[0];
    confirmBackupAction = window.confirm(`¿Seguro desea respaldar ${linkByClick.text.trim()}?`)
    if (confirmBackupAction) {
        let isDownloadLink = linkByClick.getAttribute("download") !== null
        createAvaliableLink(linkByClick.href, isDownloadLink)
    }
}

burgerButtonMenu.addEventListener('click', openMenu)

for (listItem of backupListItems){
    listItem.addEventListener('click', clickBackupAdvise)
}