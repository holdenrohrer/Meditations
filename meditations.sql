drop database if exists meditations;
create database if not exists meditations;
use meditations;

create table section (
    book_id varchar(100) not null,
    section_id varchar(100) not null,
    texts varchar(MAX) not null,
    primary key (book_id, section_id)
);

create table annotations (
    token varchar(100) not null,
    book_id varchar(100) not null,
    section_id varchar(MAX) not null,
    texts varchar(MAX) not null,
    primary key (annotation_id)
);

create table reflections (
    token varchar(100) not null,
    book_id varchar(100) not null,
    section_id varchar(100) not null,
    texts varchar(MAX) not null,
    start_id varchar(100) not null,
    end_id varchar(100) not null,
    primary key (reflections_id)
);

insert into section (book_id, section_id, texts)
values ("meditations", 1, "1"),
values ("meditations", 2, "2"),
values ("meditations", 3, "3");

