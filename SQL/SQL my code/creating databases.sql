-- creating databases

-- create command

CREATE DATABASE testdb;

-- creating tables
USE testdb;
CREATE TABLE students(
					Roll_no INT,
                    Name VARCHAR(10),
                    Age INT,
                    Phone INT);
                    
SELECT * FROM students;


-- Inserting data into table
insert into students 
values (1, 'Elnur', 22, 0136128982),
		(2, 'Bran', 23, 0136124982),
        (3, 'John', 24, 0136122382);

select * from students