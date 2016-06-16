--
-- SELECT
--
select * from products;

select count(*) from products;

SELECT name, price FROM products WHERE price < 1.0;
SELECT name, quantity FROM products WHERE quantity <= 2000;
SELECT name, price FROM products WHERE productCode = 'PEN';

-- LIKE and NOT LIKE --
SELECT name, price FROM products WHERE name LIKE 'PENCIL%';
SELECT name, price FROM products WHERE name LIKE 'P__ %';

-- AND, OR, NOT, XOR --
SELECT * FROM products WHERE quantity >= 5000 AND name LIKE 'Pen %';
SELECT * FROM products WHERE quantity >= 5000 AND price < 1.24 AND name LIKE 'Pen %';
SELECT * FROM products WHERE NOT (quantity >= 5000 AND name LIKE 'Pen %');

-- IN, NOT IN --
SELECT * FROM products WHERE name IN ('Pen Red', 'Pen Black');

-- BETWEEN, NOT BETWEEN --
SELECT * FROM products WHERE (price BETWEEN 1.0 AND 2.0) AND (quantity BETWEEN 1000 AND 2000);

-- IS NULL, IS NOT NULL --
SELECT * FROM products WHERE productCode IS NULL;
SELECT * FROM products WHERE productCode = NULL;  -- This is a common mistake. NULL cannot be compared.

--
-- ORDER BY
--
select * from products order by price ASC;  -- 升序排序
select * from products order by price DESC;  -- 降序排列
SELECT * FROM products ORDER BY RAND();  -- 随机顺序

--
-- LIMIT
--
SELECT * FROM products ORDER BY price LIMIT 2;
SELECT * FROM products ORDER BY price LIMIT 2, 1;

--
-- AS
--
SELECT productID AS ID, productCode AS Code,
              name AS Description, price AS `Unit Price`  -- Define aliases to be used as display names
       FROM products
       ORDER BY ID;  -- Use alias ID as reference

--
-- Function CONCAT()
--
SELECT CONCAT(productCode, ' - ', name) AS `Product Description`, price FROM products;

--
-- DISTINCT
--
SELECT price FROM products;
SELECT DISTINCT price AS `Distinct Price` FROM products;
SELECT DISTINCT price, name FROM products;

--
-- GROUP BY
--
SELECT * FROM products GROUP BY productCode;

-- GROUP BY Aggregate Functions: COUNT, MAX, MIN, AVG, SUM, STD, GROUP_CONCAT
SELECT COUNT(*) AS `Count` FROM products;
SELECT productCode, COUNT(*) FROM products GROUP BY productCode;
SELECT productCode, COUNT(*) AS count
       FROM products
       GROUP BY productCode
       ORDER BY count DESC;

SELECT MAX(price), MIN(price), AVG(price), STD(price), SUM(quantity) FROM products;

SELECT productCode, MAX(price) AS `Highest Price`, MIN(price) AS `Lowest Price`
       FROM products
       GROUP BY productCode;

SELECT productCode, MAX(price), MIN(price),
              CAST(AVG(price) AS DECIMAL(7,2)) AS `Average`,
              CAST(STD(price) AS DECIMAL(7,2)) AS `Std Dev`,
              SUM(quantity)
       FROM products
       GROUP BY productCode;

--
-- HAVING
--
SELECT
          productCode AS `Product Code`,
          COUNT(*) AS `Count`,
          CAST(AVG(price) AS DECIMAL(7,2)) AS `Average`
       FROM products 
       GROUP BY productCode
       HAVING Count >=3;
       -- CANNOT use WHERE count >= 3

--
-- WITH ROLLUP
--
SELECT 
          productCode, 
          MAX(price), 
          MIN(price), 
          CAST(AVG(price) AS DECIMAL(7,2)) AS `Average`,
          SUM(quantity)
       FROM products
       GROUP BY productCode
       WITH ROLLUP;        -- Apply aggregate functions to all groups

--
-- UPDATE
--
UPDATE products SET price = price * 1.1;  -- Increase the price by 10% for all products
UPDATE products SET quantity = quantity - 100 WHERE name = 'Pen Red';  -- Modify selected rows
UPDATE products SET quantity = quantity + 50, price = 1.23 WHERE name = 'Pen Red';

--
-- delete
--
DELETE FROM products WHERE productID = 1006;
DELETE FROM products WHERE name LIKE 'Pencil%';
DELETE FROM products;

--
-- SELECT with JOIN
--
SELECT products.name, price, suppliers.name 
       FROM products 
          JOIN suppliers ON products.supplierID = suppliers.supplierID
       WHERE price < 0.6;

SELECT products.name, price, suppliers.name 
       FROM products, suppliers 
       WHERE products.supplierID = suppliers.supplierID
          AND price < 0.6;

SELECT products.name AS `Product Name`, price, suppliers.name AS `Supplier Name` 
       FROM products 
          JOIN suppliers ON products.supplierID = suppliers.supplierID
       WHERE price < 0.6;

SELECT p.name AS `Product Name`, p.price, s.name AS `Supplier Name` 
       FROM products AS p 
          JOIN suppliers AS s ON p.supplierID = s.supplierID
       WHERE p.price < 0.6;

--
-- index
--
SHOW INDEX FROM employees;

--
-- Many-To-Many Relationship
--

SELECT products.name AS `Product Name`, price, suppliers.name AS `Supplier Name`
       FROM products_suppliers 
          JOIN products  ON products_suppliers.productID = products.productID
          JOIN suppliers ON products_suppliers.supplierID = suppliers.supplierID
       WHERE price < 0.6;

SELECT p.name AS `Product Name`, s.name AS `Supplier Name`
       FROM products_suppliers AS ps 
          JOIN products AS p ON ps.productID = p.productID
          JOIN suppliers AS s ON ps.supplierID = s.supplierID
       WHERE p.name = 'Pencil 3B';

SELECT p.name AS `Product Name`, s.name AS `Supplier Name`
       FROM products AS p, products_suppliers AS ps, suppliers AS s
       WHERE p.productID = ps.productID
          AND ps.supplierID = s.supplierID
          AND s.name = 'ABC Traders';

--
-- One-to-one Relationship
--
CREATE TABLE product_details (
          productID  INT UNSIGNED   NOT NULL,
                     -- same data type as the parent table
          comment    TEXT  NULL,
                     -- up to 64KB
          PRIMARY KEY (productID),
          FOREIGN KEY (productID) REFERENCES products (productID)
       );



select crm_progress.id, progress, project_id from crm_progress join 
    (select max(id) as max_id from crm_progress group by project_id) b 
	on crm_progress.id=b.max_id;



