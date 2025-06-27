const menuTab = document.querySelector('.menu-tab');
        const tabHandle = document.querySelector('.tab-handle');

        // Открытие/закрытие по клику
        tabHandle.addEventListener('click', (e) => {
            e.stopPropagation();
            menuTab.classList.toggle('active');
        });

        // Закрытие при клике в любом месте страницы
        document.addEventListener('click', () => {
            menuTab.classList.remove('active');
        });

        // Предотвращаем закрытие при клике внутри меню
        document.querySelector('.tab-menu').addEventListener('click', (e) => {
            e.stopPropagation();
        });

