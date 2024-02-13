create database joins_demo;
use joins_demo;
CREATE TABLE Student (
id int PRIMARY KEY,
admission_no varchar(45) NOT NULL,
first_name varchar(45) NOT NULL,
last_name varchar(45) NOT NULL,
age int,
city varchar(25) NOT NULL
);
CREATE TABLE Fee (
admission_no varchar(45) NOT NULL,
course varchar(45) NOT NULL,

amount_paid int
);

INSERT INTO Student (id,admission_no, first_name, last_name, age, city)
VALUES (1,3354,"Luisa", "Evans", 13, "Texas"),
(2,2135, "Paul", "Ward", 15, "Alaska"),
(3,4321, "Peter", "Bennett", 14, "California"),
(4,4213,"Carlos", "Patterson", 17, "New York"),
(5,5112, "Rose", "Huges", 16, "Florida"),
(6,6113, "Marielia", "Simmons", 15, "Arizona"),
(8,7555,"Antonio", "Butler", 14, "New York"),
(9,8345, "Diego", "Cox", 13, "California");

INSERT INTO Fee (admission_no, course, amount_paid)
VALUES (3354,"Java", 20000),
(7555, "Android", 22000),
(4321, "Python", 18000),
(8345,"SQL", 15000),
(5112, "Machine Learning", 30000);

select * from fee;
select * from student;

############inner join#################
SELECT Student.admission_no, Student.first_name, Student.last_name, Fee.course, Fee.amount_paid

FROM Student
INNER JOIN Fee
ON Student.admission_no = Fee.admission_no;

##############self join##################

SELECT S1.first_name, S2.last_name, S2.city
FROM Student S1, Student S2
WHERE S1.id <> S2.iD AND S1.city = S2.city
ORDER BY S2.city;

###############cross join###################
SELECT Student.admission_no, Student.first_name, Student.last_name, Fee.course, Fee.amount_paid
FROM Student
CROSS JOIN Fee
WHERE Student.admission_no = Fee.admission_no;

##################LEFT OUTER JOIN

#############right outer join
SELECT Student.admission_no, Student.first_name, Student.last_name, Fee.course, Fee.amount_paid
FROM Student

RIGHT OUTER JOIN Fee
ON Student.admission_no = Fee.admission_no;

##########full outer join
SELECT Student.admission_no, Student.first_name, Student.last_name, Fee.course, Fee.amount_paid
FROM Student 

FULL OUTER JOIN Fee
ON Student.admission_no = Fee.admission_no;

SELECT * FROM student
left outer join fee on student.admission_no = fee.admission_no
union
select * from student
right outer join fee on student.admission_no = fee.admission_no