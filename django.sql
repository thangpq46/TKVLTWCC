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
drop trigger wipe_cart;


CREATE TRIGGER delete_order_on_delete_details
after delete 
ON order_details FOR EACH ROW
BEGIN
	delete from core_orders where OrderID=OLD.OrderID
END $$
DELIMITER ;
drop trigger delete_order_on_delete_details;

CREATE TRIGGER on_delete_product
before delete 
ON core_product FOR EACH ROW
BEGIN
	delete from core_orders where OrderID in(
		select DISTINCT OrderID from core_orderdetails where ProductID=Old.ID)
	select a.DeltailsID,a.quantity,a.CartID,a.ProductID,b.numofproducts,b.Total,c.ID,c.Price from core_cartdetails a inner join core_cart b on a.CartID=b.CartID inner join core_product c on a.ProductID=c.ID
END $$
DELIMITER ;

INSERT INTO `core_brand` VALUES (1,'Acer',NULL,'lrg_acer-228x228_RKEhTaO.png'),(2,'Apple',NULL,'Logo-228x228_gi51xp4.jpg'),(3,'Asus',NULL,'lrg_asus-228x228_IlxY1cV.png'),(4,'Dell',NULL,'dell_2016_logo-228x228_MGIPKsH.png'),(5,'Hp',NULL,'HP_logo_2012.svg-228x228_80ULYZz.png'),(7,'LG',NULL,'Lg_logo-3-228x228_GtcBjKX.png'),(8,'Philips',NULL,'Philips-228x228.png'),(9,'Msi',NULL,'msi-corporate_identity-logo-black-rgb-png-228x228_wvHg2Qi.png'),(10,'Lenovo',NULL,'lenovo-logo_Yz01uGa.png');