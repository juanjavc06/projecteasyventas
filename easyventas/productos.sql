-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: sellpoint
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.17.10.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add almacen',7,'add_almacen'),(26,'Can change almacen',7,'change_almacen'),(27,'Can delete almacen',7,'delete_almacen'),(28,'Can view almacen',7,'view_almacen'),(29,'Can add categoria_ productos',8,'add_categoria_productos'),(30,'Can change categoria_ productos',8,'change_categoria_productos'),(31,'Can delete categoria_ productos',8,'delete_categoria_productos'),(32,'Can view categoria_ productos',8,'view_categoria_productos'),(33,'Can add compras',9,'add_compras'),(34,'Can change compras',9,'change_compras'),(35,'Can delete compras',9,'delete_compras'),(36,'Can view compras',9,'view_compras'),(37,'Can add compras_ detalle',10,'add_compras_detalle'),(38,'Can change compras_ detalle',10,'change_compras_detalle'),(39,'Can delete compras_ detalle',10,'delete_compras_detalle'),(40,'Can view compras_ detalle',10,'view_compras_detalle'),(41,'Can add corte',11,'add_corte'),(42,'Can change corte',11,'change_corte'),(43,'Can delete corte',11,'delete_corte'),(44,'Can view corte',11,'view_corte'),(45,'Can add detalle_ corte',12,'add_detalle_corte'),(46,'Can change detalle_ corte',12,'change_detalle_corte'),(47,'Can delete detalle_ corte',12,'delete_detalle_corte'),(48,'Can view detalle_ corte',12,'view_detalle_corte'),(49,'Can add inventario',13,'add_inventario'),(50,'Can change inventario',13,'change_inventario'),(51,'Can delete inventario',13,'delete_inventario'),(52,'Can view inventario',13,'view_inventario'),(53,'Can add movimientos',14,'add_movimientos'),(54,'Can change movimientos',14,'change_movimientos'),(55,'Can delete movimientos',14,'delete_movimientos'),(56,'Can view movimientos',14,'view_movimientos'),(57,'Can add perfiles',15,'add_perfiles'),(58,'Can change perfiles',15,'change_perfiles'),(59,'Can delete perfiles',15,'delete_perfiles'),(60,'Can view perfiles',15,'view_perfiles'),(61,'Can add productos',16,'add_productos'),(62,'Can change productos',16,'change_productos'),(63,'Can delete productos',16,'delete_productos'),(64,'Can view productos',16,'view_productos'),(65,'Can add productos_ proveedores',17,'add_productos_proveedores'),(66,'Can change productos_ proveedores',17,'change_productos_proveedores'),(67,'Can delete productos_ proveedores',17,'delete_productos_proveedores'),(68,'Can view productos_ proveedores',17,'view_productos_proveedores'),(69,'Can add proveedores_ clientes',18,'add_proveedores_clientes'),(70,'Can change proveedores_ clientes',18,'change_proveedores_clientes'),(71,'Can delete proveedores_ clientes',18,'delete_proveedores_clientes'),(72,'Can view proveedores_ clientes',18,'view_proveedores_clientes'),(73,'Can add usuarios',19,'add_usuarios'),(74,'Can change usuarios',19,'change_usuarios'),(75,'Can delete usuarios',19,'delete_usuarios'),(76,'Can view usuarios',19,'view_usuarios'),(77,'Can add ventas',20,'add_ventas'),(78,'Can change ventas',20,'change_ventas'),(79,'Can delete ventas',20,'delete_ventas'),(80,'Can view ventas',20,'view_ventas'),(81,'Can add ventas_ detalle',21,'add_ventas_detalle'),(82,'Can change ventas_ detalle',21,'change_ventas_detalle'),(83,'Can delete ventas_ detalle',21,'delete_ventas_detalle'),(84,'Can view ventas_ detalle',21,'view_ventas_detalle'),(85,'Can add zona',22,'add_zona'),(86,'Can change zona',22,'change_zona'),(87,'Can delete zona',22,'delete_zona'),(88,'Can view zona',22,'view_zona');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'sellpoint','almacen'),(8,'sellpoint','categoria_productos'),(9,'sellpoint','compras'),(10,'sellpoint','compras_detalle'),(11,'sellpoint','corte'),(12,'sellpoint','detalle_corte'),(13,'sellpoint','inventario'),(14,'sellpoint','movimientos'),(15,'sellpoint','perfiles'),(16,'sellpoint','productos'),(17,'sellpoint','productos_proveedores'),(18,'sellpoint','proveedores_clientes'),(19,'sellpoint','usuarios'),(20,'sellpoint','ventas'),(21,'sellpoint','ventas_detalle'),(22,'sellpoint','zona'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-30 00:15:38.715423'),(2,'auth','0001_initial','2018-11-30 00:15:43.465486'),(3,'admin','0001_initial','2018-11-30 00:15:44.548754'),(4,'admin','0002_logentry_remove_auto_add','2018-11-30 00:15:44.578025'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-30 00:15:44.608422'),(6,'contenttypes','0002_remove_content_type_name','2018-11-30 00:15:45.273998'),(7,'auth','0002_alter_permission_name_max_length','2018-11-30 00:15:45.348684'),(8,'auth','0003_alter_user_email_max_length','2018-11-30 00:15:45.432034'),(9,'auth','0004_alter_user_username_opts','2018-11-30 00:15:45.461298'),(10,'auth','0005_alter_user_last_login_null','2018-11-30 00:15:46.020113'),(11,'auth','0006_require_contenttypes_0002','2018-11-30 00:15:46.040009'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-30 00:15:46.070772'),(13,'auth','0008_alter_user_username_max_length','2018-11-30 00:15:46.295113'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-30 00:15:46.370108'),(15,'sellpoint','0001_initial','2018-11-30 00:15:57.145343'),(16,'sellpoint','0002_auto_20181130_0015','2018-11-30 00:15:57.229023'),(17,'sessions','0001_initial','2018-11-30 00:15:57.562100'),(18,'sellpoint','0003_auto_20181130_0158','2018-11-30 01:58:12.957229');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_almacen`
--

DROP TABLE IF EXISTS `sellpoint_almacen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_almacen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `almacen` varchar(255) NOT NULL,
  `zona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_almacen_zona_id_8b9edd22_fk_sellpoint_zona_id` (`zona_id`),
  CONSTRAINT `sellpoint_almacen_zona_id_8b9edd22_fk_sellpoint_zona_id` FOREIGN KEY (`zona_id`) REFERENCES `sellpoint_zona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_almacen`
--

LOCK TABLES `sellpoint_almacen` WRITE;
/*!40000 ALTER TABLE `sellpoint_almacen` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_almacen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_categoria_productos`
--

DROP TABLE IF EXISTS `sellpoint_categoria_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_categoria_productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(50) NOT NULL,
  `descripcion_categoria` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_categoria_productos`
--

LOCK TABLES `sellpoint_categoria_productos` WRITE;
/*!40000 ALTER TABLE `sellpoint_categoria_productos` DISABLE KEYS */;
INSERT INTO `sellpoint_categoria_productos` VALUES (1,'Lacteos','Productos elaborados a base de leche'),(2,'Cereales','Semillas de trigo o maiz'),(3,'Carnes','Alimentos de origen animal');
/*!40000 ALTER TABLE `sellpoint_categoria_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_compras`
--

DROP TABLE IF EXISTS `sellpoint_compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_compras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `sub_total` double NOT NULL,
  `impuestos` double NOT NULL,
  `total` double NOT NULL,
  `fecha_entrega` date NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_compras_proveedor_id_91eec7c8_fk_sellpoint` (`proveedor_id`),
  CONSTRAINT `sellpoint_compras_proveedor_id_91eec7c8_fk_sellpoint` FOREIGN KEY (`proveedor_id`) REFERENCES `sellpoint_proveedores_clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_compras`
--

LOCK TABLES `sellpoint_compras` WRITE;
/*!40000 ALTER TABLE `sellpoint_compras` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_compras_detalle`
--

DROP TABLE IF EXISTS `sellpoint_compras_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_compras_detalle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` double NOT NULL,
  `total_producto` double NOT NULL,
  `compra_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_compras_de_compra_id_508f1dc2_fk_sellpoint` (`compra_id`),
  KEY `sellpoint_compras_de_producto_id_cc81f1b7_fk_sellpoint` (`producto_id`),
  CONSTRAINT `sellpoint_compras_de_compra_id_508f1dc2_fk_sellpoint` FOREIGN KEY (`compra_id`) REFERENCES `sellpoint_compras` (`id`),
  CONSTRAINT `sellpoint_compras_de_producto_id_cc81f1b7_fk_sellpoint` FOREIGN KEY (`producto_id`) REFERENCES `sellpoint_productos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_compras_detalle`
--

LOCK TABLES `sellpoint_compras_detalle` WRITE;
/*!40000 ALTER TABLE `sellpoint_compras_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_compras_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_corte`
--

DROP TABLE IF EXISTS `sellpoint_corte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_corte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `total_vendido` int(11) NOT NULL,
  `total_comprado` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_corte`
--

LOCK TABLES `sellpoint_corte` WRITE;
/*!40000 ALTER TABLE `sellpoint_corte` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_corte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_detalle_corte`
--

DROP TABLE IF EXISTS `sellpoint_detalle_corte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_detalle_corte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `producto` varchar(200) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `total` double NOT NULL,
  `iva` double NOT NULL,
  `corte_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_detalle_corte_corte_id_b8fb7c8a_fk_sellpoint_corte_id` (`corte_id`),
  CONSTRAINT `sellpoint_detalle_corte_corte_id_b8fb7c8a_fk_sellpoint_corte_id` FOREIGN KEY (`corte_id`) REFERENCES `sellpoint_corte` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_detalle_corte`
--

LOCK TABLES `sellpoint_detalle_corte` WRITE;
/*!40000 ALTER TABLE `sellpoint_detalle_corte` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_detalle_corte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_inventario`
--

DROP TABLE IF EXISTS `sellpoint_inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_inventario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `existencias` int(11) NOT NULL,
  `producto` varchar(200) NOT NULL,
  `zona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_inventario_zona_id_805b9ff9_fk_sellpoint_zona_id` (`zona_id`),
  CONSTRAINT `sellpoint_inventario_zona_id_805b9ff9_fk_sellpoint_zona_id` FOREIGN KEY (`zona_id`) REFERENCES `sellpoint_zona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_inventario`
--

LOCK TABLES `sellpoint_inventario` WRITE;
/*!40000 ALTER TABLE `sellpoint_inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_movimientos`
--

DROP TABLE IF EXISTS `sellpoint_movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_movimientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) NOT NULL,
  `producto` varchar(200) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `zona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_movimientos_zona_id_19ddce51_fk_sellpoint_zona_id` (`zona_id`),
  CONSTRAINT `sellpoint_movimientos_zona_id_19ddce51_fk_sellpoint_zona_id` FOREIGN KEY (`zona_id`) REFERENCES `sellpoint_zona` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_movimientos`
--

LOCK TABLES `sellpoint_movimientos` WRITE;
/*!40000 ALTER TABLE `sellpoint_movimientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_movimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_perfiles`
--

DROP TABLE IF EXISTS `sellpoint_perfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_perfiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `perfil` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_perfiles`
--

LOCK TABLES `sellpoint_perfiles` WRITE;
/*!40000 ALTER TABLE `sellpoint_perfiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_perfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_productos`
--

DROP TABLE IF EXISTS `sellpoint_productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `unidad_medida` varchar(4) NOT NULL,
  `inventario_minimo` double NOT NULL,
  `inventario_maximo` double NOT NULL,
  `imagen` longblob NOT NULL,
  `precio` double NOT NULL,
  `categoria_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_productos_categoria_id_9d6b25e4_fk_sellpoint` (`categoria_id`),
  CONSTRAINT `sellpoint_productos_categoria_id_9d6b25e4_fk_sellpoint` FOREIGN KEY (`categoria_id`) REFERENCES `sellpoint_categoria_productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_productos`
--

LOCK TABLES `sellpoint_productos` WRITE;
/*!40000 ALTER TABLE `sellpoint_productos` DISABLE KEYS */;
INSERT INTO `sellpoint_productos` VALUES (1,'Nutri-Leche','PRODUCTO ELABORADO CON GRASA VEGETAL SEMIPASTEURIZADO','LT',16,60,'',13,1),(2,'Jamon','Carne de cerdo en rebanadas','KG',3,8,'',80,3);
/*!40000 ALTER TABLE `sellpoint_productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_productos_proveedores`
--

DROP TABLE IF EXISTS `sellpoint_productos_proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_productos_proveedores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `costo_total` double NOT NULL,
  `producto_id` int(11) NOT NULL,
  `proveedor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_productos__producto_id_d5ee678b_fk_sellpoint` (`producto_id`),
  KEY `sellpoint_productos__proveedor_id_5a5f2874_fk_sellpoint` (`proveedor_id`),
  CONSTRAINT `sellpoint_productos__producto_id_d5ee678b_fk_sellpoint` FOREIGN KEY (`producto_id`) REFERENCES `sellpoint_productos` (`id`),
  CONSTRAINT `sellpoint_productos__proveedor_id_5a5f2874_fk_sellpoint` FOREIGN KEY (`proveedor_id`) REFERENCES `sellpoint_proveedores_clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_productos_proveedores`
--

LOCK TABLES `sellpoint_productos_proveedores` WRITE;
/*!40000 ALTER TABLE `sellpoint_productos_proveedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_productos_proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_proveedores_clientes`
--

DROP TABLE IF EXISTS `sellpoint_proveedores_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_proveedores_clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_comencial` varchar(255) NOT NULL,
  `rfc` varchar(18) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `tipo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_proveedores_clientes`
--

LOCK TABLES `sellpoint_proveedores_clientes` WRITE;
/*!40000 ALTER TABLE `sellpoint_proveedores_clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_proveedores_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_usuarios`
--

DROP TABLE IF EXISTS `sellpoint_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuarios` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `password` varchar(100) NOT NULL,
  `perfil_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_usuarios_perfil_id_4948f69b_fk_sellpoint_perfiles_id` (`perfil_id`),
  CONSTRAINT `sellpoint_usuarios_perfil_id_4948f69b_fk_sellpoint_perfiles_id` FOREIGN KEY (`perfil_id`) REFERENCES `sellpoint_perfiles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_usuarios`
--

LOCK TABLES `sellpoint_usuarios` WRITE;
/*!40000 ALTER TABLE `sellpoint_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_ventas`
--

DROP TABLE IF EXISTS `sellpoint_ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_ventas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `sub_total` double NOT NULL,
  `impuestos` double NOT NULL,
  `total` double NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_ventas_cliente_id_2b9fe604_fk_sellpoint` (`cliente_id`),
  CONSTRAINT `sellpoint_ventas_cliente_id_2b9fe604_fk_sellpoint` FOREIGN KEY (`cliente_id`) REFERENCES `sellpoint_proveedores_clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_ventas`
--

LOCK TABLES `sellpoint_ventas` WRITE;
/*!40000 ALTER TABLE `sellpoint_ventas` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_ventas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_ventas_detalle`
--

DROP TABLE IF EXISTS `sellpoint_ventas_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_ventas_detalle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` double NOT NULL,
  `total_producto` double NOT NULL,
  `producto_id` int(11) NOT NULL,
  `venta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sellpoint_ventas_det_producto_id_17a70b81_fk_sellpoint` (`producto_id`),
  KEY `sellpoint_ventas_det_venta_id_6c4f4a74_fk_sellpoint` (`venta_id`),
  CONSTRAINT `sellpoint_ventas_det_producto_id_17a70b81_fk_sellpoint` FOREIGN KEY (`producto_id`) REFERENCES `sellpoint_productos` (`id`),
  CONSTRAINT `sellpoint_ventas_det_venta_id_6c4f4a74_fk_sellpoint` FOREIGN KEY (`venta_id`) REFERENCES `sellpoint_ventas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_ventas_detalle`
--

LOCK TABLES `sellpoint_ventas_detalle` WRITE;
/*!40000 ALTER TABLE `sellpoint_ventas_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_ventas_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sellpoint_zona`
--

DROP TABLE IF EXISTS `sellpoint_zona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sellpoint_zona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zona` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sellpoint_zona`
--

LOCK TABLES `sellpoint_zona` WRITE;
/*!40000 ALTER TABLE `sellpoint_zona` DISABLE KEYS */;
/*!40000 ALTER TABLE `sellpoint_zona` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-29 22:07:37
