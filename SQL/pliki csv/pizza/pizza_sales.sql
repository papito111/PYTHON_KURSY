use pizza_db;

select 
SUM(quantity * price) as total_revenue
from order_details as od
join pizzas as p
on od.pizza_id = p.pizza_id
order by quantity desc;

select 
round(sum(quantity * price)/ count(distinct order_id),2) as average_order_value
from order_details as od
join pizzas as p
on od.pizza_id = p.pizza_id;

select
sum(quantity) as Total_pizzas_sold
from order_details as od
join pizzas as p
on od.pizza_id = p.pizza_id;

select
count(distinct order_id) as Total_orders
from order_details as od
join pizzas as p
on od.pizza_id = p.pizza_id;

select
sum(quantity)/count(distinct order_id) as avg_pizzas_for_order
from order_details as od
join pizzas as p
on od.pizza_id = p.pizza_id;

select str_to_date(date1,'%Y-%m-%d') as date_ from orders;
select * from orders;

select 
str_to_date(date1,'%Y-%m-%d'),
format(date1,'dddd') as DayOfWeek,
count(distinct order_id) as total_orders
from orders
group by format( STR_TO_DATE(date1, '%Y-%m-%d'))
order by total_orders desc;



SELECT
  STR_TO_DATE(date1, '%Y-%m-%d') AS formatted_date,
  FORMAT(formatted_date, 'dddd') AS DayOfWeek,
  COUNT(DISTINCT order_id) AS total_orders
FROM
  orders
GROUP BY
  formatted_date, DayOfWeek
ORDER BY
  total_orders DESC;


SELECT
  DAYNAME(STR_TO_DATE(date1, '%Y-%m-%d')) AS DayOfWeek,
  COUNT(DISTINCT order_id) AS total_orders
FROM
  orders
GROUP BY
  DayOfWeek
ORDER BY
  total_orders DESC;

SELECT 
    DATE_FORMAT(STR_TO_DATE(time1, '%H:%i:%s'), '%H') AS HourOfDay,
    COUNT(DISTINCT order_id) AS total_orders
FROM 
    orders
GROUP BY 
    DATE_FORMAT(STR_TO_DATE(time1, '%H:%i:%s'), '%H')
ORDER BY 
    total_orders DESC;

select category,
round(sum(quantity * price)) as revenue,
round(sum(quantity * price) * 100/(select sum(quantity * price) from pizzas as p2
join order_details as od2 on od2.pizza_id = p2.pizza_id),1) as percentage_sales
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by category
order by percentage_sales desc;

select category,
sum(quantity) as quantity
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by category
order by quantity desc;

select size,
sum(quantity) as quantity
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by size
order by quantity desc;

#top 5 best selling pizzas
select name ,
sum(quantity) as quantity
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by name
order by quantity desc
Limit 5;

#top 5 worst selling pizzas
select name ,
sum(quantity) as quantity
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by name
order by quantity asc
Limit 5;

select size,
round(sum(quantity * price)) as revenue,
round(sum(quantity * price) * 100/(select sum(quantity * price) from pizzas as p2
join order_details as od2 on od2.pizza_id = p2.pizza_id),1) as percentage_sales
from pizzas as p
join pizza_types as pt on p.pizza_type_id = pt.pizza_type_id
join order_details as od on p.pizza_id = od.pizza_id
group by size
order by percentage_sales desc;






