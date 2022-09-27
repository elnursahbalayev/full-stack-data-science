-- inserting into a single row

use sql_store;

select * 
from customers;

insert into customers
values (default, 'Elnur', 'Shahbalayev', '1999-11-14', 0773061366, 'Baku, Hosvan', 'Baku', 'Az', 2000);

-- inserting multiple data into the table

insert into shippers
values
	(default, 'shipper1'),
	(default, 'shipper2'),
    (default, 'shipper3'),
    (default, 'shipper4');
    
select *
from shippers;

-- creating a copy of a table
create table new_orders as 
select * from orders; 

drop table new_orders; 

insert into new_orders
select *
from orders
where order_date < '2019-01-01';

select * 
from new_orders
order by order_date desc;


-- update existing table

use sql_invoicing;

update payments
set date='2022-01-02',
	amount=40.02,
    payment_method=1
where payment_id=2;

select *
from payments;

update invoices
set payment_total=10,
	payment_date = due_date
where invoice_id=5;

-- updating multiple records

update invoices
set payment_total=40
where client_id=5;

update invoices
set payment_total=40
where client_id in (3,5);