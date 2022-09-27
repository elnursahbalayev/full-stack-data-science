

-- CONSTRAINTS

-- not null constraints

use testdb;
create table persons (
					ID int not null,
                    First_name varchar(10) not null,
                    Last_name varchar(10) null,
                    Age int null);
                    
select * from persons;


-- unique constraints
DROP TABLE persons;

CREATE TABLE persons(
					ID INT NOT NULL,
                    First_name VARCHAR(10),
                    Last_name VARCHAR(10),
                    Age INT,
                    UNIQUE(ID)
                    );
                    
                    
INSERT INTO persons (First_name, Last_name, Age)
VALUES ('Elnur', 'Shahbalayev', 22);

-- DEFAULT CONSTRAINTS

DROP TABLE persons;
CREATE TABLE persons(
					ID INT DEFAULT 100,
                    First_name VARCHAR(19),
                    Last_name VARCHAR(19),
                    Age INT,
                    UNIQUE(ID)
                    );
                    
INSERT INTO persons (First_name, Last_name, Age)
VALUES ('Elnur', 'Shahbalayev', 22);

SELECT * FROM persons;


-- PRIMARY KEY CONSTRAINT

CREATE TABLE Customers(
name varchar(10),
product varchar(15),
product_id int,
primary key(product_id)
);

select * from Customers;


-- altering existing table(adding a constraint later on)

alter table persons
add primary key(ID);


-- droping the constraints from the existing table

create table passengers
(
first_name varchar(15),
last_name varchar(15),
mobile int,
ticket_number varchar(10)
);

select * from passengers;

alter table passengers
add constraint UC_passengers unique(mobile, ticket_number);

alter table passengers
drop index UC_passengers;


-- foreign key constraint

create table customers(
customer_id int not null,
first_name varchar(15),
last_name varchar(20),
age int,
primary key (customer_id)
);

create table orders
(
order_id int not null,
order_number int not null,
customer_id int,
primary key(order_id),
foreign key(customer_id) references customers(customer_id)
);

