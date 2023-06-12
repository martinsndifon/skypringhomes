-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: sky_dev_db
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('edce7c3f-0747-48ad-9107-de0c829ab168','2023-05-31 19:42:49','2023-05-31 19:42:49','martins ndifon','martinsndifon@gmail.com','sha256$a3sU2zYAiiWBmkRO$ed928f9cbffb060efe8ded87fd617b17c61c9ffaec82a6331adb49559d383055');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rent`
--

DROP TABLE IF EXISTS `rent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rent` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(60) NOT NULL,
  `rent_type` varchar(60) NOT NULL,
  `price` int DEFAULT '0',
  `description` varchar(1500) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `image_path` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rent_type` (`rent_type`),
  CONSTRAINT `rent_ibfk_1` FOREIGN KEY (`rent_type`) REFERENCES `renttype` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rent`
--

LOCK TABLES `rent` WRITE;
/*!40000 ALTER TABLE `rent` DISABLE KEYS */;
INSERT INTO `rent` VALUES ('0a8aaab6-f569-40a1-be17-29755dc51383','2023-06-08 23:02:12','2023-06-08 23:02:12','One room, one office','2-bedroom',900000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Dawaki, Abuja','/static/media_storage/rent/2-bedroom/images/0a8aaab6-f569-40a1-be17-29755dc51383/'),('162de57c-6184-4d4d-ba26-2e32a242a547','2023-06-08 23:06:36','2023-06-08 23:06:36','A 4 bedroom duplex','4-bedroom',4600000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Katampe, Abuja','/static/media_storage/rent/4-bedroom/images/162de57c-6184-4d4d-ba26-2e32a242a547/'),('707a6cb3-4601-40c5-ac92-e180c2a73762','2023-06-08 22:57:45','2023-06-08 22:57:45','For a small family','3-bedroom',1000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Lugbe, Abuja','/static/media_storage/rent/3-bedroom/images/707a6cb3-4601-40c5-ac92-e180c2a73762/'),('755db348-fc6d-4ce2-bb6e-8d7be95b2b3b','2023-06-08 22:48:00','2023-06-08 22:48:00','A family house','4-bedroom',3000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Gwarinpa, Abuja','/static/media_storage/rent/4-bedroom/images/755db348-fc6d-4ce2-bb6e-8d7be95b2b3b/'),('b0fa6e3c-cd9c-47af-9b13-baeee6f4f36a','2023-06-08 22:49:09','2023-06-08 22:49:09','Single room for students','self-contain',275000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Karu, Abuja','/static/media_storage/rent/self-contain/images/b0fa6e3c-cd9c-47af-9b13-baeee6f4f36a/'),('b6f87713-96a5-4016-b866-2fcdb0d4fb12','2023-06-08 22:54:05','2023-06-08 22:54:05','A bachelor\'s abode','1-bedroom',750000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Life camp, Abuja','/static/media_storage/rent/1-bedroom/images/b6f87713-96a5-4016-b866-2fcdb0d4fb12/'),('b734b96c-b0d9-4615-9c1e-e7cfe2a27773','2023-06-08 22:46:29','2023-06-08 22:46:29','A 5 bedroom condo','5-bedroom',4000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Katampe, FCT-Abuja','/static/media_storage/rent/5-bedroom/images/b734b96c-b0d9-4615-9c1e-e7cfe2a27773/'),('fc2b718f-754e-44f2-abc3-3337f0c10e14','2023-06-08 22:59:10','2023-06-08 22:59:10','Perfect for 2 friends','2-bedroom',800000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Jahi, Abuja','/static/media_storage/rent/2-bedroom/images/fc2b718f-754e-44f2-abc3-3337f0c10e14/');
/*!40000 ALTER TABLE `rent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renttype`
--

DROP TABLE IF EXISTS `renttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renttype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renttype`
--

LOCK TABLES `renttype` WRITE;
/*!40000 ALTER TABLE `renttype` DISABLE KEYS */;
INSERT INTO `renttype` VALUES (2,'1-bedroom'),(3,'2-bedroom'),(4,'3-bedroom'),(5,'4-bedroom'),(6,'5-bedroom'),(1,'self-contain');
/*!40000 ALTER TABLE `renttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(60) NOT NULL,
  `price` int DEFAULT '0',
  `description` varchar(1500) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `image_path` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES ('3c089c3c-f64a-4488-9d9d-ad92515b8167','2023-06-08 23:18:00','2023-06-08 23:19:37','A nice 4 bedroom condo',120000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Katampe, Abuja','/static/media_storage/sale/images/3c089c3c-f64a-4488-9d9d-ad92515b8167/'),('6db6fd04-3985-4496-9abb-709b95c55cf0','2023-06-08 23:31:23','2023-06-08 23:31:23','A beauty to behold',450000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Central Area, Abuja','/static/media_storage/sale/images/6db6fd04-3985-4496-9abb-709b95c55cf0/'),('75862fd8-2a11-4750-8e47-67b57479ad15','2023-06-08 23:26:57','2023-06-08 23:27:36','Newly built 3 bedroom',90000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Asokoro, Abuja','/static/media_storage/sale/images/75862fd8-2a11-4750-8e47-67b57479ad15/'),('bd5ad366-9d2a-49b5-be14-0d2b8ddf4344','2023-06-08 23:21:50','2023-06-08 23:21:50','Beautifully finished home',105000000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Guzape, Abuja','/static/media_storage/sale/images/bd5ad366-9d2a-49b5-be14-0d2b8ddf4344/');
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serviced`
--

DROP TABLE IF EXISTS `serviced`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serviced` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(60) NOT NULL,
  `price` int DEFAULT '0',
  `description` varchar(1500) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `image_path` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serviced`
--

LOCK TABLES `serviced` WRITE;
/*!40000 ALTER TABLE `serviced` DISABLE KEYS */;
INSERT INTO `serviced` VALUES ('5a707a07-98e4-4c06-a563-d0d1d9520d93','2023-06-08 23:11:39','2023-06-08 23:11:39','Luxurious apartment',170000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Wuse, Abuja','/static/media_storage/serviced/images/5a707a07-98e4-4c06-a563-d0d1d9520d93/'),('6304bd8e-7a61-4305-bb56-c1ac59447095','2023-06-08 23:09:07','2023-06-08 23:09:07','Luxury at its finest',130000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Garki, Abuja','/static/media_storage/serviced/images/6304bd8e-7a61-4305-bb56-c1ac59447095/'),('9a43529a-bf82-4c4c-b41a-94c4324a14c6','2023-06-08 23:25:19','2023-06-08 23:25:19','Highly accessible',210000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Wuse 2, Abuja','/static/media_storage/serviced/images/9a43529a-bf82-4c4c-b41a-94c4324a14c6/'),('a99c8928-9222-47da-926e-b9b2d79dc9fe','2023-06-08 23:29:33','2023-06-08 23:29:33','Secret location',250000,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo rem et corporis placeat veritatis pariatur ullam officia quaerat, neque fugit, a animi perspiciatis provident odit asperiores? Sunt qui magni labore dicta commodi ipsum voluptates, quam magnam architecto pariatur perspiciatis est recusandae illum at veritatis iure porro numquam! Autem, ipsam numquam?','Available on request','/static/media_storage/serviced/images/a99c8928-9222-47da-926e-b9b2d79dc9fe/');
/*!40000 ALTER TABLE `serviced` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-12 14:28:23
