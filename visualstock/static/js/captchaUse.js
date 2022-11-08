const csrftoken = getCookie('csrftoken');
const modalCaptcha = document.querySelector(".d--modal");
const modalCaptchaClose = modalCaptcha.getElementsByClassName('close__dialog')[0];
const captchaImg = document.getElementById("captcha--img");
const captchaState = document.getElementsByClassName("captcha--state")[0];
const captchaInput = document.querySelector(".captcha--box__input input[type='text']");
const captchaSend = document.querySelector(".captcha--box__input button");
const signupForm = document.getElementById('form__signup');
const hiddenCaptcha = signupForm.querySelector("input[name='captcha']");
const renewCaptchaButton = document.getElementById("renew-captcha__button");

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

function showModalCaptcha(){
    modalCaptcha.showModal()
    captchaInput.focus()
}

function closeModalCaptcha(event){
    if (event.target == modalCaptcha){
        modalCaptcha.close();
    }
}

function restartCounter(){
    let counter = captchaState.getElementsByTagName("span")[0]
    captchaInput.value = ""
    if (counter !== undefined){
        counter.innerText = 3;
    }
}

function errorCaptcha(){
    let counter = captchaState.getElementsByTagName("span")[0]
    if (counter === undefined){
        captchaState.style.display = "block";
        captchaState.innerHTML = "Intente otra vez. Tiene <span>2</span> intentos más"
    } else {
        let valueCounter = parseInt(counter.innerText)
        if (valueCounter > 1) {
            counter.innerText--
        } else {
            counter.innerText = 3
            captchaInput.value = ""
        }
    }
}

function successCaptcha(){
    captchaState.classList.add("success");
    captchaState.style.display = "block";
    captchaState.innerHTML = "Genial! Se validaran los datos y sera redireccionado a la pagina principal"
}

function renewCaptcha(){
    const request = new Request(
        url_renew_captcha,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

    renewCaptchaButton.disabled = true;
    renewCaptchaButton.style.filter = "grayscale(1)";
    renewCaptchaButton.classList.remove("enabled");
   

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();
        setTimeout(
            () => {
                captchaImg.src = content.captcha_img;
                restartCounter();
                renewCaptchaButton.disabled = "";
                renewCaptchaButton.style.filter = "";
                renewCaptchaButton.classList.add("enabled");
            }, 1000
        );

        }
    )();
}

function sendCaptcha(){
    const request = new Request(
        url_review_captcha,
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'captcha_input' : captchaInput.value }),
            mode: 'same-origin' // Do not send CSRF token to another domain.
        }
            );

   

    (async () => {
        const rawResponse = await fetch(request);
        const content = await rawResponse.json();

        if (content.captcha_state === 'success'){
            successCaptcha()
            hiddenCaptcha.value = captchaInput.value;
            signupForm.submit()
        } else {
            captchaInput.focus()
            errorCaptcha()
            if (content.captcha_img !== undefined){
                captchaImg.src = content.captcha_img;
            }
        }

        }
    )();
}


modalCaptcha.addEventListener('click', closeModalCaptcha)
modalCaptchaClose.addEventListener('click', ()=>{modalCaptcha.close()})
enterToClick(captchaInput, captchaSend)