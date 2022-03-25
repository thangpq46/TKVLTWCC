-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tkvltw
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add address',7,'add_address'),(26,'Can change address',7,'change_address'),(27,'Can delete address',7,'delete_address'),(28,'Can view address',7,'view_address'),(29,'Can add brand',8,'add_brand'),(30,'Can change brand',8,'change_brand'),(31,'Can delete brand',8,'delete_brand'),(32,'Can view brand',8,'view_brand'),(33,'Can add cart',9,'add_cart'),(34,'Can change cart',9,'change_cart'),(35,'Can delete cart',9,'delete_cart'),(36,'Can view cart',9,'view_cart'),(37,'Can add orders',10,'add_orders'),(38,'Can change orders',10,'change_orders'),(39,'Can delete orders',10,'delete_orders'),(40,'Can view orders',10,'view_orders'),(41,'Can add product',11,'add_product'),(42,'Can change product',11,'change_product'),(43,'Can delete product',11,'delete_product'),(44,'Can view product',11,'view_product'),(45,'Can add orderdetails',12,'add_orderdetails'),(46,'Can change orderdetails',12,'change_orderdetails'),(47,'Can delete orderdetails',12,'delete_orderdetails'),(48,'Can view orderdetails',12,'view_orderdetails'),(49,'Can add cartdetails',13,'add_cartdetails'),(50,'Can change cartdetails',13,'change_cartdetails'),(51,'Can delete cartdetails',13,'delete_cartdetails'),(52,'Can view cartdetails',13,'view_cartdetails'),(53,'Can add profile',14,'add_profile'),(54,'Can change profile',14,'change_profile'),(55,'Can delete profile',14,'delete_profile'),(56,'Can view profile',14,'view_profile'),(57,'Can add feedback',15,'add_feedback'),(58,'Can change feedback',15,'change_feedback'),(59,'Can delete feedback',15,'delete_feedback'),(60,'Can view feedback',15,'view_feedback');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (15,'pbkdf2_sha256$260000$c5I0hoNftOUBAZHdH4xKJh$pPLEfPlQKb4HRe9wp3fj26hhM/tRsfdDzYoUh+xz8YY=',NULL,1,'admin','','','',1,1,'2022-01-07 07:32:47.511935'),(16,'pbkdf2_sha256$260000$GL1QdQbkosew4pxjdnGCVC$8JagmVzRJjjjnPrfiYD5vjcFVPARmu8nuFEyMV3eLf4=',NULL,0,'tin','Đức','Tin','ductin@gmail.com',0,1,'2022-01-07 08:44:41.381515');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_address`
--

DROP TABLE IF EXISTS `core_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_address` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `Default Address` varchar(45) DEFAULT NULL,
  `ShippingAddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_address`
--

