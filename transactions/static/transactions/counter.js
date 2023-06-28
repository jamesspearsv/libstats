document.addEventListener("DOMContentLoaded", () => {
    
    count = document.querySelector('#count-data')
    counterapiurl = document.querySelector('#counterapi-url').dataset.apiurl
    console.log(counterapiurl)
    
    // fetch latest transaction count from server.
    function fetchUpdates() {
        fetch(counterapiurl)
        .then(response => response.json())
        .then(data => {
            console.log(data.monthlyTransactionCount)
            
            count.innerHTML = data.monthlyTransactionCount
        })
    }

    setInterval(fetchUpdates, 10000)
}) 