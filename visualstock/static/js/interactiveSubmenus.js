let navStockCreados = document.getElementsByClassName('li__created-stocks')[0]
let navModesStocks = document.getElementsByClassName('li__modes-stocks')[0]
let navUserButton = document.getElementsByClassName('li__user-button')[0]
let navBackupStocks = document.getElementsByClassName('li__backup-stocks')
let body = document.getElementsByTagName("body")[0]

function hideSubmenu(element){
        element.getElementsByTagName('ul')[0].style.visibility = null; 
        element.getElementsByTagName('ul')[0].style.opacity = null;
    }

function showSubmenu(element){
    element.getElementsByTagName('ul')[0].style.visibility = "visible"; 
    element.getElementsByTagName('ul')[0].style.opacity = 1;
}

function showOrHideSubMenu(element){
    let eVisibility = element.getElementsByTagName('ul')[0].style.visibility
    if (eVisibility === "") {
        showSubmenu(element)
    } else {
        hideSubmenu(element)
    }
}

function enterToAction(element, action){
    element.addEventListener("keydown", (event) => { 
        if( event.key === "Enter" ){ action(element) } 
    })
}

function hideSubmenuAll(){
    hideSubmenu(navStockCreados)
    hideSubmenu(navUserButton)
    if (navModesStocks !== undefined){
        hideSubmenu(navModesStocks)
    }
    for (let item of navBackupStocks){
        hideSubmenu(item)
    }
}

enterToAction(navStockCreados, showOrHideSubMenu)
enterToAction(navUserButton, showOrHideSubMenu)
if (navModesStocks !== undefined){
    enterToAction(navModesStocks, showOrHideSubMenu)
}

for (let item of navBackupStocks){
    enterToAction(item, showOrHideSubMenu)
}

body.addEventListener("click", (event) => {
    hideSubmenuAll()
}, false)

escapeToAction(body, hideSubmenuAll)