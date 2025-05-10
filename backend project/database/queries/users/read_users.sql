-- get all users without filters
SELECT id, name, last_name, user_email, password, phone_number, created_date, user_role
FROM pets_eccomerce.users ORDER BY id ASC;

-- get users based on name. Replace :name with user's name
SELECT id, name, last_name, user_email, password, phone_number, created_date, user_role
FROM pets_eccomerce.users  WHERE name = :name
ORDER BY id ASC;

-- get user info based on email. Replace :user_email with user's email
SELECT id, name, last_name, user_email
FROM pets_eccomerce.users  WHERE user_email = :user_email;

-- Get users based on a specific created date. Replace :created_date with a valid date
SELECT id, name, last_name, user_email, password, phone_number, created_date, user_role
FROM pets_eccomerce.users  WHERE created_date = :created_date
ORDER BY id ASC;

-- Get users created in a range of dates
SELECT id, name, last_name, user_email, password, phone_number, created_date, user_role
FROM pets_eccomerce.users  WHERE created_date BETWEEN :created_date AND :created_date
ORDER BY created_date ASC;

-- get users info based on last name
SELECT id, name, last_name, user_email, password, phone_number, created_date, user_role
FROM pets_eccomerce.users  WHERE last_name = :last_name
ORDER BY id ASC;