-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS your_db_name;
CREATE USER IF NOT EXISTS 'your_user'@'your_host' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON `your_db_name`.* TO 'your_user'@'your_host';
GRANT SELECT ON `performance_schema`.* TO 'your_user'@'your_host';
FLUSH PRIVILEGES;
