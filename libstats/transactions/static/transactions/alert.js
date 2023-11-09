document.addEventListener('DOMContentLoaded', () => {

    const removeAlert = () => {
      const alert = document.getElementById('alert')

      if (alert) {
          alert.style.opacity = '0' 
          alert.addEventListener('transitionend', () => {
            alert.remove()
            })
        } else {
        return 
      }
    }
  
    setTimeout(removeAlert, 10000)

  })