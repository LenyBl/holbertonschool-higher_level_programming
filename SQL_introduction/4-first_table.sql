-- Create a table named `first_table` with an auto-incrementing primary key `id` and a `name` column
CREATE TABLE IF NOT EXISTS `first_table` (
  'id' int(11) NOT NULL AUTO_INCREMENT,
  'name' varchar(255) NOT NULL,
  PRIMARY KEY ('id')
);