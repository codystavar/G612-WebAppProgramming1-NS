function buttonClickedResponse(resp) {
   console.log("IT WORKS!")
   console.log(resp.body)
}

function buttonClickedError(err) {
    console.log("There was an error");
    console.log(err)
}


function ButtonClicked() {
   
   console.log("Someone clicked me");
   console.log("I am going to get your data");
   fetch('http://dev.thisiloapp.com'),
en(buttonClickedResponse) //o funcite care accepta acel parametru si este de fapt raspunsul serverului, poate fi o lista de date, obiect, string etc.
   .catch(buttonClickedError) // ce se intampla daca e o eroare
   .console.log("I am still waiting")
}
