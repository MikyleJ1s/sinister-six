create database university;
use university;
create table student(
student_id int not null, 
student_name varchar(20) not null, 
student_email varchar(20),
primary key (student_id)
);
create table studentmodule(
module_code int not null, 
student_id int not null, 
module_grade varchar(20) not null,
primary key (module_code),
foreign key (student_id) references student(student_id)
);

create table module(
module_code int not null, 
module_id int not null, 
module_description varchar(20), 
primary key (module_code)
);

alter table module add module_map varchar(10);
alter table module drop module_map;
alter table module rename column module_id to module_index;

drop table model;

create database dummy;
drop database dummy;

insert into module (module_code, module_id, module_description) values (1,101,"the SQL module");
select * from module;
insert into module (module_code, module_id, module_description) values 
(2,202,"the PYTHON module"), 
(3,303,"the JAVA module");

update module set module_description = "the C module", module_id = 505 where module_code = 1;

delete from module where module_code = 3;

select * from module order by module_id;

select min(module_id) as min_module_value from module;


