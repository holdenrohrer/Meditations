drop database if exists meditations;
create database if not exists meditations;
use meditations;

create table user (
    user_id varchar(100) not null,
    user_name varchar(100) not null,
    section_id varchar(100) not null,
    last_day varchar(100) not null,
    primary key (user_id)
);

create table section (
    section_id INT not null,
    book_name varchar(100) not null,
    author varchar(100) not null,
    section_name varchar(100) not null,
    texts text(100) not null,
    next_section varchar(100) not null,
    is_last boolean not null,
    last_date varchar(100) not null,
    primary key (section_id)
);

create table annotations (
    token varchar(100) not null,
    book_id varchar(100) not null,
    section_id varchar(100) not null,
    texts varchar(100) not null,
    annotation_id varchar(100) not null,
    primary key (annotation_id)
);

create table reflections (
    user_id varchar(100) not null,
    section_id varchar(100) not null,
    texts varchar(100) not null,
    reflections_id varchar(100) not null,
    primary key (reflections_id)
);

create table books(
    book_id varchar(100) not null,
    book_name varchar(100) not null,
    first_section varchar(100) not null,
    primary key (book_id)
);


INSERT INTO books (book_id, book_name, first_section)
VALUES (1, 'Meditations', 1);
