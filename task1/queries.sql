-- SQL-запити до бази даних системи управління завданнями

-- 1. Отримати всі завдання певного користувача (user_id = 1)
SELECT * FROM tasks
WHERE user_id = 1;

-- 2. Вибрати завдання за певним статусом (через підзапит), наприклад 'new'
SELECT * FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновити статус конкретного завдання (id = 1) на 'in progress'
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;

-- 4. Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- 5. Додати нове завдання для конкретного користувача (user_id = 1)
INSERT INTO tasks (title, description, status_id, user_id)
VALUES (
    'Prepare weekly report',
    'Collect metrics and prepare the weekly report',
    (SELECT id FROM status WHERE name = 'new'),
    1
);

-- 6. Отримати всі завдання, які ще не завершено
SELECT * FROM tasks
WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалити конкретне завдання (id = 2)
DELETE FROM tasks
WHERE id = 2;

-- 8. Знайти користувачів з певною електронною поштою
SELECT * FROM users
WHERE email LIKE '%@example.com';

-- 9. Оновити ім'я користувача (id = 1)
UPDATE users
SET fullname = 'John Doe'
WHERE id = 1;

-- 10. Отримати кількість завдань для кожного статусу
SELECT s.name AS status, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON t.status_id = s.id
GROUP BY s.name
ORDER BY s.name;

-- 11. Отримати завдання користувачів з певною доменною частиною електронної пошти
SELECT t.*, u.email
FROM tasks t
JOIN users u ON u.id = t.user_id
WHERE u.email LIKE '%@example.com';

-- 12. Отримати список завдань, що не мають опису
SELECT * FROM tasks
WHERE description IS NULL OR description = '';

-- 13. Вибрати користувачів та їхні завдання у статусі 'in progress'
SELECT u.id AS user_id, u.fullname, t.id AS task_id, t.title
FROM users u
INNER JOIN tasks t ON t.user_id = u.id
INNER JOIN status s ON s.id = t.status_id
WHERE s.name = 'in progress';

-- 14. Отримати користувачів та кількість їхніх завдань
SELECT u.id, u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON t.user_id = u.id
GROUP BY u.id, u.fullname
ORDER BY u.id;
