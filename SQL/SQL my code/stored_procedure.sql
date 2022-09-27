-- stored procedure
use sql_store;
create procedure test()
select * 
from sql_store.orders
where order_date > '2018-01-01';

call test();

-- stored procedure with single parameter
use sql_hr;

create procedure test1(office_id int)

select
	office_id,
    first_name,
    last_name,
    job_title,
    salary
from employees;

call test1(10);

-- stored procedure with multiple parameters
create procedure test2(id int, sal decimal)

select
	office_id,
    first_name,
    last_name,
    job_title,
    salary
from employees
where office_id = id and salary > sal;

call test2(1, 500);

-- drop stored procedure 

drop procedure test1;
drop procedure test2;
use sql_store;
drop procedure test;