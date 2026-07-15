SELECT
    title,
    length,
    IF(length >= 120, '장편', '일반') AS movie_type -- 계산된 조회
FROM film
order by movie_type asc, length asc;

SELECT
    title,
    rental_duration,
    IF(rental_duration >= 5, '길다', '짧다') AS duration_type
FROM film
order by rental_duration asc;

SELECT
    title,
    original_language_id,
    IFNULL(original_language_id, 0) AS language_id
FROM film;

SELECT
    title,
    rental_rate,
    NULLIF(rental_rate, 4.99) AS result
FROM film;

-- 실습

use test;

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    price INT,
    discount INT
);

INSERT INTO product(name, price, discount)
VALUES
('노트북', 1500000, 10),
('마우스', 30000, NULL),
('키보드', NULL, 15),
('모니터', 250000, NULL),
('스피커', NULL, NULL);

select*from product;

SELECT
	id,
    name,
    IFNULL(price, 0) AS price,
    NULLIF(discount,15) AS discount
FROM product;

SELECT
    name,
    COALESCE(price, discount, 0) AS value
FROM product;

SELECT *
FROM product
WHERE price IS NOT NULL;

-- 노트북1, 마우스2, 나머지3

select
	if(name= '노트북', 1 , if(name='마우스',2,3))
from product;

-- if()함수 == CASE표현식 근데, 조건의 경우가 많아지면 CASE

SELECT
    title,length,
    CASE
        WHEN length >= 150 THEN '매우 김'
        WHEN length >= 120 THEN '장편'
        WHEN length >= 90 THEN '보통'
        ELSE '단편'
    END AS length_type
FROM film
order by length asc;

SELECT
    title,
    rental_rate,
    CASE
        WHEN rental_rate = 0.99 THEN '저가'
        WHEN rental_rate = 2.99 THEN '중가'
        WHEN rental_rate = 4.99 THEN '고가'
        ELSE '기타'
    END AS price_type
FROM film;

SELECT
    title,
    rating,
    CASE rating
        WHEN 'G' THEN '전체관람가'
        WHEN 'PG' THEN '부모지도'
        WHEN 'PG-13' THEN '13세 이상'
        WHEN 'R' THEN '청소년 제한'
        WHEN 'NC-17' THEN '17세 이상'
        ELSE '기타'
    END AS rating_name
FROM film;

SELECT
    title,
    length,
    rental_rate
FROM film
WHERE IF(length >= 120,
         rental_rate >= 2.99,
         rental_rate >= 0.99);
         
SELECT
    title,
    rating,
    length
FROM film
WHERE IF(rating = 'G',
         length >= 90,
         length >= 120);
         
SELECT
    title,
    original_language_id
FROM film
WHERE IFNULL(original_language_id, 0) >= 10;
-- WHERE original_language_id is NULL or original_language_id = 0 -- NULL은 in 불가능

SELECT
    title,
    rental_rate
FROM film
WHERE NULLIF(rental_rate, 4.99) IS NULL;

-- G 등급은 90분 이상, 그 외는 120분 이상 조회
SELECT
    title,
    rating,
    length
FROM film
WHERE
CASE
    WHEN rating = 'G'
        THEN length >= 90
    ELSE
        length >= 120
END;

SELECT
    title,
    length
FROM film
ORDER BY length ASC;

SELECT
    title,
    length
FROM film
ORDER BY IF(length < 120, 0, 1) ASC, title ASC;


select* from product
order by IFNULL(discount,100) asc;

SELECT
    title,
    rating
FROM film
ORDER BY
CASE
    WHEN rating = 'PG-13' THEN 1
    WHEN rating = 'NC-17' THEN 2
    ELSE 3
END ASC, title ASC;

SELECT
    title,
    length
FROM film
ORDER BY
CASE
    WHEN length >= 120 THEN 1
    ELSE 2
END,
title;

with f2 as (
	select title 제목, length 시간
	from film
	limit 10
    )
    
select f2.제목,f2.시간
from f2
where f2.시간 between 50 and 100;

WITH expensive_movie AS (
    SELECT title, rental_rate
    FROM film
    WHERE rental_rate >= 4
)
SELECT *
FROM expensive_movie;

