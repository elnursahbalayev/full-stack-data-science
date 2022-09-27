-- sql joins
use sql_store;

select * 
from orders
join customers
	on orders.customer_id = customers.customer_id;
    
select order_id, first_name, last_name
from orders
join customers
		on orders.customer_id = customers.customer_id;


use sql_store;

select order_id, first_name, last_name, orders.customer_id
from orders
join customers
		on orders.customer_id = customers.customer_id;
        
select * from order_items;

select * from products;

select ord.product_id, name, quantity, ord.unit_price
from order_items ord
join products pr
	on ord.product_id = pr.product_id;
    
    
-- joining across databases

select name, io.unit_price,  
from order_items oi
join sql_inventory.products p
	on oi.product_id = p.product_id;

use sql_invoicing;

select *
from payments
join payment_methods
	on payments.payment_id = payment_methods.payment_method_id
join clients
	on payments.client_id = clients.client_id;

select *
from payments p
join payment_methods pm
	on p.payment_id = pm.payment_method_id
join clients c
	on p.client_id = c.client_id;
    
-- joining table within itself

use sql_hr;

select *
from employees e
join employees m
	on e.reports_to = m.employee_id;
    
select
	e.employee_id,
    e.first_name,
    m.first_name as 'Reports to'
from employees e
join employees m
	on e.reports_to = m.employee_id;
    
-- joining across multiple table
use sql_store;

select *
from orders o 
join customers c
	on o.customer_id = c.customer_id
join order_statuses os
	on o.status = os.order_status_id;
    
    
select p.product_id, name, quantity
from products p
left join order_items oi
	on p.product_id = oi.product_id;
    
use sql_invoicing;

select 
	p.date,
    p.amount,
    c.name as 'client',
    pm.name as 'name'
from payments p
join clients c
	on p.client_id = c.client_id
join payment_methods pm
	on p.payment_method = pm.payment_method_id;