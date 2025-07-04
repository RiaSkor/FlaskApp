function toggleFields() {
    var categoryId = document.getElementById("id_categories").value;
    var fieldsCategory1And2 = document.getElementById("fields-category-1-2");
    var fieldsCategory3 = document.getElementById("fields-category-3");

    // Скрыть все поля
    fieldsCategory1And2.style.display = "none";
    fieldsCategory3.style.display = "none";

    // Показать нужные поля в зависимости от категории
    if (categoryId == 1 || categoryId == 2) {
        fieldsCategory1And2.style.display = "block";
    } else if (categoryId == 3) {
        fieldsCategory3.style.display = "block";
    }
}
