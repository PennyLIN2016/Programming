select DISTINCT a.num as ConsecutiveNum from logs a,logs b,logs c
where a.Id = b.Id -1 and b.Id = c.Id-1
and a.num = b.num and c.num = d.num