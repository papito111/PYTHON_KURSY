select *,
year(curdate())- birth_year as age from actors
order by age desc;