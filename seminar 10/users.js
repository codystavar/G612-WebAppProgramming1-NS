function reponseReceived(response) {
    return reponse.json()
}

function processReponse(response) {
    console.log(response):
}


function getusersData(){
    url = "http://localhost:3005/users"
    reponse = fetch()
        .then(reponseReceived)
        .then(processResponse)
        .catch(errorReceived);

}