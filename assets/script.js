//MESSAGE FUNCTIONS
function isEmpty(str) {
    return (!str || 0 === str.length);
}

function sendMessage(msg) {
    pywebview.api.sendMessage(msg)
}

function getValueFromInput(clear=true) {
    msg = document.getElementById("msg-txt");
    data = msg.value;
    if (clear) {
        msg.value = "";
    }
    return data;
}

function addMessage(message, mine, date, sender="") {
    if (isEmpty(message)) return;
    var log = document.getElementsByClassName("log")[0]
    var box = document.getElementsByClassName("text-area")[0]

    var messagecontainer = document.createElement("div");
    if (mine == "true") {
        messagecontainer.className = "message-container message-mine";
    } else {
        messagecontainer.className = "message-container message-other";
        var h4 = document.createElement("h4")
        h4.innerHTML = sender
        messagecontainer.appendChild(h4)
    }
    

    var messagebox = document.createElement("div");
    messagebox.className = "message";
    messagebox.innerHTML = message;

    messagecontainer.appendChild(messagebox)
    log.appendChild(messagecontainer);

    box.scrollTop = box.scrollHeight;
}

//CONNECTION EVENTS
function connect() {
    setLoadingText("CONNECTING");
    showLoading();
    var username_node = document.getElementById("username");
    var ip_node = document.getElementById("ip");

    const username = username_node.value;
    const ip = ip_node.value;

    pywebview.api.createConnection({"addr": ip, "username": username}).then(function(response){
        if (response == "success") {
            setLoadingText("CONNECTED");
            hideLoading();
            hideLogin();
            whenConnected();
        } else {
            showAlertMessage(response);
            hideLoading();
        }
    });
}

function whenConnected() {
    var input = document.getElementById("msg-txt");
    input.addEventListener("keydown", ({key}) => {
        if (key === "Enter") {
            sendMessage(getValueFromInput())
        }
    });

    var sndbtn = document.getElementById("snd-btn");
    sndbtn.addEventListener("click", function(){
        sendMessage(getValueFromInput())
    });
}

function disconnect() {
    setLoadingText("DISCONNECTED");
    showLoading();
    showLogin();
    hideLoading();
    pywebview.api.dropConnection();
}

function disconnection(message) {
    setLoadingText("CONNECTION LOST");
    showLoading();
    showLogin();
    showAlertMessage(message)
    hideLoading();
}



//LOADING PAGE
function showLoading() {
    var loading = document.getElementsByClassName("loading")[0];
    loading.style.display = "flex";
    
    window.setTimeout(function() {
        loading.style.opacity = 1;
    }, 100);
}

function hideLoading() {
    window.setTimeout(function() {
        var loading = document.getElementsByClassName("loading")[0];
        loading.style.opacity = 0;
        window.setTimeout(function() {
            loading.style.display = "none";
        }, 1000);
    }, 1000);
}

function setLoadingText(text) {
    var loading = document.getElementsByClassName("loading")[0].querySelector("h1");
    loading.innerHTML = text;
}


//LOGIN PAGE
let inputs = document.getElementsByClassName("login-values")

for (let i in inputs) {
    inputs[i].addEventListener("keydown", ({key}) => {
        if (key === "Enter") {
            connect();
        }
    });
}

function showLogin() {
    window.setTimeout(function() {
        var login_node = document.getElementsByClassName("login")[0];
        login_node.style.display = "flex";
    }, 1000);
}

function hideLogin() {
    window.setTimeout(function() {
        var login_node = document.getElementsByClassName("login")[0];
        login_node.style.display = "none";
    }, 1000);
}