use world;

create table movies (
	name text,
    genre text,
    year integer,
    imdb_rating integer
    );
    
select name, genre, year
from movies;

insert into movies (name, genre, year)
values ('Batman', action, 2008);

insert into movies (name, genre, year)
values ('Avengers: Endgame', action, 2018);

insert into movies (name, genre, year)
values ('Batman v. Superman: Dawn of Justice', action, 2016);

    
    