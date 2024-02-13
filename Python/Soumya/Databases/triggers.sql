create database triggerexample;
use triggerexample;
create table student(
student_id int not null unique, 
student_name varchar(20) not null, 
score1 float not null, 
score2 float not null, 
score3 float not null, 
total float not null, 
percentage float not null);

insert into student values(1, "MJ", 30, 50, 20, 0, 0);

create trigger studentmarks before insert on student 
for each row 
set new.total = new.score1+new.score2+new.score3, 
new.percentage = new.total * 60/100;

insert into student(student_id, student_name, score1, score2, score3) values (2, "KJ", 10, 40, 30);
insert into student(student_id, student_name, score1, score2, score3) values (3, "FJ", 30, 10, 40);
select * from student;

create table customers(
id int not null auto_increment, 
name varchar(30) not null, 
age int not null,
address varchar(50),
salary float not null);
