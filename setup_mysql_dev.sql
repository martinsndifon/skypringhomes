-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS sky_dev_db;
CREATE USER IF NOT EXISTS 'sky_dev'@'localhost' IDENTIFIED BY 'sky_dev_pwd';
GRANT ALL PRIVILEGES ON `sky_dev_db`.* TO 'sky_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'sky_dev'@'localhost';
FLUSH PRIVILEGES;
