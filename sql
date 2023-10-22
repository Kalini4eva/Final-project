SELECT c.login,
       COUNT(*)
FROM "Orders" AS o
INNER JOIN "Couriers" AS c ON c.id = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;


SELECT track,
       CASE WHEN  finished=true THEN 2
       WHEN cancelled=true THEN -1
       WHEN "inDelivery"=true THEN 1
       ELSE 0
       END
FROM "Orders";
