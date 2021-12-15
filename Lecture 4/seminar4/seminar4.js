// cancel
function cancel() {

const container = document.getElementById("container")
const div = document.createElement("div");
const p = document.createElement("p");
p.innerText = "Warning! "
p.style.fontSize = "20px";
p.style.color = 'red';
div.appendChild(p);
container.appendChild(div);
}