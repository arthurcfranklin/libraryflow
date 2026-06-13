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

// =========================
// Modal Excluir Livro
// =========================

const deleteModal = document.getElementById("delete-modal");
const cancelDeleteModal = document.getElementById("cancel-delete-modal");
const deleteBookForm = document.getElementById("delete-book-form");
const deleteModalMessage = document.getElementById("delete-modal-message");
const openDeleteButtons = document.querySelectorAll(".open-delete-modal");

openDeleteButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const deleteUrl = button.getAttribute("data-delete-url");
        const bookTitle = button.getAttribute("data-book-title");

        deleteBookForm.setAttribute("action", deleteUrl);
        deleteModalMessage.textContent = `Tem certeza que deseja excluir "${bookTitle}"?`;

        deleteModal.classList.add("active");
    });
});

if (cancelDeleteModal) {
    cancelDeleteModal.addEventListener("click", () => {
        deleteModal.classList.remove("active");
    });
}

if (deleteModal) {
    deleteModal.addEventListener("click", (event) => {
        if (event.target === deleteModal) {
            deleteModal.classList.remove("active");
        }
    });
}

// =========================
// Notificação de Livro Excluído
// =========================

const toast = document.getElementById("toast");

if (toast) {
    setTimeout(() => {
        toast.classList.remove("active");
    }, 2500);
}

// =========================
// Modal Editar Livro
// =========================

const editModal = document.getElementById("edit-book-modal");
const editForm = document.getElementById("edit-book-form");

const editTitle = document.getElementById("edit-title");
const editAuthor = document.getElementById("edit-author");
const editYear = document.getElementById("edit-year");
const editCategory = document.getElementById("edit-category");
const editCopies = document.getElementById("edit-copies");

const cancelEditModal = document.getElementById("cancel-edit-modal");

const editButtons = document.querySelectorAll(".open-edit-modal");

editButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const id = button.dataset.id;

        editTitle.value = button.dataset.title;
        editAuthor.value = button.dataset.author;
        editYear.value = button.dataset.year;
        editCategory.value = button.dataset.category;
        editCopies.value = button.dataset.copies;

        editForm.action = `/books/${id}/edit`;

        editModal.classList.add("active");
    });

});

if (cancelEditModal) {

    cancelEditModal.addEventListener("click", () => {
        editModal.classList.remove("active");
    });

}

if (editModal) {

    editModal.addEventListener("click", (event) => {

        if (event.target === editModal) {
            editModal.classList.remove("active");
        }

    });

}