SELECT * 
FROM users
JOIN favorites ON users.id = favorites.user_id
JOIN  books ON books.id = favorites.book_id;
