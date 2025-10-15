/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	11.8.3-MariaDB-0+deb13u1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `juego_id` int(11) NOT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`juego_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`juego_id`) REFERENCES `tJuegos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tComentarios` VALUES
(1,'Mundo futurista inmersivo con narrativa compleja y gameplay mejorado tras actualizaciones.',1,1,'2025-10-15 19:01:55'),
(2,'Aventura abierta que reinventa la exploración con libertad y creatividad.',2,2,'2025-10-15 19:01:55'),
(3,'Acción épica y emotiva con una historia que profundiza en la mitología nórdica.',3,3,'2025-10-15 19:01:55'),
(4,'Shooter clásico con campaña sólida y multijugador competitivo.',4,4,'2025-10-15 19:01:55'),
(5,'Juego social divertido que mezcla colaboración y engaño en partidas rápidas.',5,5,'2025-10-15 19:01:55'),
(6,'Muy buen juego, lo he jugado en Nintendo Switch 2',NULL,2,'2025-10-15 19:01:55');
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `tJuegos`
--

DROP TABLE IF EXISTS `tJuegos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tJuegos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(200) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `plataforma` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tJuegos`
--

LOCK TABLES `tJuegos` WRITE;
/*!40000 ALTER TABLE `tJuegos` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tJuegos` VALUES
(1,'Cyberpunk 2077','https://image.api.playstation.com/vulcan/ap/rnd/202008/0416/6Bo40lnWU0BhgrOUm7Cb6by3.png','Un RPG futurista con un mundo abierto impresionante y una historia profunda, que ha mejorado mucho desde su lanzamiento inicial.','PC'),
(2,'The Legend of Zelda: Breath of the Wild','https://www.nintendo.com/eu/media/images/10_share_images/games_15/wiiu_14/SI_WiiU_TheLegendOfZeldaBreathOfTheWild_image1600w.jpg','Una aventura épica que redefine la exploración en un mundo abierto lleno de secretos y desafíos creativos.','Nintendo Switch'),
(3,'God of War Ragnarok','https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2322010/header.jpg?t=1750909504','Una secuela espectacular con una narrativa poderosa y combates intensos, que continúa la historia de Kratos y Atreus.','PS5'),
(4,'Halo Infinite','https://images.sftcdn.net/images/t_app-icon-m/p/a7dd82fb-5566-4f58-93bb-f5718dd913f9/2996025137/halo-infinite-download-halo-infinite.jpg','El regreso clásico de Master Chief con una campaña sólida y un multijugador muy entretenido y competitivo.','Xbox Series X'),
(5,'Among Us','https://www.nintendo.com/eu/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_AmongUs.jpg','Un juego social de deducción donde la comunicación y la traición son clave para sobrevivir y descubrir al impostor.','iOS/Android');
/*!40000 ALTER TABLE `tJuegos` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `tUsuarios` VALUES
(1,'Xian','Leon','xian@gmail.com','1234'),
(2,'Valentina','Ramirez','vramirez@gmail.com','1234'),
(3,'Mateo','Fernandez','mfernandez@gmail.com','1234'),
(4,'Camila','Torres','ctorres@gmail.com','1234'),
(5,'Santiago','Morales','smorales@gmail.com','1234');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-10-15 21:04:08
