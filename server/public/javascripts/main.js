let rightButton = document.getElementById("right")
let leftButton = document.getElementById("left")
let feedButton = document.getElementById("feed")



feedButton.addEventListener("click", () => {
    console.log("Feeding")
    fetch("/feed").then( res =>
        console.log(res.status)
    )
})

rightButton.addEventListener("click", () => {
    console.log("Moving right")
    fetch("/right").then( res =>
        console.log(res.status)
    )
})

leftButton.addEventListener("click", () => {
    console.log("Moving left")
    fetch("/left").then( res =>
        console.log(res.status)
    )
})
