const button = document.getElementById("theme-toggle");

if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    button.innerHTML = "☀️";
}

button.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        button.innerHTML = "☀️";
        localStorage.setItem("theme", "dark");
    } else {
        button.innerHTML = "🌙";
        localStorage.setItem("theme", "light");
    }
});