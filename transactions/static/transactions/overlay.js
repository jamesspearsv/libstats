document.addEventListener("DOMContentLoaded", () => {
    let overlayButtons = document.querySelectorAll(".overlay-button")
   
    overlayButtons.forEach((button) => { button.addEventListener("click", 
    () => {
        console.log("Clicked!")
        document.querySelector("#overlay").classList.toggle('disabled') 
        })
    })
})