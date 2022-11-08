const contentTable = document.getElementsByClassName("content-table")[0];

let dialogFilter = document.querySelector(".filter--modal");
let formFilter = dialogFilter.querySelector(".form--filter");
let checksInput = formFilter.querySelectorAll("input[type='checkbox']");
let rangesInput = formFilter.querySelectorAll("input[type='range']");
let nameOptions = document.getElementsByClassName("product--name");
let categoryOptions = document.getElementsByClassName("product--category");
let priceRange = document.getElementsByClassName("product--price");
let quantityRange = document.getElementsByClassName("product--quantity");
let minPriceInput = document.getElementById("price__range--min");
let maxPriceInput = document.getElementById("price__range--max");
let minQuantityInput = document.getElementById("quantity__range--min");
let maxQuantityInput = document.getElementById("quantity__range--max");
let minPrice, maxPrice, minQuantity, maxQuantity;
let namesArray = [], categoriesArray = [];

function toggleDisposition(event) {
    let nextElement = event.target.nextElementSibling
    while (nextElement !== null) {
        if (nextElement.tagName === "INPUT") {
            nextElement.disabled = !event.target.checked
            console.log(nextElement)
            console.log(event.target)
        }
        nextElement = nextElement.nextElementSibling
    }
}

function visualRange(event) {
    let prevElement = event.target.previousElementSibling
    while (prevElement !== null) {
        if (prevElement.tagName === "SPAN") {
            prevElement.innerText = event.target.value
            break
        }
    }
}

function fillDataListById(collection, id, array){
    let datalist = document.getElementById(id);
    for (let element of collection){
        let option = document.createElement('option');
        option.innerText = element.innerText;
        array.push(element.innerText);
        datalist.appendChild(option)
    }
}

function getMinPrice(){
    let auxMin = Infinity;
    for (let priceElement of priceRange){
        price = parseFloat(priceElement.innerText.replace(",", "."));
        if (price < auxMin) {
            auxMin = price
        }
    }
    minPrice = auxMin;
}

function getMaxPrice(){
    let auxMax = -Infinity;
    for (let priceElement of priceRange){
        price = parseFloat(priceElement.innerText.replace(",", "."));
        if (price > auxMax) {
            auxMax = price
        }
    }
    maxPrice = auxMax;
}

function getMinQuantity(){
    let auxMin = Infinity;
    for (let priceElement of quantityRange){
        price = parseInt(priceElement.innerText);
        if (price < auxMin) {
            auxMin = price
        }
    }
    minQuantity = auxMin;
}

function getMaxQuantity(){
    let auxMax = -Infinity;
    for (let priceElement of quantityRange){
        price = parseInt(priceElement.innerText);
        if (price > auxMax) {
            auxMax = price
        }
    }
    maxQuantity = auxMax;
}

function setRangePrice(){
    let minRange = document.getElementById("price__range--min");
    let maxRange = document.getElementById("price__range--max");
    let spanMinRange = document.querySelector(".price__range--min_value");
    let spanMaxRange = document.querySelector(".price__range--max_value");

    maxRange.min = minRange.min = minPrice;
    maxRange.max = minRange.max = maxPrice;

    spanMinRange.innerText = minRange.value = minPrice;
    spanMaxRange.innerText = maxRange.value = maxPrice;

    minRange.addEventListener("change", (event) => {
        maxRange.min = event.target.value;
    })
    maxRange.addEventListener("change", (event) => {
        minRange.max = event.target.value;
    })
}

function setRangeQuantity(){
    let minRange = document.getElementById("quantity__range--min");
    let maxRange = document.getElementById("quantity__range--max");
    let spanMinRange = document.querySelector(".quantity__range--min_value");
    let spanMaxRange = document.querySelector(".quantity__range--max_value");

    maxRange.min = minRange.min = minQuantity;
    maxRange.max = minRange.max = maxQuantity;

    spanMinRange.innerText = minRange.value = minQuantity;
    spanMaxRange.innerText = maxRange.value = maxQuantity;

    minRange.addEventListener("change", (event) => {
        maxRange.min = event.target.value;
    })
    maxRange.addEventListener("change", (event) => {
        minRange.max = event.target.value;
    })
}

function applyFilter(){
    let rows = document.querySelectorAll("tbody tr");
    let nameFilterCheck = document.getElementById("apply--name_filter");
    let categoryFilterCheck = document.getElementById("apply--category_filter");
    let priceFilterCheck = document.getElementById("apply--price_filter");
    let quantityFilterCheck = document.getElementById("apply--quantity_filter");
    let nameChoosed = document.getElementById("product__name");
    let categoryChoosed = document.getElementById("product__category");
    
    for (let row of rows){
        if (nameFilterCheck.checked){
            let name = row.getElementsByClassName("product--name")[0].innerText
            if (name !== nameChoosed.value) {
                row.style.display = "none";
                continue
            }
        }
        if (categoryFilterCheck !== null && categoryFilterCheck.checked) {
            let category = row.getElementsByClassName("product--category")[0].innerText
            if (category !== categoryChoosed.value) {
                row.style.display = "none";
                continue
            }
        }
        if (priceFilterCheck.checked){
            let price = parseFloat(row.getElementsByClassName("product--price")[0].innerText);
            if (!(minPriceInput.value <= price && maxPriceInput.value >= price)) {
                row.style.display = "none";
                continue
            }
        }
        if (quantityFilterCheck.checked){
            let quantity = parseFloat(row.getElementsByClassName("product--quantity")[0].innerText);
            if (!(minQuantityInput.value <= quantity && maxQuantityInput.value >= quantity)) {
                row.style.display = "none";
                continue
            }
        }
    }
    dialogFilter.close()

}


function closeDialogFilter(event){

    if (event.target == dialogFilter){
        dialogFilter.close();
    }
}



contentTable.style.paddingTop = "25px";
dialogFilter.addEventListener('click', closeDialogFilter)

for (let checkInput of checksInput) {
    checkInput.addEventListener("change", (event) => {toggleDisposition(event)})
}

for (let rangeInput of rangesInput) {
    rangeInput.addEventListener("change", (event) => {visualRange(event)})
}

fillDataListById(nameOptions, "product__names", namesArray)

if (categoryOptions.length !== 0){
    fillDataListById(categoryOptions, "product__categories", categoriesArray)
}

getMinPrice()
getMinQuantity()
getMaxPrice()
getMaxQuantity()

setRangePrice()
setRangeQuantity()