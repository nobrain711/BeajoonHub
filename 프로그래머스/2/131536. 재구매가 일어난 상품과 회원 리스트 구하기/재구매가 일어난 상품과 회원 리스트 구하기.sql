-- 코드를 입력하세요
SELECT  user_id, product_id
FROM    online_sale
GROUP   BY  USER_ID, product_id
HAVING  COUNT(*)>1
ORDER   BY  user_id,
    product_id desc