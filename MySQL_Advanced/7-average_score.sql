-- Task 7

-- Creates a stored procedure 'ComputeAverageScoreForUser'
-- that computes and store the average for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN

DECLARE nbr_of_score FLOAT;
DECLARE total_score FLOAT;

SELECT COUNT(*) INTO nbr_of_score FROM corrections WHERE user_id = input_user_id;
SELECT 'nbr_of_score', nbr_of_score;
IF nbr_of_score != 0 THEN

SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = input_user_id ;


UPDATE users SET average_score = total_score / nbr_of_score WHERE id = input_user_id;


END IF ;



END //

DELIMITER ;