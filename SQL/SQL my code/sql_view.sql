-- view in sql

use sql_hr;


-- creating view
create view new_employee as
select *
from employees
where job_title not like '%vp%' and reports_to is not null;


-- using view 
select *
from new_employee;

-- alter sql view

