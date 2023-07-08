document.addEventListener("DOMContentLoaded", () => {
    
    function overlayToggle () {
        let overlay = document.querySelector("#overlay")
        console.log("Clicked!")

        if (overlay.style.display == "none") {
            overlay.style.display = "block"
        } else {
            overlay.style.display = "none"
        }
    }

    let overlayButtons = document.querySelectorAll(".overlay-button")
    
    overlayButtons.forEach( (button) => { button.addEventListener("click", overlayToggle)})
    console.log(overlayButtons)
})