LOCK TABLES `core_address` WRITE;
/*!40000 ALTER TABLE `core_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_brand`
--

DROP TABLE IF EXISTS `core_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_brand` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `BrandName` varchar(200) NOT NULL,
  `BrandDes` varchar(2000) DEFAULT NULL,
  `IMG` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_brand`
--

LOCK TABLES `core_brand` WRITE;
/*!40000 ALTER TABLE `core_brand` DISABLE KEYS */;
INSERT INTO `core_brand` VALUES (1,'Acer',NULL,'lrg_acer-228x228_RKEhTaO.png'),(2,'Apple',NULL,'Logo-228x228_gi51xp4.jpg'),(3,'Asus',NULL,'lrg_asus-228x228_IlxY1cV.png'),(4,'Dell',NULL,'dell_2016_logo-228x228_MGIPKsH.png'),(5,'Hp',NULL,'HP_logo_2012.svg-228x228_80ULYZz.png'),(7,'LG',NULL,'Lg_logo-3-228x228_GtcBjKX.png'),(8,'Philips',NULL,'Philips-228x228.png'),(9,'Msi',NULL,'msi-corporate_identity-logo-black-rgb-png-228x228_wvHg2Qi.png'),(10,'Lenovo',NULL,'lenovo-logo_Yz01uGa.png');
/*!40000 ALTER TABLE `core_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cart`
--

DROP TABLE IF EXISTS `core_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cart` (
  `CartID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(150) NOT NULL,
  `CartTotal` double NOT NULL,
  `Cartnum` varchar(45) DEFAULT NULL,
  `typecart` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CartID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cart`
--

LOCK TABLES `core_cart` WRITE;
/*!40000 ALTER TABLE `core_cart` DISABLE KEYS */;
INSERT INTO `core_cart` VALUES (1,'admin',0,NULL,NULL),(10,'tin',1187,NULL,NULL);
/*!40000 ALTER TABLE `core_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_cartdetails`
--

DROP TABLE IF EXISTS `core_cartdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_cartdetails` (
  `DeltailsID` int NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `Price` double NOT NULL,
  `username` varchar(200) NOT NULL,
  `ProductName` varchar(200) NOT NULL,
  `IMG` varchar(200) NOT NULL,
  PRIMARY KEY (`DeltailsID`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_cartdetails`
--

LOCK TABLES `core_cartdetails` WRITE;
/*!40000 ALTER TABLE `core_cartdetails` DISABLE KEYS */;
INSERT INTO `core_cartdetails` VALUES (43,1,1187,'tin','Laptop Gaming Acer Nitro 5 Eagle AN515-57-71VV i7-11800H/ 8GB/ 512GB/ RTX 3050 4GB/ Win 11','http://127.0.0.1:8000/images/laptop-acer-nitro5-eagle-01-500x500_ya3hlFc.jpg');
/*!40000 ALTER TABLE `core_cartdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_feedback`
--

DROP TABLE IF EXISTS `core_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_feedback` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `topic` varchar(200) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Des` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_feedback`
--

LOCK TABLES `core_feedback` WRITE;
/*!40000 ALTER TABLE `core_feedback` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_orderdetails`
--

DROP TABLE IF EXISTS `core_orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_orderdetails` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `OrderID` int NOT NULL,
  `Quantity` int NOT NULL,
  `Price` double NOT NULL,
  `ProductName` varchar(200) NOT NULL,
  `IMG` varchar(200) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_orderdetails`
--

LOCK TABLES `core_orderdetails` WRITE;
/*!40000 ALTER TABLE `core_orderdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_orderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_orders`
--

DROP TABLE IF EXISTS `core_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_orders` (
  `OrderID` int NOT NULL AUTO_INCREMENT,
  `OrderAddress` varchar(500) DEFAULT NULL,
  `username` varchar(200) NOT NULL,
  `OrderDate` date NOT NULL,
  `OrderStatus` varchar(200) DEFAULT NULL,
  `Total` int DEFAULT NULL,
  PRIMARY KEY (`OrderID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_orders`
--

LOCK TABLES `core_orders` WRITE;
/*!40000 ALTER TABLE `core_orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_product`
--

DROP TABLE IF EXISTS `core_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_product` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ProductCode` varchar(200) DEFAULT NULL,
  `Name` varchar(200) NOT NULL,
  `Price` double NOT NULL,
  `IMG` varchar(200) NOT NULL,
  `Description` varchar(2000) DEFAULT NULL,
  `Stock` int NOT NULL,
  `CreateDate` date NOT NULL,
  `BrandName` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `core_product_BrandName_97c511ea_fk_core_brand_ID` (`BrandName`),
  CONSTRAINT `core_product_BrandName_97c511ea_fk_core_brand_ID` FOREIGN KEY (`BrandName`) REFERENCES `core_brand` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_product`
--

LOCK TABLES `core_product` WRITE;
/*!40000 ALTER TABLE `core_product` DISABLE KEYS */;
INSERT INTO `core_product` VALUES (8,'AN515-57-71VV','Laptop Gaming Acer Nitro 5 Eagle AN515-57-71VV i7-11800H/ 8GB/ 512GB/ RTX 3050 4GB/ Win 11',1187,'laptop-acer-nitro5-eagle-01-500x500_ya3hlFc.jpg','- CPU: Intel® Core™ i7-11800H (upto 4.60GHz, 24MB)\n\n- RAM: 8GB DDR4 khe rời 3200MHz (2 khe, tối đa 32GB)\n\n- Ổ cứng: 512GB PCIe NVMe SSD cắm sẵn (nâng cấp tối đa 2TB SSD PCIe Gen3, 8 Gb/s, NVMe và 2TB HDD 2.5-inch 5400 RPM)\n\n- VGA: NVIDIA® GeForce RTX™ 3050 4GB GDDR6\n\n- Màn hình: 15.6 inch FHD(1920 x 1080) IPS 144Hz slim bezel LCD, Acer ComfyView LED-backlit TFT LCD\n\n- Pin: 57.5 Wh, 4-cell\n\n- Cân nặng: 2.2 kg\n\n- Tính năng: Đèn nền bàn phím\n\n- Màu sắc: Shale Black\n\n- OS: Windows 11 Home',15,'2022-01-07',1),(9,'A715-42G-R1SB','Laptop Acer Aspire 7 A715-42G-R1SB R5-5500U/ 8GB/ 256GB/ GTX 1650 4GB/ 15.6 inch FHD/ Win 10',989,'acer-predator-triton-300-pt315-53-71dj-i7-600x600.jpg','- CPU: AMD Ryzen R5-5500U (8MB, 2.1GHz up to 4.00GHz)\n- RAM: 8GB(1x8GB) DDR4 3200MHz\n- Ổ cứng: 256GB PCIe NVMe SSD cắm sẵn (nâng cấp tối đa 1TB SSD)\n- VGA: NVIDIA GeForce GTX 1650 4GB GDDR6\n- Màn hình: 15.6 inch FHD(1920 x 1080) 144Hz SlimBezel, Acer ComfyView™ IPS LED LCD\n- Pin: 48 Wh\n- Cân nặng: 2.1kg\n- Màu sắc: Đen\n- Tính năng: Đèn nền bàn phím\n- OS: Windows 10 Home',18,'2022-01-07',1),(10,'GA503QC-HN074T','Laptop Asus ROG Zephyrus G15 GA503QC-HN074T R9-5900HS/ 16GB/ 512GB/ RTX 3050 4GB',1298,'asus-tuf-gaming-fx516pe-i7-hn005t-600x600.jpg','- CPU: AMD Ryzen 9-5900HS (3.0GHz up to 4.6GHz, 16MB)\n- RAM: 16GB(8GB + 8GB[On board]) DDR4 3200MHz (1x SO-DIMM slot)\n- Ổ cứng: 512GB M.2 NVMe™ PCIe® 3.0 SSD\n- VGA: NVIDIA® GeForce RTX™ 3050 4GB GDDR6\n- Màn hình: 15.6 inch FHD (1920 x 1080)-144Hz\n- Pin: 4-cell, 90WHrs Li-ion\n- Cân nặng: 1.9 KG\n- HĐH: Windows 10 Home',20,'2022-01-07',3),(11,'m15-R6-01NS','Laptop Gaming Dell Alienware m15 - R6 - 01NS i7-11800H/16GB/1TB/2K 240Hz/RTX 3060 6GB',2447,'dell-gaming-g15-5515-r5-p105f004cgr-291121-115616-600x600.jpg','- Vi xử lý: Intel Core i7 11800H, 8 nhân / 16 luồng\n- Màn hình: 15.6\" QHD (2560 x 1440) 240Hz chống chói\n- RAM: 16GB DDR4 bus 3200 MHz (Nâng cấp tối đa 64GB)\n- Card đồ họa: Nvidia RTX3060 6GB GDDR6\n- Lưu trữ: 1TB m.2 NVMe (Nâng cấp tối đa 2TB x 2)\n- Pin: 86Wh\n- Kết nối chính: 1 x USB-C 3.2 Gen 2 (Hỗ trợ xuất hình DisplayPort 1.4), 3 x USB-A 3.2 Gen 1, 1 x HDMI 2.1, 1 x RJ-45, 1 x jack 3.5mm\n- Cân nặng: 2.69kg\n- Hệ điều hành: Windows 10 Home ',5,'2022-01-07',4),(12,'Z11D000E5','Laptop Apple MacBook Pro M1 2020/16GB/256GB (Z11D000E5)',1638,'macbook-pro-m1-2020-silver-600x600.jpg','- CPU: Intel® Core™ i3-1115G4 (tối đa 4.10 GHz, 6MB)\n- RAM: 8GB(8GBx1)DDR4 3200MHz (2 Khe, tối đa 64GB)\n- Ổ cứng: 256GB M.2 NVMe PCIe SSD\n- VGA: Intel® UHD Graphics\n- Màn hình: 14 inch FHD (1920*1080), 60Hz 45%NTSC IPS-Level\n- Pin: 3 cell , 39Whr\n- Màu sắc: Gray\n- Tính năng: Đèn nền bàn phím\n- Cân nặng: 1.3 kg\n- OS: Windows 11 Home',10,'2022-01-07',2),(13,'Z15H','Laptop MacBook Pro 14 M1 Max 2021 10-core CPU/32GB/1TB SSD/32-core GPU (Z15H)',2168,'macbook-pro-14-m1-max-2021-10-core-cpu-32gb-1tb-ssd-32-core-gpu-021221-040129-600x600.jpg','- CPU: Intel® Core™ i3-1005G1 (1.20GHz upto 3.40GHz, 4MB)\n- RAM: 4GB DDR4 on board (1 onboard + 1 khe rời)\n- Ổ cứng: 256GB PCIe NVMe SSD\n- VGA: Intel® UHD Graphics\n- Màn hình: 15.6 inch FHD (1920 x 1080), high-brightness Acer ComfyView™ LED-backlit TFT LCD\n- Pin: 2-cell, 36.7 Wh\n- Cân nặng: 1.7 kg\n- OS: Windows 10 SL',2,'2022-01-07',2),(14,'10SCXK-093VN','LAPTOP GAMING MSI GL65 LEOPARD 10SCXK 093VN I7 10750H/ 1650 4GB/ 8GB/ 512GB/ 15.6”/ FHD/ 144HZ/ IPS/ WIN 10',1052,'msi-gaming-ge66-raider-11ug-i7-258vn-600x600.jpg','- CPU: Intel core i7-10750H (2.60GHz upto 5.00 GHz, 12MB)\n- RAM: 8GB DDR4 2666Mhz\n- Ổ cứng: 512GB NVMe PCIe SSD + 1 slot 2.5\"\n- VGA: NVIDIA® GeForce® GTX 1650 4GB GDDR6\n- Màn hình: 15.6 inch FHD (1920*1080), IPS-Level 144Hz, 45%NTSC Thin Bezel\n- Cân nặng: 2.3 kg\n- Tính năng: Đèn nền bàn phím\n- OS: Windows 10 Home',12,'2022-01-07',9),(15,'A315-56-37DV','Laptop Lenovo 3 A315-56-37DV i3 1005G1/ 4GB RAM/ 256GB SSD/ 15.6 inch FHD/ Win 10/ Đen',998,'lenovo-thinkbook-14s-g2-itl-i5-1135g7-8gb-512g-600x600.jpg','- CPU: Intel® Core™ i3-1005G1 (1.20GHz upto 3.40GHz, 4MB)\n- RAM: 4GB DDR4 on board (1 onboard + 1 khe rời)\n- Ổ cứng: 256GB PCIe NVMe SSD\n- VGA: Intel® UHD Graphics\n- Màn hình: 15.6 inch FHD (1920 x 1080), high-brightness Acer ComfyView™ LED-backlit TFT LCD\n- Pin: 2-cell, 36.7 Wh\n- Cân nặng: 1.7 kg\n- OS: Windows 10 SL',20,'2022-01-07',10);
/*!40000 ALTER TABLE `core_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_profile`
--

DROP TABLE IF EXISTS `core_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `IMG` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_profile`
--

LOCK TABLES `core_profile` WRITE;
/*!40000 ALTER TABLE `core_profile` DISABLE KEYS */;
INSERT INTO `core_profile` VALUES (12,'admin','placeholder.png'),(13,'tin','placeholder.png');
/*!40000 ALTER TABLE `core_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'core','address'),(8,'core','brand'),(9,'core','cart'),(13,'core','cartdetails'),(15,'core','feedback'),(12,'core','orderdetails'),(10,'core','orders'),(11,'core','product'),(14,'core','profile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-12-18 02:32:31.771915'),(2,'auth','0001_initial','2021-12-18 02:32:32.349514'),(3,'admin','0001_initial','2021-12-18 02:32:32.551995'),(4,'admin','0002_logentry_remove_auto_add','2021-12-18 02:32:32.564501'),(5,'admin','0003_logentry_add_action_flag_choices','2021-12-18 02:32:32.581428'),(6,'contenttypes','0002_remove_content_type_name','2021-12-18 02:32:32.714410'),(7,'auth','0002_alter_permission_name_max_length','2021-12-18 02:32:32.788213'),(8,'auth','0003_alter_user_email_max_length','2021-12-18 02:32:32.814297'),(9,'auth','0004_alter_user_username_opts','2021-12-18 02:32:32.831251'),(10,'auth','0005_alter_user_last_login_null','2021-12-18 02:32:32.914007'),(11,'auth','0006_require_contenttypes_0002','2021-12-18 02:32:32.918963'),(12,'auth','0007_alter_validators_add_error_messages','2021-12-18 02:32:32.931942'),(13,'auth','0008_alter_user_username_max_length','2021-12-18 02:32:33.010732'),(14,'auth','0009_alter_user_last_name_max_length','2021-12-18 02:32:33.140640'),(15,'auth','0010_alter_group_name_max_length','2021-12-18 02:32:33.163579'),(16,'auth','0011_update_proxy_permissions','2021-12-18 02:32:33.177511'),(17,'auth','0012_alter_user_first_name_max_length','2021-12-18 02:32:33.256996'),(18,'core','0001_initial','2021-12-18 02:32:33.610362'),(19,'core','0002_auto_20211124_2108','2021-12-18 02:32:33.726320'),(20,'core','0003_auto_20211125_0812','2021-12-18 02:32:33.756244'),(21,'core','0004_auto_20211207_1913','2021-12-18 02:32:34.121216'),(22,'core','0005_address_brand_cart_cartdetails_orderdetails_orders_product','2021-12-18 02:32:34.512855'),(23,'core','0006_auto_20211208_2006','2021-12-18 02:32:34.601379'),(24,'core','0007_auto_20211211_0626','2021-12-18 02:32:34.614294'),(25,'core','0008_auto_20211211_1402','2021-12-18 02:32:34.670908'),(26,'core','0009_auto_20211213_0836','2021-12-18 02:32:34.768798'),(27,'core','0010_auto_20211214_2026','2021-12-18 02:32:34.783760'),(28,'core','0011_auto_20211215_1927','2021-12-18 02:32:34.795726'),(29,'core','0012_auto_20211217_1128','2021-12-18 02:32:34.803704'),(30,'core','0013_auto_20211218_0931','2021-12-18 02:32:34.814675'),(31,'sessions','0001_initial','2021-12-18 02:32:34.870959'),(32,'core','0013_auto_20211226_1228','2021-12-26 08:09:48.800243'),(33,'core','0014_auto_20211226_1312','2021-12-26 08:09:48.807197'),(34,'core','0015_auto_20211229_0745','2021-12-29 00:46:26.224297'),(35,'core','0016_auto_20211230_1105','2021-12-30 04:05:31.758338'),(36,'core','0017_auto_20211231_0810','2021-12-31 01:10:30.482226'),(37,'core','0018_auto_20220102_0807','2022-01-02 01:07:18.282907'),(38,'core','0019_auto_20220103_0732','2022-01-03 00:32:30.735953'),(39,'core','0015_auto_20220102_1120','2022-01-04 03:30:58.735522'),(40,'core','0016_auto_20220103_0708','2022-01-04 03:30:58.767727'),(41,'core','0020_merge_0016_auto_20220103_0708_0019_auto_20220103_0732','2022-01-04 03:30:58.771681'),(42,'core','0021_auto_20220104_1030','2022-01-04 03:30:58.778344'),(43,'core','0022_auto_20220105_0848','2022-01-05 01:48:11.660319'),(44,'core','0023_auto_20220106_2027','2022-01-06 13:27:43.899010'),(45,'core','0024_auto_20220107_1216','2022-01-07 05:16:49.895659');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('46244xrscwds2f06g5njn3vjpjo0nerv','.eJxVjDsOwjAQBe_iGln-xoaSPmewdu1dHECOFCcV4u4QKQW0b2beSyTY1pq2TkuairgILU6_G0J-UNtBuUO7zTLPbV0mlLsiD9rlOBd6Xg_376BCr9_aUTDBB2PQKO04Rsvan8mRUj4DmhDYUsGMPnP0TJYtQoTBQHSD0yDeH9JLN_4:1myPmu:iAUVlRIjZxWZC66KM_3nbM_hqFxUEBkROIxac8OZ2jk','2022-01-01 02:49:32.394049'),('8ffmttbkef86tjvip3d295ovseua2hyk','.eJxVjDsOwjAQBe_iGln-xoaSPmewdu1dHECOFCcV4u4QKQW0b2beSyTY1pq2TkuairgILU6_G0J-UNtBuUO7zTLPbV0mlLsiD9rlOBd6Xg_376BCr9_aUTDBB2PQKO04Rsvan8mRUj4DmhDYUsGMPnP0TJYtQoTBQHSD0yDeH9JLN_4:1n0PYl:-Oemh0ACxKQtzM-plMy7ainNGrzB9p6xnVXt-JP8ufg','2022-01-06 14:59:11.230020');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'tkvltw'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-07 16:10:01
