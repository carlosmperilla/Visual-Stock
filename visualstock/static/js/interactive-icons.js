const theme = document.getElementById("theme");
const displayNavBarCheckbox = document.getElementById("display_nav");
const changeColorThemeCheckbox = document.getElementById("changeColorTheme");
const tableModeToSeparateRowCheckbox = document.getElementById("tableSeparateRows");
const tableModeToCardCheckbox = document.getElementById("tableCards");
const tableModeButton = document.getElementById("tableModeButton");

function persistHideDistractions(){
    localStorage.setItem("hide-distractions", displayNavBarCheckbox.checked);
}

function changeColorTheme(){
    if (changeColorThemeCheckbox.checked) {
        theme.href = dark_theme;
    } else {
        theme.href = light_theme;
    }
    localStorage.setItem("dark-mode", changeColorThemeCheckbox.checked);
}

function defaultColorTheme(){
    changeColorThemeCheckbox.checked = window.matchMedia("(prefers-color-scheme: dark)").matches;
}

function selectedColorTheme(){
    changeColorThemeCheckbox.checked = JSON.parse(localStorage.getItem("dark-mode"));
}

function changeTableMode(){
    let iconTableModeButton = tableModeButton.getElementsByTagName("span")[0]
    if (iconTableModeButton.classList.replace("icon-table", "icon-table2")){
        tableModeToSeparateRowCheckbox.checked = true;
        localStorage.setItem("table-mode", 1)
    } else if (iconTableModeButton.classList.replace("icon-table2", "icon-newspaper")){
        tableModeToCardCheckbox.checked = true;
        localStorage.setItem("table-mode", 2)
    } else if (iconTableModeButton.classList.replace("icon-newspaper", "icon-table")){
        tableModeToSeparateRowCheckbox.checked = false;
        tableModeToCardCheckbox.checked = false;
        localStorage.setItem("table-mode", 0)
    }
}

function persistTableMode(){
    switch (localStorage.getItem("table-mode")){
        case "1":
            changeTableMode();
            break;
        case "2":
            changeTableMode();
            changeTableMode();
            break;
    }

}

if (localStorage.getItem("hide-distractions") === null){
    persistHideDistractions()
} else {
    displayNavBarCheckbox.checked = JSON.parse(localStorage.getItem("hide-distractions"));
}

if (localStorage.getItem("dark-mode") === null){
    defaultColorTheme();
} else {
    selectedColorTheme();
}

if ((localStorage.getItem("table-mode") !== null) && (tableModeButton)){
    persistTableMode();
}

changeColorTheme();
changeColorThemeCheckbox.addEventListener("click", changeColorTheme);
displayNavBarCheckbox.addEventListener("click", persistHideDistractions);

if (tableModeButton) {
    tableModeButton.addEventListener("click", changeTableMode);
}