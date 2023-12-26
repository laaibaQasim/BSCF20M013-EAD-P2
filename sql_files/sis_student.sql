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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `department_id` int DEFAULT NULL,
  `interest_id` int DEFAULT NULL,
  `roll_number` varchar(20) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `degree` varchar(50) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roll_number` (`roll_number`),
  KEY `department_id` (`department_id`),
  KEY `interest_id` (`interest_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`),
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`),
  CONSTRAINT `student_ibfk_3` FOREIGN KEY (`interest_id`) REFERENCES `interest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,3,8,'R4186','Quetta','Male','2004-06-13','Bachelors','2021-02-19','2024-10-07','2023-12-24 07:20:56','2023-12-26 12:09:14'),(5,2,10,'R2718','Lahore','Male','2004-05-25','Bachelors','2019-06-24','2020-11-01','2023-12-19 11:00:00','2023-12-26 08:01:53'),(6,1,8,'R8789','Lahore','Male','2004-04-13','Doctorate','2019-12-19','2020-11-01','2023-12-20 10:00:00','2023-12-24 07:20:56'),(7,1,12,'R4905','Lahore','Female','2002-04-11','Masters','2022-12-01','2020-11-01','2023-12-21 01:00:00','2023-12-24 07:20:56'),(8,4,11,'R3541','Lahore','Female','2004-10-17','Doctorate','2021-11-10','2020-11-01','2023-12-21 01:00:00','2023-12-24 07:20:56'),(9,4,7,'R1904','Lahore','Male','2005-04-25','Masters','2020-07-17','2020-11-01','2023-12-21 01:00:00','2023-12-24 07:20:56'),(11,3,10,'R9502','Lahore','Female','2005-05-05','Masters','2022-04-19','2024-01-28','2023-12-21 01:00:00','2023-12-24 07:20:56'),(12,2,2,'R8891','Lahore','Female','2002-03-22','Bachelors','2023-11-28','2024-01-28','2023-12-24 07:20:56','2023-12-24 07:20:56'),(13,2,12,'R7374','Lahore','Male','2003-01-27','Doctorate','2023-11-28','2024-01-28','2023-12-24 07:20:56','2023-12-24 07:20:56'),(14,2,4,'R4523','Lahore','Male','2002-03-25','Doctorate','2022-01-08','2024-10-02','2023-12-24 07:20:56','2023-12-24 07:20:56'),(15,3,1,'R4984','Faislabad','Female','2002-12-23','Bachelors','2019-05-14','2024-10-11','2023-12-24 07:20:56','2023-12-24 07:20:56'),(16,3,10,'R4402','Islamabad','Female','2005-02-15','Bachelors','2020-06-26','2024-07-09','2023-12-24 07:20:56','2023-12-24 07:20:56'),(17,3,3,'R2157','Islamabad','Female','2002-03-06','Masters','2021-03-03','2024-12-03','2023-12-24 07:20:56','2023-12-24 07:20:56'),(18,2,7,'R4412','Islamabad','Female','2005-02-14','Bachelors','2021-11-10','2024-11-02','2023-12-24 07:20:56','2023-12-24 07:20:56'),(19,1,10,'R7686','Islamabad','Female','2002-10-11','Bachelors','2022-09-16','2024-08-29','2023-12-24 07:20:56','2023-12-24 07:20:56'),(20,4,11,'R8350','Karachi','Male','2004-10-21','Masters','2020-02-28','2024-07-26','2023-12-24 07:20:57','2023-12-24 07:20:57'),(21,3,5,'R6515','Karachi','Female','2003-02-21','Masters','2021-11-20','2024-12-08','2023-12-24 07:20:57','2023-12-24 07:20:57'),(22,2,8,'R2767','Karachi','Female','2003-12-26','Bachelors','2022-12-17','2024-10-22','2023-12-24 07:20:57','2023-12-24 07:20:57'),(23,5,2,'R4267','Karachi','Female','2003-05-02','Bachelors','2022-05-29','2024-11-27','2023-12-24 07:20:57','2023-12-24 07:20:57'),(24,5,10,'R5406','Karachi','Male','2003-09-06','Masters','2021-10-10','2024-11-24','2023-12-24 07:20:57','2023-12-24 07:20:57'),(25,1,12,'R1970','Karachi','Male','2004-07-21','Bachelors','2021-12-07','2024-09-12','2023-12-24 07:20:57','2023-12-24 07:20:57');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
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
