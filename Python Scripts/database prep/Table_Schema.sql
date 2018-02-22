drop table if exists DataReceived;

create table DataReceived (
    sendTime text,
    heading text,
    roll text,
    pitch text,
    tempC text,
    leftState text,
    rightState text
);
