function hideAlertMessage() {
    var alert_node = document.getElementsByClassName("alert")[0];
    alert_node.style.opacity = "0";
    window.setTimeout(function() {
        document.body.removeChild(alert_node);
    }, 1000);
}

function showAlertMessage(message) {
    var temp = document.getElementsByClassName("alert-template")[0];
    var alert_frag = temp.content.cloneNode(true);
    document.body.appendChild(alert_frag);
    var alert_node = document.getElementsByClassName("alert")[0];
    alert_node.querySelector("h4").innerHTML = message
    window.setTimeout(function() {
        alert_node.style.opacity = 1;
    }, 100);
}