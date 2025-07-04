
document.addEventListener('DOMContentLoaded', function() {


// 1 модальное окно
document.getElementById('openModal1').addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем переход по умолчанию
    // Логика для открытия первого модального окна
    const modal1 = document.getElementById('myModal1');
    modal1.style.display = 'block'; // Открываем модальное окно
});


// 2 модальное окно
document.getElementById('openModal2').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior
    const modal2 = document.getElementById('myModal2');
    modal2.style.display = 'block'; // Open the modal
});


// 3 модальное окно
document.getElementById('openModal3').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior
    const modal3 = document.getElementById('myModal3');
    modal3.style.display = 'block'; // Open the modal
});


// 4 модальное окно
document.getElementById('openModal4').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior
    const modal4 = document.getElementById('myModal4');
    modal4.style.display = 'block'; // Open the modal
});


// 5 модальное окно
document.getElementById('openModal5').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior
    const modal5 = document.getElementById('myModal5');
    modal5.style.display = 'block'; // Open the modal
});






// 1 модальное окно
document.getElementById('addInputField1').addEventListener('click', function() {
    const tableBody = document.getElementById('materialTableBody');
    const newRow = document.createElement('tr');

    // Создаем новые ячейки для новой строки
    const idCell = document.createElement('td');
    const materialCell = document.createElement('td');

    // Генерируем уникальный ID для нового поля материала
    const newId = tableBody.children.length; // Используем количество существующих строк как ID

    idCell.textContent = ''; // Оставляем ячейку ID пустой для новых материалов

    // Создаем поле ввода для нового типа материала
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = `new_material_${newId}`; // Уникальное имя для поля
    newInput.id = `new_material_${newId}`; // Уникальный ID для поля
    materialCell.appendChild(newInput);

    // Добавляем ячейки в новую строку
    newRow.appendChild(idCell);
    newRow.appendChild(materialCell);

    // Добавляем новую строку в тело таблицы
    tableBody.appendChild(newRow);
});


// 2 модальное окно
document.getElementById('addInputField2').addEventListener('click', function() {
    const tableBody = document.getElementById('MethodApplicationTableBody');
    const newRow = document.createElement('tr');

    // Создаем новые ячейки для новой строки
    const idCell = document.createElement('td');
    const materialCell = document.createElement('td');

    // Генерируем уникальный ID для нового поля материала
    const newId = tableBody.children.length; // Используем количество существующих строк как ID

    idCell.textContent = ''; // Оставляем ячейку ID пустой для новых материалов

    // Создаем поле ввода для нового типа материала
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = `new_material_${newId}`; // Уникальное имя для поля
    newInput.id = `new_material_${newId}`; // Уникальный ID для поля
    materialCell.appendChild(newInput);

    // Добавляем ячейки в новую строку
    newRow.appendChild(idCell);
    newRow.appendChild(materialCell);

    // Добавляем новую строку в тело таблицы
    tableBody.appendChild(newRow);
});


// 3 модальное окно
document.getElementById('addInputField3').addEventListener('click', function() {
    const tableBody = document.getElementById('ColoringAgentTableBody');
    const newRow = document.createElement('tr');

    // Создаем новые ячейки для новой строки
    const idCell = document.createElement('td');
    const materialCell = document.createElement('td');

    // Генерируем уникальный ID для нового поля материала
    const newId = tableBody.children.length; // Используем количество существующих строк как ID

    idCell.textContent = ''; // Оставляем ячейку ID пустой для новых материалов

    // Создаем поле ввода для нового типа материала
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = `new_material_${newId}`; // Уникальное имя для поля
    newInput.id = `new_material_${newId}`; // Уникальный ID для поля
    materialCell.appendChild(newInput);

    // Добавляем ячейки в новую строку
    newRow.appendChild(idCell);
    newRow.appendChild(materialCell);

    // Добавляем новую строку в тело таблицы
    tableBody.appendChild(newRow);
});


// 4 модальное окно
document.getElementById('addInputField4').addEventListener('click', function() {
    const tableBody = document.getElementById('ColorTableBody');
    const newRow = document.createElement('tr');

    // Создаем новые ячейки для новой строки
    const idCell = document.createElement('td');
    const materialCell = document.createElement('td');

    // Генерируем уникальный ID для нового поля материала
    const newId = tableBody.children.length; // Используем количество существующих строк как ID

    idCell.textContent = ''; // Оставляем ячейку ID пустой для новых материалов

    // Создаем поле ввода для нового типа материала
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = `new_material_${newId}`; // Уникальное имя для поля
    newInput.id = `new_material_${newId}`; // Уникальный ID для поля
    materialCell.appendChild(newInput);

    // Добавляем ячейки в новую строку
    newRow.appendChild(idCell);
    newRow.appendChild(materialCell);

    // Добавляем новую строку в тело таблицы
    tableBody.appendChild(newRow);
});


