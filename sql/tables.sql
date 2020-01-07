use world;

insert into celebs (id, name, age)
values (1, 'Justin Bieber', 22);

insert into celebs (id, name, age)
values (2, 'Beyonce Knowles', 33);

insert into celebs (id, name, age)
values (3, 'Jeremy Lin', 26);

insert into celebs (id, name, age)
values (4, 'Taylor Swift', 26);

delete from celebs
where twitter_handle is not null;
select * from celebs;