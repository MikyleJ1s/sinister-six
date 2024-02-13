create database policy_management_system;
use policy_management_system;

create table user_table (
	user_identifier int not null auto_increment,
	user_name varchar(50) not null, 
	user_email varchar(100) not null unique,
	user_surname varchar(50) not null, 
	user_age date not null,
	user_password varchar(50) not null,
	primary key (`user_identifier`)
);

create table policy_table(
	policy_name varchar(100) not null, 
	amount_paid float,
	policy_decription varchar(100) not null, 
	date_acquired date not null,
	user_identifier int,
	policy_identifier int not null auto_increment, 
	primary key (`policy_identifier`),
	foreign key (user_identifier) references user_table(user_identifier)
);

insert into user_table(user_name, user_email, user_surname, user_age, user_password) values
	('A', 'a@gmail.com', 'a', '1999-12-03', 'A'), 
	('B', 'b@gmail.com', 'b', '2000-03-23', 'B'),
	('C', 'c@gmail.com', 'c', '1985-09-26', 'C'),
	('D', 'd@gmail.com', 'd', '1956-06-02', 'D'), 
	('E', 'e@gmail.com', 'e', '1951-07-07', 'E');

insert into policy_table(policy_name, amount_paid, policy_decription, date_acquired, user_identifier) values
	('Car Insurance', 5631.99, 'Car Insurance', '2018-02-13', 1), 
	('Car Insurance', 4563.33, 'Car Insurance', '2017-02-21', 2), 
	('Car Insurance', 65423.54, 'Car Insurance', '2020-03-23', 3), 
	('Home Insurance', 123.54, 'Home Insurance', '2018-12-10', 1), 
	('Home Insurance', 51.99, 'Home Insurance', '2018-01-01', 5), 
	('Life Insurance', 465.95, 'Life Insurance', '2022-11-06', 4), 
	('Car Insurance', 3.00, 'Car Insurance', '2022-12-03', 4), 
	('Life Insurance', 56321.56, 'Life Insurance', '2017-05-18', 1), 
	('Home Insurance', 1.99, 'Home Insurance', '2000-02-16', 4),
	('Pet Insurance', 4563.33, 'Pet Insurance', '2017-02-21', 1), 
	('Travel Insurance', 65423.54, 'Travel Insurance', '2020-03-23', 1),  
	('Funeral Insurance', 51.99, 'Funeral Insurance', '2018-01-01', 1),
	('Disability Insurance', 51.99, 'Disability Insurance', '2018-01-01', 1),
	('Unemployment Insurance', 564.10, 'Unemployment Insurance', '2017-02-21', 1), 
	('Accident and Health Insurance', 65423.50, 'Accident and Health Insurance', '2020-03-23', 1);

create table payment_table(
	payment_identifier int not null auto_increment, 
	amount_paid float,
	payment_date date not null,
	policy_identifier int, 
	user_identifier int, 
    payment_description varchar(100) not null,
	primary key (`payment_identifier`),
	foreign key (policy_identifier) references policy_table(policy_identifier), 
	foreign key (user_identifier) references user_table(user_identifier)
);

insert into payment_table(payment_description, amount_paid, payment_date, policy_identifier, user_identifier) values
	('Car Insurance', 5631.99, '2018-02-13', 1, 1), 
	('Car Insurance', 4563.33, '2017-02-21', 2, 2), 
	('Car Insurance', 65423.54, '2020-03-23', 3, 3), 
	('Home Insurance', 123.54, '2018-12-10', 4, 1), 
	('Home Insurance', 51.99, '2018-01-01', 5, 5), 
	('Life Insurance', 465.95, '2022-11-06', 6, 4), 
	('Car Insurance', 3.00, '2022-12-03', 7, 4), 
	('Life Insurance', 56321.56, '2017-05-18', 8, 1), 
	('Home Insurance', 1.99, '2000-02-16', 9, 4),
	('Pet Insurance', 4563.33, '2017-02-21', 10, 1), 
	('Travel Insurance', 65423.54, '2020-03-23', 11, 1),  
	('Funeral Insurance', 51.99, '2018-01-01', 12, 1),
	('Disability Insurance', 51.99, '2018-01-01', 13, 1),
	('Unemployment Insurance', 564.10, '2017-02-21', 14, 1), 
	('Accident and Health Insurance', 65423.50, '2020-03-23', 15, 1);

select * from user_table;
select * from policy_table;
select * from payment_table;