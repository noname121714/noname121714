<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой Сайт</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Главная</a></li>
                <li><a href="#about">О нас</a></li>
                <li><a href="#contact">Контакты</a></li>
            </ul>
        </nav>
    </header>

    <section id="home">
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Здесь будет интересная информация о нас.</p>
    </section>

    <section id="about">
        <h2>О нас</h2>
        <p>Мы - команда профессионалов, создающих крутые сайты!</p>
    </section>

    <section id="contact">
        <h2>Контакты</h2>
        <form>
            <label for="name">Ваше имя:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Ваш email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Сообщение:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Отправить</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2025 Мой Сайт. Все права защищены.</p>
    </footer>
</body>
</html>