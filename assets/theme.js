var currentTheme = "light";
let imgTheme = document.getElementById("img-theme");

function switchTheme() {
    if (currentTheme == "light") {
        document.documentElement.setAttribute('data-theme', 'dark');
        currentTheme = "dark";
        imgTheme.src = "sun.png";
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        currentTheme = "light";
        imgTheme.src = "moon.png";
    }
}