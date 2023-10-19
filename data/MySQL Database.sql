CREATE DATABASE  IF NOT EXISTS `wedding_planner` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `wedding_planner`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: wedding_planner
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `assistants`
--

DROP TABLE IF EXISTS `assistants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assistants` (
  `SNo` int NOT NULL,
  `Name` text,
  `Contact` bigint DEFAULT NULL,
  `City` text,
  `Experience` text,
  `Availability` int DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assistants`
--

LOCK TABLES `assistants` WRITE;
/*!40000 ALTER TABLE `assistants` DISABLE KEYS */;
/*!40000 ALTER TABLE `assistants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catering`
--

DROP TABLE IF EXISTS `catering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `catering` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Contact` bigint DEFAULT NULL,
  `Details` text,
  `Availability` tinyint DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Price_per_plate` bigint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catering`
--

LOCK TABLES `catering` WRITE;
/*!40000 ALTER TABLE `catering` DISABLE KEYS */;
/*!40000 ALTER TABLE `catering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dj`
--

DROP TABLE IF EXISTS `dj`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dj` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Contact` bigint DEFAULT NULL,
  `Experience` text,
  `Availability` tinyint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dj`
--

LOCK TABLES `dj` WRITE;
/*!40000 ALTER TABLE `dj` DISABLE KEYS */;
/*!40000 ALTER TABLE `dj` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entertainment`
--

DROP TABLE IF EXISTS `entertainment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entertainment` (
  `SNo` int NOT NULL,
  `Name` text,
  `Details` text,
  `City` text,
  `Cost` int DEFAULT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entertainment`
--

LOCK TABLES `entertainment` WRITE;
/*!40000 ALTER TABLE `entertainment` DISABLE KEYS */;
/*!40000 ALTER TABLE `entertainment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedbacks`
--

DROP TABLE IF EXISTS `feedbacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedbacks` (
  `Name` varchar(45) DEFAULT NULL,
  `Stars` int DEFAULT NULL,
  `Feedback` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedbacks`
--

LOCK TABLES `feedbacks` WRITE;
/*!40000 ALTER TABLE `feedbacks` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedbacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `live`
--

DROP TABLE IF EXISTS `live`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `live` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Contact` bigint DEFAULT NULL,
  `Experience` text,
  `Availability` tinyint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `live`
--

LOCK TABLES `live` WRITE;
/*!40000 ALTER TABLE `live` DISABLE KEYS */;
/*!40000 ALTER TABLE `live` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mua`
--

DROP TABLE IF EXISTS `mua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mua` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Contact` bigint DEFAULT NULL,
  `Experience` text,
  `Availability` tinyint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mua`
--

LOCK TABLES `mua` WRITE;
/*!40000 ALTER TABLE `mua` DISABLE KEYS */;
/*!40000 ALTER TABLE `mua` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `packs`
--

DROP TABLE IF EXISTS `packs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `packs` (
  `SNo` int NOT NULL,
  `Name` text,
  `Details` text,
  `City` text,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `packs`
--

LOCK TABLES `packs` WRITE;
/*!40000 ALTER TABLE `packs` DISABLE KEYS */;
/*!40000 ALTER TABLE `packs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photographer`
--

DROP TABLE IF EXISTS `photographer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photographer` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Contact` bigint DEFAULT NULL,
  `Experience` text,
  `Availability` tinyint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photographer`
--

LOCK TABLES `photographer` WRITE;
/*!40000 ALTER TABLE `photographer` DISABLE KEYS */;
/*!40000 ALTER TABLE `photographer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_data`
--

DROP TABLE IF EXISTS `user_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_data` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Username` varchar(45) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `E_Mail` varchar(30) DEFAULT NULL,
  `Booked` tinyint DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Guests` int DEFAULT NULL,
  `Pack` int DEFAULT NULL,
  `Venue` int DEFAULT NULL,
  `Caterer` int DEFAULT NULL,
  `Photographer` int DEFAULT NULL,
  `MUA` int DEFAULT NULL,
  `Live` int DEFAULT NULL,
  `DJ` int DEFAULT NULL,
  `Entertainment` int DEFAULT NULL,
  `EstimatedTotal` int DEFAULT '0',
  `Paid` int DEFAULT '0',
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`),
  UNIQUE KEY `Username_UNIQUE` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_data`
--

LOCK TABLES `user_data` WRITE;
/*!40000 ALTER TABLE `user_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venue`
--

DROP TABLE IF EXISTS `venue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venue` (
  `SNo` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `City` text,
  `Address` text,
  `Type` text,
  `Rating` int DEFAULT NULL,
  `Size` text,
  `Availability` tinyint DEFAULT NULL,
  `Price_per_Plate` bigint DEFAULT NULL,
  `Cost` bigint DEFAULT NULL,
  PRIMARY KEY (`SNo`),
  UNIQUE KEY `SNo_UNIQUE` (`SNo`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venue`
--

LOCK TABLES `venue` WRITE;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
/*!40000 ALTER TABLE `venue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-20 15:38:25
