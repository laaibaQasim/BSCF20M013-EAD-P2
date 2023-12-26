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
-- Table structure for table `user_activity`
--

DROP TABLE IF EXISTS `user_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `action` varchar(50) DEFAULT NULL,
  `details` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_activity_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=605 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_activity`
--

LOCK TABLES `user_activity` WRITE;
/*!40000 ALTER TABLE `user_activity` DISABLE KEYS */;
INSERT INTO `user_activity` VALUES (400,5,'VIEW','Viewing interests','2023-12-25 18:00:03','2023-12-25 18:00:03'),(401,5,'VIEW','Viewing interests','2023-12-25 18:00:11','2023-12-25 18:00:11'),(402,5,'VIEW','Viewing interests','2023-12-25 18:00:30','2023-12-25 18:00:30'),(403,5,'VIEW','Viewing interests','2023-12-25 18:00:34','2023-12-25 18:00:34'),(404,5,'VIEW','Viewing interests','2023-12-25 18:00:55','2023-12-25 18:00:55'),(405,5,'VIEW','Viewing interests','2023-12-25 18:00:58','2023-12-25 18:00:58'),(406,5,'VIEW','Viewing interests','2023-12-25 18:01:11','2023-12-25 18:01:11'),(407,5,'VIEW','Viewing interests','2023-12-25 18:01:13','2023-12-25 18:01:13'),(408,5,'VIEW','Viewing interests','2023-12-25 18:01:22','2023-12-25 18:01:22'),(409,5,'VIEW','Viewing interests','2023-12-25 18:01:25','2023-12-25 18:01:25'),(410,5,'VIEW','Viewing interests','2023-12-25 18:01:38','2023-12-25 18:01:38'),(411,5,'VIEW','Viewing interests','2023-12-25 18:01:41','2023-12-25 18:01:41'),(412,5,'VIEW','Viewing interests','2023-12-25 18:01:53','2023-12-25 18:01:53'),(413,5,'VIEW','Viewing interests','2023-12-25 18:01:56','2023-12-25 18:01:56'),(414,5,'VIEW','Viewing interests','2023-12-25 18:07:42','2023-12-25 18:07:42'),(415,5,'VIEW','Viewing interests','2023-12-25 18:07:48','2023-12-25 18:07:48'),(416,5,'VIEW','Viewing interests','2023-12-25 18:08:39','2023-12-25 18:08:39'),(417,5,'VIEW','Viewing interests','2023-12-25 18:08:41','2023-12-25 18:08:41'),(418,5,'VIEW','Viewing interests','2023-12-25 18:08:49','2023-12-25 18:08:49'),(419,5,'VIEW','Viewing interests','2023-12-25 18:08:52','2023-12-25 18:08:52'),(420,5,'VIEW','Viewing interests','2023-12-25 18:11:39','2023-12-25 18:11:39'),(421,5,'VIEW','Viewing interests','2023-12-25 18:11:42','2023-12-25 18:11:42'),(422,5,'VIEW','Viewing interests','2023-12-25 18:12:08','2023-12-25 18:12:08'),(423,5,'VIEW','Viewing interests','2023-12-25 18:13:50','2023-12-25 18:13:50'),(424,5,'VIEW','Viewing interests','2023-12-25 18:13:55','2023-12-25 18:13:55'),(425,5,'VIEW','Viewing interests','2023-12-25 18:18:23','2023-12-25 18:18:23'),(426,5,'VIEW','Viewing interests','2023-12-25 18:18:30','2023-12-25 18:18:30'),(427,5,'VIEW','Viewing interests','2023-12-25 18:18:59','2023-12-25 18:18:59'),(428,5,'VIEW','Viewing interests','2023-12-25 18:19:05','2023-12-25 18:19:05'),(429,5,'VIEW','Viewing interests','2023-12-25 18:19:09','2023-12-25 18:19:09'),(430,5,'VIEW','Viewing interests','2023-12-25 18:19:42','2023-12-25 18:19:42'),(431,1,'VIEW','Viewing interests','2023-12-26 04:31:48','2023-12-26 04:31:48'),(432,1,'VIEW','Viewing user with email: l','2023-12-26 04:32:03','2023-12-26 04:32:03'),(433,1,'VIEW','Viewing interests','2023-12-26 04:34:03','2023-12-26 04:34:03'),(434,1,'VIEW','Viewing departments','2023-12-26 04:34:03','2023-12-26 04:34:03'),(435,1,'VIEW','Viewing student with ID: 1','2023-12-26 04:34:03','2023-12-26 04:34:03'),(436,1,'VIEW','Viewing interests','2023-12-26 04:34:50','2023-12-26 04:34:50'),(437,1,'VIEW','Viewing departments','2023-12-26 04:34:50','2023-12-26 04:34:50'),(438,1,'VIEW','Viewing student with ID: 1','2023-12-26 04:34:50','2023-12-26 04:34:50'),(439,1,'VIEW','Viewing interests','2023-12-26 04:35:36','2023-12-26 04:35:36'),(440,1,'VIEW','Viewing departments','2023-12-26 04:35:36','2023-12-26 04:35:36'),(441,1,'VIEW','Viewing student with ID: 1','2023-12-26 04:35:36','2023-12-26 04:35:36'),(442,1,'VIEW','Viewing interests','2023-12-26 04:35:50','2023-12-26 04:35:50'),(443,1,'VIEW','Viewing departments','2023-12-26 04:35:50','2023-12-26 04:35:50'),(444,1,'VIEW','Viewing student with ID: 1','2023-12-26 04:35:51','2023-12-26 04:35:51'),(445,1,'VIEW','Viewing student with ID: 1','2023-12-26 04:36:38','2023-12-26 04:36:38'),(446,1,'VIEW','Viewing interests','2023-12-26 04:36:46','2023-12-26 04:36:46'),(447,1,'VIEW','Viewing interests','2023-12-26 04:42:11','2023-12-26 04:42:11'),(448,1,'VIEW','Viewing interests','2023-12-26 04:42:11','2023-12-26 04:42:11'),(449,1,'VIEW','Viewing interests','2023-12-26 04:42:50','2023-12-26 04:42:50'),(450,1,'VIEW','Viewing interests','2023-12-26 04:42:51','2023-12-26 04:42:51'),(451,1,'VIEW','Viewing interests','2023-12-26 04:42:59','2023-12-26 04:42:59'),(452,1,'VIEW','Viewing interests','2023-12-26 04:43:00','2023-12-26 04:43:00'),(453,1,'VIEW','Viewing interests','2023-12-26 04:43:29','2023-12-26 04:43:29'),(454,1,'VIEW','Viewing interests','2023-12-26 04:43:30','2023-12-26 04:43:30'),(455,1,'VIEW','Viewing interests','2023-12-26 04:43:32','2023-12-26 04:43:32'),(456,1,'LOGIN','User logged into the system','2023-12-26 08:01:24','2023-12-26 08:01:24'),(457,1,'NAVIGATE','User naviagted to /studentList','2023-12-26 08:01:24','2023-12-26 08:01:24'),(458,1,'VIEW','Viewing interests','2023-12-26 08:01:47','2023-12-26 08:01:47'),(459,1,'VIEW','Viewing departments','2023-12-26 08:01:47','2023-12-26 08:01:47'),(460,1,'VIEW','Viewing student with ID: 5','2023-12-26 08:01:47','2023-12-26 08:01:47'),(461,1,'UPDATE','Updating user 5','2023-12-26 08:01:53','2023-12-26 08:01:53'),(462,1,'UPDATE','Updating student 5','2023-12-26 08:01:53','2023-12-26 08:01:53'),(463,1,'NAVIGATE','User naviagted to /login','2023-12-26 09:14:33','2023-12-26 09:14:33'),(464,1,'VIEW','Viewing user with email: l','2023-12-26 09:31:56','2023-12-26 09:31:56'),(465,1,'LOGIN','User logged into the system','2023-12-26 09:31:57','2023-12-26 09:31:57'),(466,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 09:31:57','2023-12-26 09:31:57'),(467,1,'SORT','user set user.name for sorting','2023-12-26 09:32:04','2023-12-26 09:32:04'),(468,1,'SORT DIRECTION','user changed sort direction','2023-12-26 09:32:07','2023-12-26 09:32:07'),(469,1,'ENTER','User changed page size','2023-12-26 09:32:31','2023-12-26 09:32:31'),(470,1,'BUTTON CLICK','user clicked on undefined button on page navigator','2023-12-26 09:32:31','2023-12-26 09:32:31'),(471,1,'VIEW','Viewing student with ID: 22','2023-12-26 09:35:07','2023-12-26 09:35:07'),(472,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 09:35:09','2023-12-26 09:35:09'),(473,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 09:35:10','2023-12-26 09:35:10'),(474,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 09:35:10','2023-12-26 09:35:10'),(475,1,'VIEW','Viewing interests','2023-12-26 09:35:10','2023-12-26 09:35:10'),(476,1,'VIEW','Viewing departments','2023-12-26 09:35:10','2023-12-26 09:35:10'),(477,1,'VIEW','Viewing student with ID: 1','2023-12-26 09:35:10','2023-12-26 09:35:10'),(478,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 09:35:13','2023-12-26 09:35:13'),(479,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 09:35:19','2023-12-26 09:35:19'),(480,1,'VIEW','Viewing interests','2023-12-26 09:35:20','2023-12-26 09:35:20'),(481,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 09:35:31','2023-12-26 09:35:31'),(482,1,'LOGIN','User logged into the system','2023-12-26 09:39:22','2023-12-26 09:39:22'),(483,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 09:39:22','2023-12-26 09:39:22'),(484,1,'LOGIN','User logged into the system','2023-12-26 10:02:10','2023-12-26 10:02:10'),(485,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:02:10','2023-12-26 10:02:10'),(486,1,'LOGOUT','User logged out of the system','2023-12-26 10:02:14','2023-12-26 10:02:14'),(487,1,'LOGIN','User logged into the system','2023-12-26 10:02:23','2023-12-26 10:02:23'),(488,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:02:23','2023-12-26 10:02:23'),(489,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 10:02:26','2023-12-26 10:02:26'),(490,1,'VIEW','Viewing interests','2023-12-26 10:02:27','2023-12-26 10:02:27'),(491,1,'LOGOUT','User logged out of the system','2023-12-26 10:02:28','2023-12-26 10:02:28'),(492,1,'LOGIN','User logged into the system','2023-12-26 10:02:50','2023-12-26 10:02:50'),(493,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:02:50','2023-12-26 10:02:50'),(494,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:04:32','2023-12-26 10:04:32'),(495,1,'BUTTON CLICK','user clicked on next button on page navigator','2023-12-26 10:04:40','2023-12-26 10:04:40'),(496,1,'BUTTON CLICK','user clicked on next button on page navigator','2023-12-26 10:04:41','2023-12-26 10:04:41'),(497,1,'BUTTON CLICK','user clicked on prev button on page navigator','2023-12-26 10:04:44','2023-12-26 10:04:44'),(498,1,'BUTTON CLICK','user clicked on last button on page navigator','2023-12-26 10:04:47','2023-12-26 10:04:47'),(499,1,'ENTER','User changed page size','2023-12-26 10:05:05','2023-12-26 10:05:05'),(500,1,'SORT DIRECTION','user changed sort direction','2023-12-26 10:05:25','2023-12-26 10:05:25'),(501,1,'SORT','user set department.name for sorting','2023-12-26 10:05:25','2023-12-26 10:05:25'),(502,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:53:00','2023-12-26 10:53:00'),(503,1,'VIEW','Viewing user with email: l','2023-12-26 10:59:52','2023-12-26 10:59:52'),(504,1,'LOGIN','User logged into the system','2023-12-26 10:59:52','2023-12-26 10:59:52'),(505,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 10:59:52','2023-12-26 10:59:52'),(506,1,'ENTER','User changed page size','2023-12-26 10:59:57','2023-12-26 10:59:57'),(507,1,'ENTER','User changed page size','2023-12-26 10:59:58','2023-12-26 10:59:58'),(508,1,'ENTER','User changed page size','2023-12-26 10:59:58','2023-12-26 10:59:58'),(509,1,'ENTER','User changed page size','2023-12-26 11:03:17','2023-12-26 11:03:17'),(510,1,'VIEW','Viewing student with ID: 1','2023-12-26 11:15:07','2023-12-26 11:15:07'),(511,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:16:58','2023-12-26 11:16:58'),(512,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 11:17:02','2023-12-26 11:17:02'),(513,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 11:17:02','2023-12-26 11:17:02'),(514,1,'VIEW','Viewing interests','2023-12-26 11:17:02','2023-12-26 11:17:02'),(515,1,'VIEW','Viewing departments','2023-12-26 11:17:02','2023-12-26 11:17:02'),(516,1,'VIEW','Viewing student with ID: 1','2023-12-26 11:17:02','2023-12-26 11:17:02'),(517,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:17:07','2023-12-26 11:17:07'),(518,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 11:17:17','2023-12-26 11:17:17'),(519,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 11:17:17','2023-12-26 11:17:17'),(520,1,'VIEW','Viewing interests','2023-12-26 11:17:17','2023-12-26 11:17:17'),(521,1,'VIEW','Viewing departments','2023-12-26 11:17:17','2023-12-26 11:17:17'),(522,1,'VIEW','Viewing student with ID: 11','2023-12-26 11:17:17','2023-12-26 11:17:17'),(523,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:29:14','2023-12-26 11:29:14'),(524,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 11:31:06','2023-12-26 11:31:06'),(525,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 11:31:06','2023-12-26 11:31:06'),(526,1,'VIEW','Viewing interests','2023-12-26 11:31:06','2023-12-26 11:31:06'),(527,1,'VIEW','Viewing departments','2023-12-26 11:31:06','2023-12-26 11:31:06'),(528,1,'VIEW','Viewing student with ID: 1','2023-12-26 11:31:06','2023-12-26 11:31:06'),(529,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:31:12','2023-12-26 11:31:12'),(530,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 11:31:21','2023-12-26 11:31:21'),(531,1,'VIEW','Viewing interests','2023-12-26 11:31:21','2023-12-26 11:31:21'),(532,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 11:32:01','2023-12-26 11:32:01'),(533,1,'VIEW','Viewing interests','2023-12-26 11:32:02','2023-12-26 11:32:02'),(534,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 11:40:51','2023-12-26 11:40:51'),(535,1,'VIEW','Viewing interests','2023-12-26 11:40:52','2023-12-26 11:40:52'),(536,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 11:40:57','2023-12-26 11:40:57'),(537,1,'VIEW','Viewing interests','2023-12-26 11:40:58','2023-12-26 11:40:58'),(538,5,'LOGIN','User logged into the system','2023-12-26 11:59:15','2023-12-26 11:59:15'),(539,5,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:59:16','2023-12-26 11:59:16'),(540,5,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 11:59:17','2023-12-26 11:59:17'),(541,5,'VIEW','Viewing interests','2023-12-26 11:59:17','2023-12-26 11:59:17'),(542,5,'VIEW','Viewing departments','2023-12-26 11:59:17','2023-12-26 11:59:17'),(543,5,'NAVIGATE','User nagiated to /studentList','2023-12-26 11:59:20','2023-12-26 11:59:20'),(544,5,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:03:07','2023-12-26 12:03:07'),(545,5,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:03:20','2023-12-26 12:03:20'),(546,5,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:03:54','2023-12-26 12:03:54'),(547,5,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:05:31','2023-12-26 12:05:31'),(548,5,'VIEW','Viewing interests','2023-12-26 12:05:31','2023-12-26 12:05:31'),(549,5,'LOGOUT','User logged out of the system','2023-12-26 12:05:35','2023-12-26 12:05:35'),(550,1,'LOGIN','User logged into the system','2023-12-26 12:05:38','2023-12-26 12:05:38'),(551,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:05:38','2023-12-26 12:05:38'),(552,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 12:05:41','2023-12-26 12:05:41'),(553,1,'VIEW','Viewing interests','2023-12-26 12:05:42','2023-12-26 12:05:42'),(554,1,'VIEW','Viewing departments','2023-12-26 12:05:42','2023-12-26 12:05:42'),(555,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:05:43','2023-12-26 12:05:43'),(556,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 12:08:54','2023-12-26 12:08:54'),(557,1,'VIEW','Viewing interests','2023-12-26 12:08:54','2023-12-26 12:08:54'),(558,1,'VIEW','Viewing departments','2023-12-26 12:08:54','2023-12-26 12:08:54'),(559,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:09:01','2023-12-26 12:09:01'),(560,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 12:09:10','2023-12-26 12:09:10'),(561,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 12:09:10','2023-12-26 12:09:10'),(562,1,'VIEW','Viewing interests','2023-12-26 12:09:10','2023-12-26 12:09:10'),(563,1,'VIEW','Viewing departments','2023-12-26 12:09:10','2023-12-26 12:09:10'),(564,1,'VIEW','Viewing student with ID: 1','2023-12-26 12:09:10','2023-12-26 12:09:10'),(565,1,'UPDATE','Updating user 1','2023-12-26 12:09:13','2023-12-26 12:09:13'),(566,1,'UPDATE','Updating student 1','2023-12-26 12:09:14','2023-12-26 12:09:14'),(567,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:09:14','2023-12-26 12:09:14'),(568,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 12:41:26','2023-12-26 12:41:26'),(569,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:43:55','2023-12-26 12:43:55'),(570,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:43:56','2023-12-26 12:43:56'),(571,1,'VIEW','Viewing interests','2023-12-26 12:43:56','2023-12-26 12:43:56'),(572,1,'VIEW','Viewing interests','2023-12-26 12:43:57','2023-12-26 12:43:57'),(573,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:44:17','2023-12-26 12:44:17'),(574,1,'VIEW','Viewing interests','2023-12-26 12:44:18','2023-12-26 12:44:18'),(575,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:44:18','2023-12-26 12:44:18'),(576,1,'VIEW','Viewing interests','2023-12-26 12:44:19','2023-12-26 12:44:19'),(577,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:45:02','2023-12-26 12:45:02'),(578,1,'VIEW','Viewing interests','2023-12-26 12:45:03','2023-12-26 12:45:03'),(579,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:45:06','2023-12-26 12:45:06'),(580,1,'VIEW','Viewing interests','2023-12-26 12:45:07','2023-12-26 12:45:07'),(581,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:45:23','2023-12-26 12:45:23'),(582,1,'VIEW','Viewing interests','2023-12-26 12:45:24','2023-12-26 12:45:24'),(583,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 12:47:03','2023-12-26 12:47:03'),(584,1,'VIEW','Viewing interests','2023-12-26 12:47:04','2023-12-26 12:47:04'),(585,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 13:34:56','2023-12-26 13:34:56'),(586,1,'VIEW','Viewing interests','2023-12-26 13:34:57','2023-12-26 13:34:57'),(587,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 13:52:28','2023-12-26 13:52:28'),(588,1,'ENTER','User changed page size','2023-12-26 13:52:31','2023-12-26 13:52:31'),(589,1,'ENTER','User changed page size','2023-12-26 13:52:32','2023-12-26 13:52:32'),(590,1,'ENTER','User changed page size','2023-12-26 13:52:32','2023-12-26 13:52:32'),(591,1,'BUTTON CLICK','user clicked on next button on page navigator','2023-12-26 13:57:48','2023-12-26 13:57:48'),(592,1,'BUTTON CLICK','user clicked on next button on page navigator','2023-12-26 13:57:53','2023-12-26 13:57:53'),(593,1,'VIEW','Viewing student with ID: 20','2023-12-26 14:00:24','2023-12-26 14:00:24'),(594,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 14:01:47','2023-12-26 14:01:47'),(595,1,'NAVIAGTE','User navigated to /studentList/update','2023-12-26 14:01:48','2023-12-26 14:01:48'),(596,1,'NAVIGATE','User nagiated to /studentList/view','2023-12-26 14:01:48','2023-12-26 14:01:48'),(597,1,'VIEW','Viewing interests','2023-12-26 14:01:48','2023-12-26 14:01:48'),(598,1,'VIEW','Viewing departments','2023-12-26 14:01:48','2023-12-26 14:01:48'),(599,1,'VIEW','Viewing student with ID: 5','2023-12-26 14:01:48','2023-12-26 14:01:48'),(600,1,'NAVIGATE','User nagiated to /studentList','2023-12-26 14:02:58','2023-12-26 14:02:58'),(601,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 14:03:01','2023-12-26 14:03:01'),(602,1,'VIEW','Viewing interests','2023-12-26 14:03:02','2023-12-26 14:03:02'),(603,1,'NAVIGATE','User nagiated to /dashboard','2023-12-26 14:07:18','2023-12-26 14:07:18'),(604,1,'VIEW','Viewing interests','2023-12-26 14:07:19','2023-12-26 14:07:19');
/*!40000 ALTER TABLE `user_activity` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-26 19:27:38
