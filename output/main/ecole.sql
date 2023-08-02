-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 24 déc. 2022 à 17:01
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ecole`
--

-- --------------------------------------------------------

--
-- Structure de la table `composer`
--

DROP TABLE IF EXISTS `composer`;
CREATE TABLE IF NOT EXISTS `composer` (
  `idetudiants` int(11) NOT NULL,
  `idmatieres` int(11) NOT NULL,
  `idevaluation` int(11) NOT NULL,
  `note` float DEFAULT NULL,
  PRIMARY KEY (`idetudiants`,`idmatieres`,`idevaluation`),
  KEY `idmatieres` (`idmatieres`),
  KEY `idevaluation` (`idevaluation`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `composer`
--

INSERT INTO `composer` (`idetudiants`, `idmatieres`, `idevaluation`, `note`) VALUES
(18, 4, 4, 12),
(18, 4, 3, 10),
(15, 4, 3, 14),
(17, 5, 5, 15),
(18, 4, 5, 17),
(16, 6, 4, 15),
(15, 4, 4, 15),
(15, 4, 5, 9),
(18, 5, 4, 17),
(17, 5, 3, 10),
(17, 5, 4, 7),
(17, 4, 3, 10),
(17, 4, 4, 11),
(17, 6, 3, 15),
(17, 4, 5, 13),
(17, 6, 4, 12),
(17, 6, 5, 15),
(15, 6, 4, 13),
(15, 6, 5, 20),
(15, 7, 5, 20);

-- --------------------------------------------------------

--
-- Structure de la table `etudiants`
--

DROP TABLE IF EXISTS `etudiants`;
CREATE TABLE IF NOT EXISTS `etudiants` (
  `idetudiants` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idetudiants`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `etudiants`
--

INSERT INTO `etudiants` (`idetudiants`, `Nom`) VALUES
(16, 'Azerty'),
(15, 'JEAN'),
(17, 'AZZEERTY'),
(18, 'Jack Polo                                           ');

-- --------------------------------------------------------

--
-- Structure de la table `evaluations`
--

DROP TABLE IF EXISTS `evaluations`;
CREATE TABLE IF NOT EXISTS `evaluations` (
  `idevaluation` int(11) NOT NULL AUTO_INCREMENT,
  `Nomevaluation` varchar(255) DEFAULT NULL,
  `Coefficient` int(11) DEFAULT NULL,
  PRIMARY KEY (`idevaluation`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `evaluations`
--

INSERT INTO `evaluations` (`idevaluation`, `Nomevaluation`, `Coefficient`) VALUES
(3, 'Devoir', 2),
(4, 'Interro', 1),
(5, 'Projet', 3);

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
CREATE TABLE IF NOT EXISTS `matieres` (
  `idmatieres` int(11) NOT NULL AUTO_INCREMENT,
  `NomMat` varchar(255) DEFAULT NULL,
  `CoefMat` int(11) NOT NULL,
  PRIMARY KEY (`idmatieres`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`idmatieres`, `NomMat`, `CoefMat`) VALUES
(4, 'SQL', 3),
(5, 'C#', 1),
(6, 'Excel', 4),
(7, 'eps', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
