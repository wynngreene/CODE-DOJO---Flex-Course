SELECT ninjas.first_name, ninjas.last_name, dojos.name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas_id = 6;