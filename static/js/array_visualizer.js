let step = 0

function drawArray(arr){

let container = document.getElementById("array-container")

container.innerHTML=""

arr.forEach(value => {

let bar = document.createElement("div")

bar.className="bar"

bar.style.height = value*10 + "px"

bar.innerText = value

container.appendChild(bar)

})

}


function startAnimation(){

step = 0

animate()

}


function animate(){

if(step >= states.length) return

drawArray(states[step])

step++

setTimeout(animate,800)

}