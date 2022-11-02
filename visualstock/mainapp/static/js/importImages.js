const dialogModalImportImages = document.getElementsByClassName('d--modal')[0];
const dialogModalImportImagesClose = dialogModalImportImages.getElementsByClassName('close__dialog')[0];
const formImportImages = document.getElementById("form--import_images");
const zipInput = formImportImages.querySelector("input[name='zip']");
const imagesInput = formImportImages.querySelector("input[name='images']");

function showDialogImportImages(){
    dialogModalImportImages.showModal();
}

function closeDialogImport(event){
    if (event.target == dialogModalImportImages){
        dialogModalImportImages.close();
    }
}

function uploadZip(){
    zipInput.click()
}

function uploadImages(){
    imagesInput.click()
}

dialogModalImportImages.addEventListener('click', closeDialogImport)
dialogModalImportImagesClose.addEventListener('click', ()=>{dialogModalImportImages.close()})

zipInput.addEventListener('change', () => {
    dialogModalImportImages.querySelector("button[onclick='uploadImages()']").disabled = true;
    formImportImages.submit();
})
imagesInput.addEventListener('change', () => {
    dialogModalImportImages.querySelector("button[onclick='uploadZip()']").disabled = true;
    formImportImages.submit();
})
