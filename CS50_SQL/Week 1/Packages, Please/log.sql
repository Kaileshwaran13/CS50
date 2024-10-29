
-- *** The Lost Letter ***
SELECT * FROM addresses
WHERE address = "900 Somerville Avenue";

SELECT * FROM addresses
WHERE address LIKE "2 Fin%";


-- *** The Devious Delivery ***

SELECT * FROM PACKAGES
WHERE from_address_id IS NULL;

SELECT * FROM scans
WHERE package_id = (
    SELECT id FROM PACKAGES
    WHERE from_address_id IS NULL
)AND action = "Drop";

SELECT * from addresses
WHERE id = (
    SELECT address_id FROM scans
    WHERE package_id = (
        SELECT id FROM PACKAGES
        WHERE from_address_id IS NULL
    )AND action = "Drop"
);

-- *** The Forgotten Gift ***


SELECT * FROM addresses
WHERE address = "728 Maple Place";

SELECT * FROM scans
where address_id = (
    SELECT id FROM addresses
    WHERE address = "728 Maple Place"
);

SELECT * FROM packages
WHERE to_address_id =(
    SELECT address_id FROM scans
    where address_id = (
        SELECT id FROM addresses
        WHERE address = "728 Maple Place"
    )
);

SELECT * FROM scans
WHERE package_id = (
    SELECT id FROM packages
    WHERE to_address_id =(
        SELECT address_id FROM scans
        where address_id = (
            SELECT id FROM addresses
            WHERE address = "728 Maple Place"
        )
    )
) ORDER BY timestamp DESC LIMIT 1;


SELECT name FROM drivers
WHERE id = (
    SELECT driver_id FROM scans
    WHERE package_id = (
        SELECT id FROM packages
        WHERE to_address_id =(
            SELECT address_id FROM scans
            where address_id = (
                SELECT id FROM addresses
                WHERE address = "728 Maple Place"
            )
        )
    ) ORDER BY timestamp DESC LIMIT 1
) ;

