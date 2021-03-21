window.addEventListener("pywebviewready", function() {
    window.setTimeout(function() {
        var loading = document.getElementsByClassName("loading")[0];
        loading.style.opacity = 0;
        window.setTimeout(function() {
            loading.style.display = "none";
        }, 2000);
    }, 2000);
});

function sendMessage(msg) {
    pywebview.api.sendMessage(msg);
};