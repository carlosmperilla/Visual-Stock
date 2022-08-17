const theme = document.getElementById("theme");
const displayNavBarCheckbox = document.getElementById("display_nav");
const changeColorThemeCheckbox = document.getElementById("changeColorTheme");

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

changeColorTheme();
changeColorThemeCheckbox.addEventListener("click", changeColorTheme);
displayNavBarCheckbox.addEventListener("click", persistHideDistractions);