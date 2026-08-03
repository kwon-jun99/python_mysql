'''
-- 반정규화

CREATE TABLE member (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(30),
    password VARCHAR(100),
    password_changed_at DATETIME
);

CREATE TABLE password_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    password VARCHAR(100),
    changed_at DATETIME,

    FOREIGN KEY(member_id)
        REFERENCES member(member_id)
);

INSERT INTO member VALUES
(1001,'홍길동','pw1234',NOW()),
(1002,'김철수','abcd1234',NOW());

select* from member;

update member
set password = "0000"
where member_id= 1001;

insert into password_history(member_id,password,changed_at) values(1001, "0000", now());

select* from password_history;
'''