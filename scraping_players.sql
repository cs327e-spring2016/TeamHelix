-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: scraping
-- ------------------------------------------------------
-- Server version	5.7.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `players` (
  `player_id` int(2) NOT NULL AUTO_INCREMENT,
  `player_name` varchar(20) NOT NULL,
  `TK` int(6) NOT NULL,
  `HS` float NOT NULL,
  `TD` int(6) NOT NULL,
  `KD` float NOT NULL,
  `matches` int(5) NOT NULL,
  `rounds` int(10) NOT NULL,
  `AKR` float NOT NULL,
  `AAR` float NOT NULL,
  `ADR` float NOT NULL,
  PRIMARY KEY (`player_id`),
  UNIQUE KEY `player_name` (`player_name`),
  UNIQUE KEY `player_name_2` (`player_name`)
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (152,'xantares',4255,53.8,3250,1.31,182,4671,0.91,0.18,0.7),(153,'get_right',18756,49.1,14096,1.33,919,23166,0.81,0.15,0.61),(154,'fancy1',2511,48.8,1880,1.34,124,3080,0.82,0.16,0.61),(155,'coldzera',5320,45.8,4135,1.29,253,6565,0.81,0.13,0.63),(156,'mo',2355,40,1910,1.23,115,2869,0.82,0.15,0.67),(157,'f0rest',18072,50.1,14295,1.26,896,22501,0.8,0.13,0.64),(158,'s1mple',9089,40.7,7578,1.2,409,10765,0.84,0.11,0.7),(159,'niko',7854,50.2,6581,1.19,354,9430,0.83,0.15,0.7),(160,'fxy0',2592,28.6,2072,1.25,126,3212,0.81,0.12,0.65),(161,'kennys',16320,31.2,12934,1.26,793,20678,0.79,0.12,0.63),(162,'guardian',15574,30.2,12334,1.26,755,19845,0.78,0.12,0.62),(163,'mixwell',2309,40,1873,1.23,112,2862,0.81,0.15,0.65),(164,'device',13496,37.2,10881,1.24,668,17164,0.79,0.14,0.63),(165,'oskar',6658,34.7,5522,1.21,318,8306,0.8,0.12,0.66),(166,'dd',2289,44,1836,1.25,118,2939,0.78,0.17,0.62),(167,'dream3r',7562,49.8,6031,1.25,383,9833,0.77,0.13,0.61),(168,'attacker',2424,42.9,1973,1.23,123,3023,0.8,0.15,0.65),(169,'zelin',2268,47.7,1869,1.21,106,2855,0.79,0.15,0.65),(170,'olofmeister',13398,42.7,11066,1.21,669,17232,0.78,0.15,0.64),(171,'fer',6232,42.7,5328,1.17,301,7828,0.8,0.17,0.68),(172,'magiskb0y',3244,46,2707,1.2,161,4212,0.77,0.15,0.64),(173,'shox',17017,49.6,14508,1.17,846,21960,0.77,0.13,0.66),(174,'hen1',2411,26.3,1898,1.27,129,3332,0.72,0.13,0.57),(175,'allu',11567,30.3,9789,1.18,585,15118,0.77,0.13,0.65),(176,'nex',9479,49.9,8097,1.17,463,12211,0.78,0.16,0.66),(177,'tarik',6986,36.9,6062,1.15,346,8951,0.78,0.15,0.68),(178,'spaze',4058,50.2,3616,1.12,193,5060,0.8,0.14,0.71),(179,'deadfox',3709,33.6,3234,1.15,183,4794,0.77,0.13,0.67),(180,'swag',2954,50.2,2475,1.19,148,3891,0.76,0.17,0.64),(181,'mir',2392,52.5,2039,1.17,117,3060,0.78,0.13,0.67),(182,'scream',13387,69.9,11553,1.16,689,17764,0.75,0.12,0.65),(183,'twist',9344,43.1,8262,1.13,459,12039,0.78,0.16,0.69),(184,'hiko',8135,53.2,6730,1.21,426,11184,0.73,0.15,0.6),(185,'skadoodle',7287,25,5978,1.22,388,10060,0.72,0.12,0.59),(186,'shroud',6318,50.9,5449,1.16,326,8315,0.76,0.15,0.66),(187,'keev',3418,29.8,2959,1.16,168,4439,0.77,0.1,0.67),(188,'joelz',3232,40.7,2791,1.16,161,4211,0.77,0.15,0.66),(189,'jks',2115,45.3,1805,1.17,119,2928,0.72,0.13,0.62),(190,'little',2289,28.1,1967,1.16,112,2970,0.77,0.12,0.66),(191,'flusha',16096,42,13763,1.17,835,21685,0.74,0.18,0.63),(192,'jw',16623,35.9,14617,1.14,833,21633,0.77,0.15,0.68),(193,'happy',15311,40.2,13010,1.18,768,19975,0.77,0.12,0.65),(194,'dupreeh',14707,50.9,12695,1.16,759,19451,0.76,0.15,0.65),(195,'chrisj',13049,36.7,11289,1.16,669,17519,0.74,0.12,0.64),(196,'v1c7or',8271,42.5,7218,1.15,431,11088,0.75,0.18,0.65),(197,'fallen',5632,29.4,4730,1.19,299,7784,0.72,0.12,0.61),(198,'naf-fly',5388,43.1,4668,1.15,268,7110,0.76,0.17,0.66),(199,'koosta',3272,26.8,2878,1.14,172,4396,0.74,0.12,0.65),(200,'ryx',2979,37.2,2638,1.13,140,3782,0.79,0.18,0.7),(201,'jr',2343,34.1,2033,1.15,119,3124,0.75,0.13,0.65);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-02 19:17:42
