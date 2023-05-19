CREATE DATABASE mtuci_timetable;

CREATE TABLE timestamps(
    id serial PRIMARY KEY,
    time_start VARCHAR(5) NOT NULL,
    time_end VARCHAR(5) NOT NULL);

CREATE TABLE subject(
    id serial PRIMARY KEY,
    named VARCHAR(25) NOT NULL,
    teacher VARCHAR(25));

DROP TABLE IF EXISTS monday;
CREATE TABLE monday(
    num SERIAL PRIMARY KEY,
    time_start VARCHAR(5),
    time_end VARCHAR(5),
    subject VARCHAR(25),
    teacher VARCHAR(25));

INSERT INTO monday(time_start, time_end, subject) VALUES ('9:30','11:05','Physics');
INSERT INTO monday(time_start, time_end, subject) VALUES ('11:20','12:55','Algebra');
INSERT INTO monday(time_start, time_end, subject) VALUES ('13:10','14:45','');
INSERT INTO monday(time_start, time_end, subject) VALUES ('15:25','17:00','');
INSERT INTO monday(time_start, time_end, subject) VALUES ('17:25','19:00','');

DROP TABLE IF EXISTS tuesday;
CREATE TABLE tuesday(
    num SERIAL PRIMARY KEY,
    time_start VARCHAR(5),
    time_end VARCHAR(5),
    subject VARCHAR(25),
    teacher VARCHAR(25));

INSERT INTO tuesday(time_start, time_end, subject) VALUES ('9:30','11:05','');
INSERT INTO tuesday(time_start, time_end, subject) VALUES ('11:20','12:55','');
INSERT INTO tuesday(time_start, time_end, subject) VALUES ('13:10','14:45','');
INSERT INTO tuesday(time_start, time_end, subject) VALUES ('15:25','17:00','');
INSERT INTO tuesday(time_start, time_end, subject) VALUES ('17:25','19:00','');

DROP TABLE IF EXISTS wednesday;
CREATE TABLE wednesday(
    num SERIAL PRIMARY KEY,
    time_start VARCHAR(5),
    time_end VARCHAR(5),
    subject VARCHAR(25),
    teacher VARCHAR(25));

INSERT INTO wednesday(time_start, time_end, subject) VALUES ('9:30','11:05','');
INSERT INTO wednesday(time_start, time_end, subject) VALUES ('11:20','12:55','');
INSERT INTO wednesday(time_start, time_end, subject) VALUES ('13:10','14:45','');
INSERT INTO wednesday(time_start, time_end, subject) VALUES ('15:25','17:00','');
INSERT INTO wednesday(time_start, time_end, subject) VALUES ('17:25','19:00','');

INSERT INTO timestamps(time_start,time_end) VALUES\

UPDATE