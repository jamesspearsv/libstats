document.addEventListener("DOMContentLoaded", () => {
 
    // fetch latest transaction count from server.
    function fetchUpdates() {
        // Select correct DOM element and get api url
        count = document.querySelector('#count-data')
        counterapiurl = document.querySelector('#counterapi-url').dataset.apiurl

        fetch(counterapiurl)
        .then(response => response.json())
        .then(data => {
            console.log(data.monthlyTransactionCount)
            
            count.innerHTML = data.monthlyTransactionCount
        })
    }

    // set onclick action of refresh button
    document.querySelector('#refresh-button').onclick = fetchUpdates
    
}) 