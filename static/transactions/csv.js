function tabletocsv() {
    console.log('clicked')
    var csvdata = [];

    var rows = document.getElementsByTagName('tr');
    for (var i=0; i < rows.length; i++) {
        var cols = rows[i].getElementsByTagName('th','td');
        console.log(cols)

        var csvrows = [];
        for (var j = 0; j < cols.length; j++) {

            csvrows.push(cols.[j].innerHTML);
            console.log(csvrows)
        }

    }
}

document.getElementById('downloadbutton').addEventListener('click', tabletocsv)