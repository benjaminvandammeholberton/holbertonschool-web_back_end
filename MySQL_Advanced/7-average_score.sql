-- Task 7

-- Creates a stored procedure 'ComputeAverageScoreForUser'
-- that computes and store the average for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN

DECLARE nbr_of_score INT;
DECLARE total_score INT;

SELECT COUNT(*) INTO nbr_of_score FROM corrections WHERE user_id = user_id;

IF nbr_of_score != 0 THEN

SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id ;


UPDATE users SET average_score = total_score / nbr_of_score WHERE id = user_id;


END IF ;



END //

DELIMITER ;