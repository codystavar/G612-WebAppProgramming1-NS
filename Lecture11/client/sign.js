function ifSuccess(reponse) {
    console_log("USER LOGGED IN.")
}

function ifError(error) {
    console.log(error);
}

function signin() {
    const data = {
        email: document.getElementsByName("email")[0].value,
        password: document.getElementsByName("password")[0].value
    }
    console.log(data)
    url = "http://localhost:3006/api/v1/sign-in"
    options = {
        body: JSON.stringify(data),
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    }

    fetch (url,options)
    .then(ifSuccess)
    .catch(ifError)
}