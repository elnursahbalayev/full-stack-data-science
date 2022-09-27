select *
from sql_store.customers
having points > 1000;

select first_name, length(first_name) as length_of_name
from sql_hr.employees;

select first_name, char_length(first_name) as length_of_name
from sql_hr.employees;

select first_name, character_length(first_name) as length_of_name
from sql_hr.employees;

select concat(first_name,' ', last_name)
from sql_hr.employees;

select format(salary,1)
from sql_hr.employees;