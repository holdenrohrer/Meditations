drop database if exists hello;
create database if not exists hello;
use hello;

create table testyBoy (
    number varchar(100) not null,
    primary key (number)
);