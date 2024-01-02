
SELECT  * FROM movies where title LIKE "%Captain%";
select	distinct industry from movies;
select * from movies where title like "%Thor%";
select * from movies where industry = "Bollywood";
select * from movies where studio = "Hombale Films";
select * from movies where imdb_rating >8.5;
SELECT * from movies where imdb_rating between 6 and 8;
SELECT * from movies where release_year=2022 or release_year = 2021 or release_year = 2019;
select * from movies where language_id in(3,2,5);
select * from movies where industry = "hollywood" order by imdb_rating desc limit 5 offset 1;

select studio, COUNT(studio) as cnt,
	avg(imdb_rating) as avg,
	max(imdb_rating) as max,
	min(imdb_rating) as min
from movies 
where studio !=""
group by studio 
order by max desc;

select round(avg(imdb_rating),2) as AVG_RATING, max(imdb_rating) as MAX_RATING, min(imdb_rating) as MIN_RATING from movies where studio like "%marvel%";

select release_year, count(*) as movies_count
from movies
group by release_year
having release_year >= 2000 and movies_count >=2
order by release_year desc;



