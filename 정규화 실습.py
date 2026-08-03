'''
CREATE TABLE student_course_score (
    student_id INT,
    course_id INT,
    student_name VARCHAR(30),
    course_name VARCHAR(50),
    score INT,
    PRIMARY KEY (student_id, course_id)
);

INSERT INTO student_course_score
VALUES
(1001, 101, '홍길동', '데이터베이스', 95),
(1001, 102, '홍길동', 'Python', 88),
(1002, 101, '김철수', '데이터베이스', 91),
(1002, 103, '김철수', 'Power BI', 85),
(1003, 102, '이영희', 'Python', 93);

select* from student_course_score;

CREATE TABLE student_master (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(30)
);
INSERT INTO student_master
VALUES
(1001,'홍길동'),
(1002,'김철수'),
(1003,'이영희');

CREATE TABLE course_master (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

INSERT INTO course_master
VALUES
(101,'데이터베이스'),
(102,'Python'),
(103,'Power BI');

CREATE TABLE enrollment_score (
    student_id INT,
    course_id INT,
    score INT,
    PRIMARY KEY(student_id, course_id),
    FOREIGN KEY(student_id)
        REFERENCES student_master(student_id),
    FOREIGN KEY(course_id)
        REFERENCES course_master(course_id)
);

INSERT INTO enrollment_score
VALUES
(1001,101,95),
(1001,102,88),
(1002,101,91),
(1002,103,85),
(1003,102,93);

select* from enrollment_score;

-- 3정규형(함수 종속성이 기본키가 아닌 다른 키에 종속되면 분리하는 것)

CREATE TABLE employee_info (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(30),
    dept_code CHAR(2),
    dept_name VARCHAR(30)
);

INSERT INTO employee_info
VALUES
(1001, '홍길동', 'D1', '영업부'),
(1002, '김철수', 'D2', '개발부'),
(1003, '이영희', 'D2', '개발부'),
(1004, '박민수', 'D3', '인사부');

select* from employee_info;

CREATE TABLE department_master (
    dept_code CHAR(2) PRIMARY KEY,
    dept_name VARCHAR(30)
);

INSERT INTO department_master
VALUES
('D1','영업부'),
('D2','개발부'),
('D3','인사부');

CREATE TABLE employee_master (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(30),
    dept_code CHAR(2),
    FOREIGN KEY (dept_code)
        REFERENCES department_master(dept_code)
);

INSERT INTO employee_master
VALUES
(1001,'홍길동','D1'),
(1002,'김철수','D2'),
(1003,'이영희','D2'),
(1004,'박민수','D3');

select* from employee_master;

SELECT
    e.emp_id,
    e.emp_name,
    d.dept_name
FROM employee_master e
JOIN department_master d
    ON e.dept_code = d.dept_code
ORDER BY e.emp_id;

-- --------------------------------------------------------------------------- --
-- 정규형 실습
CREATE TABLE employee_project (
    emp_id INT,
    emp_name VARCHAR(30),
    phone_numbers VARCHAR(100),
    project_id INT,
    project_name VARCHAR(50),
    dept_code CHAR(2),
    dept_name VARCHAR(30),
    PRIMARY KEY(emp_id, project_id)
);

INSERT INTO employee_project
VALUES
(1001,'홍길동','010-1111-1111,010-9999-9999',101,'쇼핑몰 구축','D1','개발부'),
(1001,'홍길동','010-1111-1111,010-9999-9999',102,'ERP 구축','D1','개발부'),
(1001,'홍길동','010-1111-1111,010-9999-9999',103,'모바일 앱','D1','개발부'),
(1002,'김철수','010-2222-2222',101,'쇼핑몰 구축','D2','영업부'),
(1002,'김철수','010-2222-2222',104,'CRM 구축','D2','영업부'),
(1003,'이영희','010-3333-3333',103,'모바일 앱','D1','개발부'),
(1003,'이영희','010-3333-3333',105,'AI 챗봇','D1','개발부'),
(1004,'박민수','010-4444-4444',102,'ERP 구축','D3','인사부'),
(1004,'박민수','010-4444-4444',106,'전자결재','D3','인사부'),
(1005,'최지훈','010-5555-5555,010-8888-8888',101,'쇼핑몰 구축','D2','영업부'),
(1005,'최지훈','010-5555-5555,010-8888-8888',107,'데이터웨어하우스','D2','영업부'),
(1006,'한소영','010-6666-6666',105,'AI 챗봇','D1','개발부'),
(1006,'한소영','010-6666-6666',108,'클라우드 전환','D1','개발부'),
(1007,'정우성','010-7777-7777',104,'CRM 구축','D4','마케팅부'),
(1007,'정우성','010-7777-7777',109,'홈페이지 리뉴얼','D4','마케팅부'),
(1008,'오세훈','010-8888-1111',106,'전자결재','D3','인사부'),
(1008,'오세훈','010-8888-1111',108,'클라우드 전환','D3','인사부'),
(1009,'강민지','010-9999-2222',107,'데이터웨어하우스','D5','전략기획부'),
(1010,'윤성호','010-1234-5678',109,'홈페이지 리뉴얼','D4','마케팅부'),
(1010,'윤성호','010-1234-5678',105,'AI 챗봇','D4','마케팅부');

select* from employee_project
order by project_id;

-- --------------------------------------------------------------------------- --
-- 1정규형 
CREATE TABLE employee_subject (
	emp_id INT,
    emp_name VARCHAR(30),
    phone_numbers VARCHAR(100),
    dept_code CHAR(2),
    dept_name VARCHAR(30),
    PRIMARY KEY(emp_id)
    );
    
INSERT INTO employee_subject
VALUES
(1001,'홍길동','010-1111-1111,010-9999-9999','D1','개발부'),
(1002,'김철수','010-2222-2222','D2','영업부'),
(1003,'이영희','010-3333-3333','D1','개발부'),
(1004,'박민수','010-4444-4444','D3','인사부'),
(1005,'최지훈','010-5555-5555,010-8888-8888','D2','영업부'),
(1006,'한소영','010-6666-6666','D1','개발부'),
(1007,'정우성','010-7777-7777','D4','마케팅부'),
(1008,'오세훈','010-8888-1111','D3','인사부'),
(1009,'강민지','010-9999-2222','D5','전략기획부'),
(1010,'윤성호','010-1234-5678','D4','마케팅부');

select* from employee_subject;

CREATE TABLE information_subject (
    project_id INT,
    project_name VARCHAR(50),
    PRIMARY KEY(project_id)
    );
    
select* from information_subject;

INSERT INTO information_subject
VALUES
(101,'쇼핑몰 구축'),
(102,'ERP 구축'),
(103,'모바일 앱'),
(104,'CRM 구축'),
(105,'AI 챗봇'),
(106,'전자결재'),
(107,'데이터웨어하우스'),
(108,'클라우드 전환'),
(109,'홈페이지 리뉴얼');

select* from employee_subject;
select* from information_subject;

-- --------------------------------------------------------------------------- --
-- 2정규형

CREATE TABLE employee_phone_number_subject (
    emp_id INT,
    phone_numbers VARCHAR(100)
    );
    
select* from employee_phone_number_subject;

INSERT INTO employee_phone_number_subject
VALUES
(1001, '010-1111-1111'),
(1001, '010-9999-9999'),
(1002, '010-2222-2222'),
(1003, '010-3333-3333'),
(1004, '010-4444-4444'),
(1005, '010-5555-5555'),
(1005, '010-8888-8888'),
(1006, '010-6666-6666'),
(1007, '010-7777-7777'),
(1008, '010-8888-1111'),
(1009, '010-9999-2222'),
(1010, '010-1234-5678');
'''