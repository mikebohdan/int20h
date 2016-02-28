/**
 * Created by mbohdan on 2/28/16.
 */

function onNameFromSubmit() {
    var xhttp = new XMLHttpRequest();
    xhttp.responseType = 'text';

    xhttp.onreadystatechange = function (body) {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            // alert(xhttp.response);
            document.getElementById("name").innerHTML = xhttp.response['name'];
            return xhttp.response;
        }
    };
    xhttp.open("POST", "/", true);
    xhttp.responseType = 'json';
    xhttp.send(JSON.stringify({name: document.getElementById('your_name').value}));

    return false;
}
