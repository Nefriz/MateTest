

select week(leads.created_at) AS week_number,
    leads.status,
    COUNT(leads.id) as lead_count
from leads
inner join courses on leads.course_id = courses.id
group by week_number, leads.status
;

select domains.country_name as CountryName,
       count(leads.id) as Leads
from leads
inner join courses on leads.course_id = courses.id
inner join users on leads.user_id = users.id
inner join domains on users.domain_id = domains.id
where leads.status = 'Won'
and courses.type = 'FLEX'
and leads.created_at >= '2024-01-01'
group by domains.country_name

select users.email, leads.id, leads.lost_reason
from leads
inner join courses on courses.id = leads.course_id
inner join users on leads.user_id = users.id
where leads.status = 'LOST' and
    courses.type = 'FLEX' and
    leads.created_at >= '2024-07-01';

