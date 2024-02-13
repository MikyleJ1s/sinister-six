create database employeedatabase;
use employeedatabase;

create table employees(
employeeNumber int primary key,
firstname varchar(20),
lastname varchar(20),
extension int,
email varchar(50),
officeCode int,
reportsTo varchar(20),
jobTitle varchar(20));

create table employees_audit(
id INT AUTO_INCREMENT PRIMARY KEY,
employeeNumber INT NOT NULL,
lastname VARCHAR(50) NOT NULL,
changedat DATETIME DEFAULT NULL,
action VARCHAR(50) DEFAULT NULL);

INSERT INTO employees VALUES 
(1,'Steffan','S', 82000, 'Steffan@gmail.com', 3, 'Bob', 'Intern'),
(2,'Amelie', 'A', 52000, 'amelie@gmail.com', 2, 'Bob', 'Intern'),
(3,'Antonio', 'A', 25000, 'antonio@gmail.com', 1, 'Bob', 'Intern'),
(4,'Marco', 'M', 47000, 'Marco@gmail.com', 2, 'Bob', 'Intern'),
(5,'Eliana', 'E', 46000, 'emilie@gmail.com', 3, 'Bob', 'Intern');

SELECT * FROM employees;

CREATE TRIGGER before_employee_update 
BEFORE UPDATE ON employees
FOR EACH ROW
INSERT INTO employees_audit
SET action = 'update',
employeeNumber = OLD.employeeNumber,
lastname = OLD.lastname,
changedat = NOW();

UPDATE employees
SET lastName='Phan' WHERE employeeNumber = 1;
SELECT * FROM employees_audit;

DELIMITER //

CREATE PROCEDURE get_stuff()
BEGIN
	select name FROM employees;
    select * from employees where extension > 50000 and firstname like 'A%';
END //

DELIMITER ;


DELIMITER //

create function get_designation_name(input_id int) 
returns varchar(20) reads sql data deterministic

BEGIN
declare e_name varchar(20) default '';
select firstname into e_name FROM employees where employeeNumber = input_id;
return e_name;
END //


DELIMITER ;

select get_designation_name(2);






