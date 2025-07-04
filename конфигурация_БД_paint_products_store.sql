CREATE DATABASE `paint_products_store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `categories` (
  `id_categories` int NOT NULL AUTO_INCREMENT,
  `name_categories` varchar(45) NOT NULL,
  PRIMARY KEY (`id_categories`),
  UNIQUE KEY `id_categories_UNIQUE` (`id_categories`),
  UNIQUE KEY `name_categories_UNIQUE` (`name_categories`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `clients` (
  `id_clients` int NOT NULL AUTO_INCREMENT,
  `surname_client` varchar(45) NOT NULL,
  `name_client` varchar(45) NOT NULL,
  `patronymic_client` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(200) NOT NULL,
  `id_roles_3` int NOT NULL DEFAULT '3',
  PRIMARY KEY (`id_clients`),
  UNIQUE KEY `id_clients_UNIQUE` (`id_clients`),
  UNIQUE KEY `phone_UNIQUE` (`email`),
  KEY `id_roles_idx` (`id_roles_3`),
  CONSTRAINT `id_roles3` FOREIGN KEY (`id_roles_3`) REFERENCES `roles` (`id_roles`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `products` (
  `id_product` int NOT NULL AUTO_INCREMENT,
  `name_product` varchar(100) NOT NULL,
  `price` float NOT NULL,
  `volume` float NOT NULL,
  `id_categories` int NOT NULL,
  `id_type_material` int DEFAULT NULL,
  `id_type_coloring_agent` int DEFAULT NULL,
  `id_type_color` int DEFAULT NULL,
  `id_type_gloss` int DEFAULT NULL,
  `id_type_method_application` int DEFAULT NULL,
  PRIMARY KEY (`id_product`),
  UNIQUE KEY `name_features_UNIQUE` (`name_product`) /*!80000 INVISIBLE */,
  UNIQUE KEY `id_product_UNIQUE` (`id_product`),
  KEY `id_categories_idx` (`id_categories`),
  KEY `id_type_material_idx` (`id_type_material`),
  KEY `id_type_coloring_agent_idx` (`id_type_coloring_agent`),
  KEY `id_type_color_idx` (`id_type_color`),
  KEY `id_type_gloss_idx` (`id_type_gloss`),
  KEY `id_type_method_application_idx` (`id_type_method_application`),
  CONSTRAINT `id_categories` FOREIGN KEY (`id_categories`) REFERENCES `categories` (`id_categories`),
  CONSTRAINT `id_type_color` FOREIGN KEY (`id_type_color`) REFERENCES `type_color` (`id_type_color`),
  CONSTRAINT `id_type_coloring_agent` FOREIGN KEY (`id_type_coloring_agent`) REFERENCES `type_coloring_agent` (`id_type_coloring_agent`),
  CONSTRAINT `id_type_gloss` FOREIGN KEY (`id_type_gloss`) REFERENCES `type_gloss` (`id_type_gloss`),
  CONSTRAINT `id_type_material` FOREIGN KEY (`id_type_material`) REFERENCES `type_material` (`id_type_material`),
  CONSTRAINT `id_type_method_application` FOREIGN KEY (`id_type_method_application`) REFERENCES `type_method_application` (`id_type_method_application`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `roles` (
  `id_roles` int NOT NULL AUTO_INCREMENT,
  `name_roles` varchar(45) NOT NULL,
  PRIMARY KEY (`id_roles`),
  UNIQUE KEY `id_roles_UNIQUE` (`id_roles`),
  UNIQUE KEY `name_roles_UNIQUE` (`name_roles`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `staff` (
  `id_staff` int NOT NULL AUTO_INCREMENT,
  `surname_staff` varchar(45) NOT NULL,
  `name_staff` varchar(45) NOT NULL,
  `patronymic_staff` varchar(45) DEFAULT NULL,
  `login_staff` varchar(45) NOT NULL,
  `password_staff` varchar(200) NOT NULL,
  `id_roles` int NOT NULL,
  PRIMARY KEY (`id_staff`),
  UNIQUE KEY `id_staff_UNIQUE` (`id_staff`),
  UNIQUE KEY `login_staff_UNIQUE` (`login_staff`),
  KEY `id_roles_idx` (`id_roles`),
  CONSTRAINT `id_roles` FOREIGN KEY (`id_roles`) REFERENCES `roles` (`id_roles`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `type_color` (
  `id_type_color` int NOT NULL AUTO_INCREMENT,
  `name_color` varchar(45) NOT NULL,
  PRIMARY KEY (`id_type_color`),
  UNIQUE KEY `name_color_UNIQUE` (`name_color`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `type_coloring_agent` (
  `id_type_coloring_agent` int NOT NULL AUTO_INCREMENT,
  `name_type_coloring_agent` varchar(45) NOT NULL,
  PRIMARY KEY (`id_type_coloring_agent`),
  UNIQUE KEY `id_type_coloring_agent_UNIQUE` (`id_type_coloring_agent`),
  UNIQUE KEY `name_type_coloring_agent_UNIQUE` (`name_type_coloring_agent`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `type_gloss` (
  `id_type_gloss` int NOT NULL AUTO_INCREMENT,
  `name_gloss` varchar(45) NOT NULL,
  PRIMARY KEY (`id_type_gloss`),
  UNIQUE KEY `id_type_gloss_UNIQUE` (`id_type_gloss`),
  UNIQUE KEY `name_gloss_UNIQUE` (`name_gloss`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `type_material` (
  `id_type_material` int NOT NULL AUTO_INCREMENT,
  `name_type_material` varchar(45) NOT NULL,
  PRIMARY KEY (`id_type_material`),
  UNIQUE KEY `id_type_material_UNIQUE` (`id_type_material`),
  UNIQUE KEY `name_type_material_UNIQUE` (`name_type_material`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `type_method_application` (
  `id_type_method_application` int NOT NULL AUTO_INCREMENT,
  `name_method_application` varchar(45) NOT NULL,
  PRIMARY KEY (`id_type_method_application`),
  UNIQUE KEY `id_type_method_application_UNIQUE` (`id_type_method_application`),
  UNIQUE KEY `name_method_application_UNIQUE` (`name_method_application`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
