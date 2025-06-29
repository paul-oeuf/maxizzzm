// Функция для проверки российского IP
async function checkRussianIP() {
  try {
    // Получаем IP-адрес клиента через сторонний сервис
    const ipResponse = await fetch('https://api.ipify.org?format=json');
    const ipData = await ipResponse.json();
    const clientIP = ipData.ip;

    // Проверяем страну IP через free API
    const geoResponse = await fetch(`https://ipapi.co/${clientIP}/country/`);
    const country = await geoResponse.text();

    // Если страна - Россия (RU), перенаправляем
    if (country === 'RU') {
      window.location.href = '/sadrussia';
    }
  } catch (error) {
    console.error('Ошибка проверки IP:', error);
    // В случае ошибки разрешаем доступ
  }
}

// Запускаем проверку при загрузке страницы
document.addEventListener('DOMContentLoaded', checkRussianIP);