SELECT
	CASE
		WHEN (A + B <= C) OR (B + C <= A) OR (A + C <= B) THEN 'Not A Triangle'
        WHEN (A = B) AND (A = C) THEN 'Equilateral'
        WHEN (A = B) OR (A =C) OR (B = C) THEN 'Isosceles'
        ELSE 'Scalene'
	END
FROM TRIANGLES