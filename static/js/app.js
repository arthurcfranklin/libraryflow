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

// =========================
// Modal Novo Livro
// =========================

const openBookModal = document.getElementById("open-book-modal");
const closeBookModal = document.getElementById("close-book-modal");
const cancelBookModal = document.getElementById("cancel-book-modal");
const bookModal = document.getElementById("book-modal");

if (openBookModal && bookModal) {

    openBookModal.addEventListener("click", () => {
        bookModal.classList.add("active");
    });

    closeBookModal.addEventListener("click", () => {
        bookModal.classList.remove("active");
    });

    cancelBookModal.addEventListener("click", () => {
        bookModal.classList.remove("active");
    });

    bookModal.addEventListener("click", (event) => {
        if (event.target === bookModal) {
            bookModal.classList.remove("active");
        }
    });

}