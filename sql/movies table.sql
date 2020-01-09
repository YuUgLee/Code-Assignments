use world;#must have a database to to make table in

create table movies ( #to create the table
	name text,
    genre text,
    year integer,
    imdb_rating integer
    );
    
select name, genre, year #select * shows everything without having to type up all columns
from movies; #like a print statement to show the table

insert into movies (name, genre, year) #to insert values into table
values ('Batman', 'action', 2008);

insert into movies (name, genre, year)
values ('Avengers: Endgame', 'action', 2018);

insert into movies (name, genre, year)
values ('Batman v. Superman: Dawn of Justice', 'action', 2016);

select name as 'Titles' #changes the text display of the column in the result but not the actual table
from movies;

select imdb_rating as 'IMDb'
from movies;

select distinct name, genre, year
from movies;



    
    