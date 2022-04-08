DELIMITER $$

CREATE TRIGGER wipe_cart
before update 
ON core_cart FOR EACH ROW
BEGIN
	if NEW.numofproducts =0 then
		DELETE from core_cartdetails where CartID=old.CartID;
	end if;
END $$
DELIMITER ;
drop trigger wipe_cart
