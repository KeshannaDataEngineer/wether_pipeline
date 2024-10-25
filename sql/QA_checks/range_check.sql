SELECT * FROM weather
WHERE temperature < -50 OR temperature > 60
   OR relative_humidity < 0 OR relative_humidity > 100
   OR precipitation < 0;
