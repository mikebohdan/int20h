/**
 * Created by mbohdan on 2/28/16.
 */

function onNameFromSubmit() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById("name").innerHTML = JSON.parse(xhttp.responseText)['name'];
        }
    };
    xhttp.open("POST", "/", true);
    xhttp.send({'name': document.forms.yname);

    return false;
}
