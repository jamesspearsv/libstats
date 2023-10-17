document.addEventListener('DOMContentLoaded', () => {

    const removeAlert = () => {
      console.log("run!")
      const alert = document.getElementById('alert')

      if (alert) {
          alert.style.opacity = '0' 
          alert.addEventListener('transitionend', () => {
              alert.remove()
            })
        } else {
         console.log('removed')
        console.log('not removed!')
        return 
      }
    }
  
    setTimeout(removeAlert, 10000)

  })