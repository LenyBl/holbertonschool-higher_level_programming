-- Create a new user named user_0d_2 with the password user_0d_2_pwd and give this user only SELECT privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';