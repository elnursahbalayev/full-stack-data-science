use sql_hr;

alter view  new_employee as
select * from employees
where job_title not like '%VP%';

-- drop the view
use sql_hr;
drop view new_employee;