create database store;
use store;
create table products(
product_id int not null unique,
product_name varchar(10) not null, 
product_price double not null,
product_quantity int not null, 
product_owner varchar(15) not null, 
product_expire date
); 

insert into products(
product_id, product_name, product_prince, product_quantity, product_owner, product_expire) values 
(1, "Milk", 10.23, 54, "Milk.Co", '2023-2-17'), 
(2, "Rice", 21.50, 11, "RiceLikeIce", '2023-2-21'), 
(3, "Tea", 5.00, 125, "T", '2023-3-2');

select * from products;

select sum(product_quantity) as q from products;
alter table products rename column product_prince to product_price;
select count(product_name) from products where product_price > 10;
select * from products where product_owner like '%o';
select * from products where product_owner like 'Ri%';
select * from products where product_name like '%i%';
select * from products where product_quantity like '1%';
select * from products where product_quantity between 10 and 100;
select * from products where product_quantity not between 10 and 100;