select*
from actor
where UPPER(first_name) like '%E%'
or UPPER(last_name) like '%O%';

with a_n as (
	SELECT UPPER(CONCAT(first_name,last_name)) fullname 
	from actor
)
select fullname from a_n
where fullname like'%Z%';

-- 1.영화제목이 'A'로 시작하는 영화(상영시간이 긴 순으로 정렬, 상위 10개만)
select title, length
from film
where title like 'A%'
order by length desc
limit 10;

-- film 테이블 - 영화 러닝타임(숫자함수)
-- 2.상영시간을 시간 단위로 반올림하여 함께 출력
select title, 
	length,
    (ROUND(length/60,1)) as running_hour
from film
where length 
limit 10;

-- actor 테이블 -문자열 함수
-- 3.배우의 이름과 성을 하나의 문자열로 합쳐(CONCAT) 배우 이름(full_name)으로 출력
select (CONCAT(first_name,last_name)) as full_name
from actor;

-- 4.이름이 'A'로 시작하는 배우 조회
-- 이름과 성을 출력하고 성 오름차순으로 정렬

select first_name,last_name
from actor
order by last_name asc
limit 10;

-- country 테이블 -WHERE + LIKE + ORDER BY
-- 5.국가명에 'an'이 포함된 국가를 조회하시오.
-- 국가명을 출력하고 국가명 오름차순으로 정렬하시오.
select country 
from country
where country like '%an%'
order by country asc
limit 10;

-- country 테이블-단일행 함수
-- 6.국가명과 국가명의 글자 수를 함께 출력하시오
select country,
	length(country) AS length
from country
limit 10;

-- 7.이름이 'M'으로 시작하는 고객 조회
-- 이름,성,이메일을 출력하고 이름 오름차순으로 정렬

select first_name, last_name,email
from customer
order by first_name asc
limit 10;

-- customer 테이블-단일행 함수
-- 8.고객의 이름과 성을 연결하여 전체 이름을 출력하고 가입일은 YYYY-MM-DD형식을 출력
select (CONCAT(first_name,last_name)) as full_name,
	(DATE_FORMAT(create_date,'%Y-%m-%d')) as date
from customer
limit 10;

-- category 테이블 - WHERE + LIKE + ORDER BY
-- 9. 카테고리명이 'C'로 시작하는 카테고리 조회/ 오름차순으로 정렬
SELECT	name
FROM category
WHERE name like 'C%'
ORDER BY name desc;

-- city 테이블 - 단일행 함수
-- 10. 도시명과 도시명의 글자 수 함께 출력

select city,
	(length(city)) as length
from city
limit 10;

-- 11. 영화 제목과 상영시간을 조회하고 상영시간이 120분 이상이면 "장편" 아니면 "일반" 출력
select title,
	length,
    if(length >=120 ,'장편','일반') type
from film
limit 10;

-- 12. 영화제목과 대여요금을 조회하고, 0.99면 저가,2.99면 중가,4.99면 고가로 출력
select title, 
	rental_rate,
case
	when rental_rate = 0.99 then'저가' 	-- case - when~then - end
	when rental_rate = 2.99 then'중가'
    else '고가'
end as price_type
from film
limit 10;

-- 13. 영화 제목과 등급을 조회하고 다음과 같이 출력
-- G → "전체관람가",PG → "부모지도",PG-13 → "13세 이상",R → "청소년 제한",NC-17 → "17세 이상"
select title,
	rating,
case
	when rating = 'G' then '전체관람가'
    when rating = 'PG' then '부모지도'
    when rating = 'PG-13' then '13세 이상'
    when rating = 'R' then '청소년 제한'
    when rating = 'NC-17' then '17세 이상'
end as 등급
from film
limit 10;

-- 14.original_language_id가 NULL이면 0으로 출력하고, NULL이 아니면 원래 값을 출력

select title, ifnull(original_language_id , 0)
from film
limit 10;

-- 15.영화 제목과 대여기간을 조회하고 7일이상 → "매우 김"/5~6일 → "보통"/4일 이하 → "짧음"으로 출력

select title,rental_duration,
case
	when rental_duration >= '7' then '매우 김'
    when rental_duration >= '5' then '보통'
    when rental_duration <= '4' then '짧음'
from film
limit 10;