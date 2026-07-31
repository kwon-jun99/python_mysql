'''
CREATE TABLE person (
    person_id INT PRIMARY KEY,
    person_name VARCHAR(30),
    hobby VARCHAR(100)
);

INSERT INTO person VALUES
(1001, '홍길동', '야구,농구'),
(1002, '김철수', '독서'),
(1003, '이영희', '영화감상,여행'),
(1004, '박민수', '등산,수영,캠핑'),
(1005, '최지훈', '게임,발야구');

SELECT *
FROM person
WHERE hobby = '야구'; -- 조회결과가 없다

SELECT *
FROM person
WHERE hobby LIKE '%야구%'; -- 발야구도 조회되어 나온다
-- ----------------------------------------------------------------------- --
-- 1정규화 relation 분리

CREATE TABLE person1 (
    person_id INT PRIMARY KEY,
    person_name VARCHAR(30)
);

INSERT INTO person1 VALUES
(1001,'홍길동'),
(1002,'김철수'),
(1003,'이영희'),
(1004,'박민수'),
(1005,'최지훈');

CREATE TABLE person1_hobby (
    person_id INT,
    hobby VARCHAR(30),
    PRIMARY KEY(person_id, hobby),
    FOREIGN KEY(person_id)
        REFERENCES student(person_id)
);

INSERT INTO person1_hobby VALUES
(1001,'야구'),
(1001,'농구'),
(1002,'독서'),
(1003,'영화감상'),
(1003,'여행'),
(1004,'등산'),
(1004,'수영'),
(1004,'캠핑'),
(1005,'게임'),
(1005,'발야구');
-- ----------------------------------------------------------------------- --

select * from person1_hobby ph join person1 p on ph.person_id = p.person_id
where hobby = '야구';
-- ----------------------------------------------------------------------- --

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(30),
    subject1 VARCHAR(30),
    subject2 VARCHAR(30),
    subject3 VARCHAR(30)
);

INSERT INTO student VALUES
(1001,'홍길동','DB','Python','Power BI'),
(1002,'김철수','Java','SQL',NULL),
(1003,'이영희','Python',NULL,NULL);

select * from student;
-- ----------------------------------------------------------------------- --

CREATE TABLE student1 (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(30)
);

INSERT INTO student1 VALUES
(1001,'홍길동'),
(1002,'김철수'),
(1003,'이영희');

CREATE TABLE student1_subject (
    student_id INT,
    subject_name VARCHAR(30),
    PRIMARY KEY(student_id, subject_name),
    FOREIGN KEY(student_id)
        REFERENCES student1(student_id)
);

INSERT INTO student1_subject VALUES
(1001,'DB'),
(1001,'Python'),
(1001,'Power BI'),
(1002,'Java'),
(1002,'SQL'),
(1003,'Python');

select * from student1_subject;

insert into student1_subject
values('1001','Java');
-- 1정규화 전
select * from student1 where student_id ='1001';
-- 1정규화 후(정규화 후 조인 -> 복잡성 증가)
select * 
from student1 s join student1_subject ss 
on s.student_id = ss.student_id
where s.student_id ='1001';

select s.student_id, s.student_name, group_concat(ss.subject_name)
from student1 s join student1_subject ss 
on s.student_id = ss.student_id
where s.student_id ='1001'
group by s.student_id, s.student_name;


-- ----------------------------------------------------------------------- --

CREATE TABLE student_course (
    student_id INT,
    student_name VARCHAR(30),
    subject_id CHAR(3),
    subject_name VARCHAR(30),
    tuition INT,
    discount_rate INT,
    PRIMARY KEY(student_id, subject_id)
);

INSERT INTO student_course
(student_id, student_name, subject_id, subject_name, tuition, discount_rate)
VALUES
(1001, '홍길동', 'S01', 'Python',    300000, 10),
(1001, '홍길동', 'S02', 'SQL',       250000, 20),
(1001, '홍길동', 'S03', 'Power BI',  350000, 15),

(1002, '김철수', 'S01', 'Python',    300000,  5),
(1002, '김철수', 'S02', 'SQL',       250000, 10),
(1002, '김철수', 'S04', 'Java',      280000,  0),

(1003, '이영희', 'S01', 'Python',    300000,  0),
(1003, '이영희', 'S03', 'Power BI',  350000, 20),
(1003, '이영희', 'S04', 'Java',      280000, 10),

(1004, '박민수', 'S02', 'SQL',       250000, 15),
(1004, '박민수', 'S03', 'Power BI',  350000,  5),

(1005, '최유리', 'S01', 'Python',    300000, 20),
(1005, '최유리', 'S04', 'Java',      280000, 10);

select* from student_course;

-- 수강료 확인
SELECT
    subject_id,
    COUNT(DISTINCT tuition) AS tuition_count
FROM student_course
GROUP BY subject_id;

-- 할인률 확인
SELECT
    subject_id,
    COUNT(DISTINCT discount_rate) AS discount_count
FROM student_course
GROUP BY subject_id;
'''