let initialPrice = 0; // Переменная для хранения начальной цены

    document.addEventListener('DOMContentLoaded', function() {
        const priceElement = document.getElementById('product-price');
        initialPrice = parseFloat(priceElement.innerText.replace(' рублей', '')); // Получаем начальную цену

        document.getElementById('add-button').addEventListener('click', function() {
            const volumeInput = document.getElementById('numeric');
            let volume = parseInt(volumeInput.value);
            
            // Рассчитываем новую цену, добавляя начальную цену за каждый литр
            const newPrice = initialPrice * volume;

            // Обновляем отображаемую цену
            priceElement.innerText = newPrice + ' рублей';
        });
    });