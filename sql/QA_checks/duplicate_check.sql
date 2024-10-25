SELECT venue_id, timestamp, COUNT(*)
FROM weather
GROUP BY venue_id, timestamp
HAVING COUNT(*) > 1;
