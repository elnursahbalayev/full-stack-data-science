use sql_store;

select * from customers;

select first_name, last_name, points
from customers
order by points desc;


select first_name, last_name, points
from customers
where birth_date < '1990-01-01'
order by points desc;

use sql_store;
SELECT first_name,
		last_name,
        points,
        points*10-5 AS operations
FROM customers;


SELECT *
FROM orders;

SELECT 
		product_id,
        quantity,
        unit_price,
        quantity*unit_price AS total_price,
		round(quantity*unit_price*.95,2) as discounted_price
FROM order_items;


SELECT * FROM products;

SELECT name,
		unit_price,
        round(unit_price*.95,2) AS discounted_price
FROM products;


SELECT * FROM customers;
        
        
-- DISTINCT keyword to find unique items

SELECT DISTINCT state
FROM customers;

SELECT DISTINCT * 
FROM customers;


-- WHERE clause in details -- 

SELECT * 
FROM customers
where points = 457;

SELECT * 
FROM customers
where state = 'VA';

select * from orders where order_date < '2019-01-01';


--- and, or and not operators

use sql_store;
select *
from customers
where birth_date > '1990-01-01' or city='Chicago' and points > 1000;

select * from order_items;

select
	unit_price,
    quantity*unit_price as total_price
from order_items
where order_id = 6 and quantity*unit_price > 20;


select *
from customers
where points between 1000 and 3000;




-- in operator --
select *
from customers
where state='VA' or state='FL' or state='GA';


select *
from products
where quantity_in_stock in (49, 38, 70);


select *
from customers
where birth_date between '1990-01-01' and '2000-01-01';


-- like --
select *
from customers
where last_name like 'brush%';


select * 
from customers
where last_name like 'b_____';


select *
from customers
where address like '*Trail*' or address like '*Avenue*' and phone like '*4';

use sql_store;

-- regexp
select *
from customers
where last_name regexp '^b';

-- regexp find letter in last name
select *
from customers
where last_name regexp 'd$';


select *
from customers
where last_name regexp 'y|s';


select *
from customers
where last_name regexp '[g,s,l]e';


-- ^ beginning of a string
-- $ end of a string
-- | logical or
-- [a,b,c,d] combination of characters before or after the letter, can give range as well [a-m]


select * 
from customers
where first_name ='Elka' or first_name='Ambur';

select *
from customers
where last_name like '%ey' or last_name like '%on';

select * 
from customers
where last_name regexp '^my|se';

select *
from customers
where last_name regexp 'b[r,u]';


-- is null & is not null operators

select *
from customers
where phone is null;

select * 
from orders;


select *
from orders
where shipped_date is null;


-- order by operator

select *
from customers
order by first_name;

select *
from customers
order by points desc, first_name;

-- limit clause
select *
from customers
limit 5;

select *
from customers
limit 5,3;


-- top 3 loyal customers
select *
from customers
order by points desc
limit 3;