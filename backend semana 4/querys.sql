-- Obtenga todos los libros y sus autores
SELECT Books.name, Authors.name
FROM Books
LEFT JOIN Authors ON Books.AuthorID = Authors.id;

-- Obtenga todos los libros que no tienen autor
SELECT Books.name, Authors.name
FROM Books
LEFT JOIN Authors
ON Books.AuthorID = Authors.id
WHERE Books.AuthorID IS NULL;

-- Obtenga todos los autores que no tienen libros
SELECT Authors.name, Books.name
FROM Authors
LEFT JOIN Books
ON Authors.id = Books.AuthorID
WHERE Books.AuthorID IS NULL;

-- Obtenga todos los libros que han sido rentados en algún momento
SELECT Books.name, Rents.State
FROM Books
INNER JOIN Rents
ON Books.AuthorID = Rents.BookID;

-- Obtenga todos los libros que nunca han sido rentados
SELECT Books.name, Rents.State
FROM Books
LEFT JOIN Rents
ON Books.AuthorID = Rents.BookID
WHERE Rents.State IS NULL;

-- Obtenga todos los clientes que nunca han rentado un libro
SELECT Customers.Name, Rents.CustomerID
FROM Customers
LEFT JOIN Rents
ON Customers.id = Rents.CustomerID
WHERE CustomerID IS NULL;

-- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT Books.Name, Rents.State
FROM Books
INNER JOIN Rents
ON Books.id = Rents.BookID
WHERE State = 'Overdue';