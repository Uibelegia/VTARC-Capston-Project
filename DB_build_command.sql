CREATE DATABASE IF NOT EXISTS vtarc;
CREATE TABLE IF NOT EXISTS vtarc.list
(
    rank_other         int,
    rank_vtarc         int,
    rank_justification varchar(1000),
    source             varchar(50),
    name               varchar(100),
    last_name          varchar(50),
    institution        varchar(150),
    title              varchar(100),
    domain             varchar(50),
    gender             varchar(50),
    topic              varchar(50),
    description        varchar(500),
    fields             varchar(100),
    key_notes          varchar(1000),
    links              varchar(500),
    email              varchar(500),
    website            varchar(500),
    pub                int,
    citation           bigint,
    hindex             int,
    h5index            int,
    id                 bigint,
    invited_attend     varchar(10),
    attended           varchar(10),
    uniq                bigint AUTO_INCREMENT primary key NOT NULL
);