// 5 модальное окно
document.getElementById('addInputField5').addEventListener('click', function() {
    const tableBody = document.getElementById('GlossTableBody');
    const newRow = document.createElement('tr');

    // Создаем новые ячейки для новой строки
    const idCell = document.createElement('td');
    const materialCell = document.createElement('td');

    // Генерируем уникальный ID для нового поля материала
    const newId = tableBody.children.length; // Используем количество существующих строк как ID

    idCell.textContent = ''; // Оставляем ячейку ID пустой для новых материалов

    // Создаем поле ввода для нового типа материала
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = `new_material_${newId}`; // Уникальное имя для поля
    newInput.id = `new_material_${newId}`; // Уникальный ID для поля
    materialCell.appendChild(newInput);

    // Добавляем ячейки в новую строку
    newRow.appendChild(idCell);
    newRow.appendChild(materialCell);

    // Добавляем новую строку в тело таблицы
    tableBody.appendChild(newRow);
});






// 1 модальное окно
document.getElementById('saveMaterialChanges').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById('typeMaterialForm'));

    fetch('/add_type_material/', {
        method: 'POST',
        body: formData
    })
    // .then(response => {
    //     if (response.ok) {
    //         return response.json(); // Assuming the server returns JSON
    //     }
    //     throw new Error('Network response was not ok.');
    // })
    .then(data => {
        alert("Сохранено успешно"); // Show success message
        location.reload(); // Reload the page to update the displayed materials
    })
    
});


// 2 модальное окно
document.getElementById('saveMethodApplicationChanges').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById('typeMethodApplicationForm'));

    fetch('/add_type_method_application/', {
        method: 'POST',
        body: formData
    })
    .then(data => {
        alert("Сохранено успешно");
        location.reload(); // Reload the page to update the displayed materials
    })    
    
});


// 3 модальное окно
document.getElementById('saveColoringAgentChanges').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById('typeColoringAgentForm'));

    fetch('/add_type_coloring_agent/', {
        method: 'POST',
        body: formData
    })
    .then(data => {
        alert("Сохранено успешно");
        location.reload(); // Reload the page to update the displayed materials
    })    
    
});


// 4 модальное окно
document.getElementById('saveColorChanges').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById('typeColorForm'));

    fetch('/add_type_color/', {
        method: 'POST',
        body: formData
    })
    .then(data => {
        alert("Сохранено успешно");
        location.reload(); // Reload the page to update the displayed materials
    })    
    
});


// 5 модальное окно
document.getElementById('saveGlossChanges').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(document.getElementById('typeGlossForm'));

    fetch('/add_type_gloss/', {
        method: 'POST',
        body: formData
    })
    .then(data => {
        alert("Сохранено успешно");
        location.reload(); // Reload the page to update the displayed materials
    })    
    
});






// 1 модальное окно
document.getElementById('closeModal1').addEventListener('click', function() {
    const modal1 = document.getElementById('modal1');
    modal1.style.display = 'none'; // Закрываем модальное окно
});


// 2 модальное окно
document.getElementById('closeModal2').addEventListener('click', function() {
    const modal2 = document.getElementById('modal2');
    modal2.style.display = 'none'; // Закрываем модальное окно
});


// 3 модальное окно
document.getElementById('closeModal3').addEventListener('click', function() {
    const modal3 = document.getElementById('modal3');
    modal3.style.display = 'none'; // Закрываем модальное окно
});


// 4 модальное окно
document.getElementById('closeModal4').addEventListener('click', function() {
    const modal4 = document.getElementById('modal4');
    modal4.style.display = 'none'; // Закрываем модальное окно
});


// 5 модальное окно
document.getElementById('closeModal5').addEventListener('click', function() {
    const modal5 = document.getElementById('modal5');
    modal5.style.display = 'none'; // Закрываем модальное окно
});




});




function confirmDelete(url) {
    if (confirm("Вы уверены, что хотите удалить этот объект?")) {
        // alert("Удалено успешно");
        window.location.href = url; // Если пользователь подтвердил, перенаправляем его на URL удаления
    }
}




