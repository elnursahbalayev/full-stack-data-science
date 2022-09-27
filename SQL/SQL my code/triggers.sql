-- triggers are programs that are automatically invoked in response to an event

-- before insert trigger
create trigger new_price

before insert
on products
for each row

set new.unit_price = new.unit_price*.90 