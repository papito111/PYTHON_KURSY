select *,
revenue - budget as profit from financials
order by profit desc;

select *,
if(currency="USD",revenue *77, revenue)  as revenue_inr from financials
order by revenue_inr desc;

select *,
	case
		when unit='Thousands' then round(revenue/1000,1)
        when unit='Billions' then round(revenue*1000,1)
        when unit='Millions' then round(revenue,1)
	end as revenue_mln
from financials
order by revenue_mln desc;

select 
movie_id, title, budget, revenue, currency, 
	case
		when unit='Thousands' then round(revenue/1000,1) and round(budget/1000,1)
        when unit='Billions' then round(revenue*1000,1)
        when unit='Millions' then round(revenue,1)
	end as revenue_mln,
    case
		when unit='Thousands' then round(budget/1000,1) 
        when unit='Billions' then round(budget*1000,1)
        when unit='Millions' then round(budget,1)
	end as budget_mln
from movies  -- m jest jako left
right join financials 
using (movie_id)

UNION

select 
m.movie_id, title, budget, revenue, currency, 
case
		when currency = 'INR' then round(revenue *  0.014,1) 
		when unit='Thousands' then round(revenue/1000,1) and round(budget/1000,1)
        when unit='Billions' then round(revenue*1000,1)
        when unit='Millions' then round(revenue,1)
	end as revenue_mln,
    case
		when unit='Thousands' then round(budget/1000,1) 
        when unit='Billions' then round(budget*1000,1)
        when unit='Millions' then round(budget,1)
	end as budget_mln
from movies m -- m jest jako left
left join financials f
on m.movie_id = f.movie_id;



select 
    m.movie_id, 
    m.title, 
    f.budget, 
    f.revenue, 
    m.movie_id, 
    m.title, 
 
    case
        when f.currency = 'INR' and f.unit = 'Billions' then round(f.revenue * 0.014 * 1000, 1) 
        when f.currency = 'INR' and f.unit = 'Thousands' then round(f.revenue * 0.014 / 1000, 1) 
        when f.currency = 'INR' and f.unit = 'Millions' then round(f.revenue * 0.014 , 1) 
        when f.unit = 'Thousands' then round(f.revenue / 1000, 1)
        when f.unit = 'Billions' then round(f.revenue * 1000, 1)
        when f.unit = 'Millions' then round(f.revenue, 1)
    end as revenue_mln$,
    case
		when f.currency = 'INR' and f.unit = 'Billions' then round(f.budget * 0.014 * 1000, 1) 
        when f.currency = 'INR' and f.unit = 'Thousands' then round(f.budget * 0.014 / 1000, 1) 
        when f.currency = 'INR' and f.unit = 'Millions' then round(f.budget * 0.014 , 1) 
        when f.unit = 'Thousands' then round(f.budget / 1000, 1)
        when f.unit = 'Billions' then round(f.budget * 1000, 1)
        when f.unit = 'Millions' then round(f.budget, 1)
    end as budget_mln$,
	case
		when f.currency = 'INR' and f.unit = 'Billions' then round((f.revenue - f.budget)  * 0.014 * 1000, 1) 
        when f.currency = 'INR' and f.unit = 'Thousands' then round((f.revenue - f.budget) * 0.014 / 1000, 1) 
         when f.currency = 'INR' and f.unit = 'Millions' then round((f.revenue - f.budget) * 0.014 , 1) 
        when f.unit = 'Thousands' then round((f.revenue - f.budget) / 1000, 1)
        when f.unit = 'Billions' then round((f.revenue - f.budget) * 1000, 1)
        when f.unit = 'Millions' then round((f.revenue - f.budget), 1)
    end as profit_mln$
	
from 
    movies m
    left join financials f on m.movie_id = f.movie_id;



