var alerts = 0;

function hideAlertMessage() {
    var nodes = document.getElementsByClassName("alert")
    var alert_node = nodes[nodes.length-1];
    alert_node.style.opacity = "0";
    window.setTimeout(function() {
        document.body.removeChild(alert_node);
    }, 1000);
}

function showAlertMessage(message) {
    var my_id = alerts.toString();
    alerts += 1;
    var temp = document.getElementsByClassName("alert-template")[0];
    var alert_frag = temp.content.cloneNode(true);
    var alert_node = alert_frag.querySelector(".alert");
    alert_node.id = my_id;
    alert_node.querySelector("h4").innerHTML = message
    document.body.appendChild(alert_frag);
    window.setTimeout(function() {
        alert_node.style.opacity = 1;
    }, 100);
}