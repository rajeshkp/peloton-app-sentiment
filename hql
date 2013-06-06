select sq.wd as sentiment, sum(sq.cnt) as score from (MAP * using 'python ./sentiment_mapper.py' as (wd, cnt) from (${hql}) ana) sq group by sq.wd
