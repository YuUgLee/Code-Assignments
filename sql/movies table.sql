use world;#must have a database to to make table in
create table ratings (
	imdb_rating integer,
    year integer
    );
    
select * from movies join ratings;
    
create table movies ( #to create the table
	name text,
    genre text,
    year integer,
    imdb_rating integer
    );
    
select name, genre, year #select shows everything without having to type up all columns
from movies; #like a print statement to show the table

insert into movies (name, genre, year, imdb_rating) #to insert values into table
values ('Batman', 'action', 2008, 5);

insert into movies (name, genre, year, imdb_rating)
values ('Avengers: Endgame', 'action', 2018, 7);

insert into movies (name, genre, year, imdb_rating)
values ('Batman v. Superman: Dawn of Justice', 'action', 2016, 10);

select name, genre from movies where genre = 'action';
select * from movies order by imdb_rating desc
	limit 2;
    
SELECT name,
	case
     when imdb_rating > 5 then 'Good Enough'
     else 'Do not even bother'
	end
from movies;
insert into ratings (imdb_rating)
values (3);

insert into movies (imdb_rating)
values (3);

insert into movies (imdb_rating)
values (7);

insert into movies (imdb_rating)
values (2);

select name as 'Titles' #changes the text display of the column in the result but not the actual table
from movies;

select imdb_rating as 'IMDb'
from movies;

select distinct name, genre, year
from movies;
select count(*) from movies;
select sum(imdb_rating) from movies;
select max(imdb_rating) from movies;
select min(imdb_rating) from movies;
select avg(imdb_rating) from movies;

select * from movies
where imdb_rating <5;

select * from movies
where name like 'Ba_man'; #can replace underlined with any character(s) 
select * from movies where name like '%man%';

select * from movies
left join ratings
	on movies.imdb_rating= ratings.imdb_rating;


    
    