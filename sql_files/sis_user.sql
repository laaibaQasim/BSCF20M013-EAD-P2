-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sis
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(126) DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('laiba','l','admin',1,1,'2023-12-24 07:20:55','2023-12-26 12:09:14'),('ayesha','a','pucit',2,2,'2023-12-24 07:20:55','2023-12-25 08:08:02'),('User 9640','user6273@example.com','pucit',2,3,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4042','user6690@example.com','pucit',2,4,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4863','user7865@example.com','pucit',2,5,'2023-12-24 07:20:55','2023-12-26 08:01:53'),('User 5402','user5820@example.com','pucit',2,6,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7304','user5843@example.com','pucit',2,7,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 3096','user1979@example.com','pucit',2,8,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 3281','user4478@example.com','pucit',2,9,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 5120','user4352@example.com','pucit',2,10,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 2813','user5903@example.com','pucit',2,11,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7494','user6285@example.com','pucit',2,12,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4737','user3330@example.com','pucit',2,13,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7308','user1304@example.com','pucit',2,14,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7995','user8364@example.com','pucit',2,15,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4275','user2090@example.com','pucit',2,16,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 8960','user3983@example.com','pucit',2,17,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 8646','user3875@example.com','pucit',2,18,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 2272','user2589@example.com','pucit',2,19,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4551','user1744@example.com','pucit',2,20,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 4354','user7757@example.com','pucit',2,21,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 9708','user9887@example.com','pucit',2,22,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7878','user2166@example.com','pucit',2,23,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 3865','user9105@example.com','pucit',2,24,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 6960','user6487@example.com','pucit',2,25,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 7642','user7883@example.com','pucit',2,26,'2023-12-24 07:20:55','2023-12-24 07:20:55'),('User 3465','User35@gmail.com','pucit',2,27,'2023-12-24 13:36:20','2023-12-24 13:36:20'),('User 4532','Usr344@gmail.com','pucit',2,28,'2023-12-24 13:38:58','2023-12-24 13:38:58'),('zaroon','z','pucit',2,29,'2023-12-25 08:33:49','2023-12-25 08:33:49'),('zaroon','zaroon@gmail.com','pucit',2,30,'2023-12-25 08:34:08','2023-12-25 08:34:08');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-26 19:27:37
