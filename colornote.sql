-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 28, 2024 at 02:19 PM
-- Server version: 10.6.16-MariaDB-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `colornote`
--

-- --------------------------------------------------------

--
-- Table structure for table `chat1vs1`
--

CREATE TABLE `chat1vs1` (
  `id` int(11) NOT NULL,
  `idSend` int(11) NOT NULL,
  `idReceive` int(11) NOT NULL,
  `room` text NOT NULL,
  `text` text DEFAULT NULL,
  `img` text DEFAULT NULL,
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'text',
  `state` varchar(50) DEFAULT 'not seen',
  `sendAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chat1vs1`
--

INSERT INTO `chat1vs1` (`id`, `idSend`, `idReceive`, `room`, `text`, `img`, `type`, `state`, `sendAt`) VALUES
(1, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-03 14:07:36'),
(2, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-03 15:25:40'),
(3, 2, 1, '21410', '19/10/2023', NULL, 'text1', 'not seen', '2023-11-03 15:36:36'),
(4, 2, 1, '21410', '19/10/2023', NULL, 'text1', 'not seen', '2023-11-03 15:36:37'),
(5, 2, 1, '21410', '19/10/2023', NULL, 'text1', 'not seen', '2023-11-03 15:39:41'),
(6, 2, 1, '21410', '19/10/2023', NULL, 'text1', 'not seen', '2023-11-03 16:06:25'),
(7, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-08 16:38:46'),
(8, 1, 2, '21410', 'hello', NULL, 'text', 'not seen', '2023-11-08 16:39:02'),
(9, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-15 10:22:18'),
(10, 1, 2, '21410', '15/11/2023', NULL, 'text', 'not seen', '2023-11-15 10:22:39'),
(11, 1, 2, '21410', '15/11/2023', NULL, 'text', 'not seen', '2023-11-15 10:27:37'),
(12, 1, 2, '21410', '15/11/2023', NULL, 'text', 'not seen', '2023-11-15 11:08:19'),
(13, 1, 2, '21410', '15/11/2023', NULL, 'text', 'not seen', '2023-11-15 14:25:50'),
(14, 1, 2, '21410', 'test1', NULL, 'text', 'not seen', '2023-11-15 14:26:51'),
(15, 1, 2, '21410', 'test2', NULL, 'text', 'not seen', '2023-11-15 14:39:16'),
(16, 1, 2, '21410', 'test2', NULL, 'text', 'not seen', '2023-11-15 14:43:41'),
(17, 1, 2, '21410', 'test3', NULL, 'text', 'not seen', '2023-11-15 14:49:18'),
(18, 1, 2, '21410', 'test4', NULL, 'text', 'not seen', '2023-11-15 14:53:34'),
(19, 1, 2, '21410', 'test5', NULL, 'text', 'not seen', '2023-11-15 15:05:14'),
(20, 2, 1, '21410', 'test6', NULL, 'text', 'not seen', '2023-11-15 15:19:04'),
(21, 1, 2, '21410', 'test6', NULL, 'text', 'not seen', '2023-11-15 15:19:30'),
(22, 1, 2, '21410', 'test7', NULL, 'text', 'not seen', '2023-11-15 15:27:23'),
(23, 1, 2, '21410', 'test8', NULL, 'text', 'not seen', '2023-11-15 15:28:41'),
(24, 1, 2, '21410', 'test8', NULL, 'text', 'not seen', '2023-11-15 15:29:36'),
(25, 1, 2, '21410', 'mesage1', NULL, 'text', 'not seen', '2023-11-15 16:03:08'),
(26, 1, 2, '21410', 'mesage1', NULL, 'text', 'not seen', '2023-11-15 16:04:20'),
(27, 1, 2, '21410', 'mesage3', NULL, 'text', 'not seen', '2023-11-15 16:05:52'),
(28, 1, 2, '21410', 'mesage3', NULL, 'text', 'not seen', '2023-11-15 16:14:10'),
(29, 1, 2, '21410', 'test1', NULL, 'text', 'seen', '2023-11-15 16:18:47'),
(30, 2, 1, '21410', 'test2', NULL, 'text', 'not seen', '2023-11-15 16:20:39'),
(31, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-19 15:42:57'),
(32, 1, 2, '21410', '19/10/2023', NULL, 'text', 'not seen', '2023-11-19 16:38:47'),
(33, 1, 2, '21410', NULL, 'https://i.ibb.co/2MJkg5P/Screenshot-2023-05-07-142345.png', 'image', 'not seen', '2023-11-19 22:02:38'),
(34, 1, 2, '21410', NULL, 'hello1', 'image', 'not seen', '2023-11-19 22:05:27'),
(35, 1, 2, '21410', NULL, 'https://i.ibb.co/2MJkg5P/Screenshot-2023-05-07-142345.png', 'image', 'not seen', '2023-11-27 15:08:18');

-- --------------------------------------------------------

--
-- Table structure for table `chats`
--

CREATE TABLE `chats` (
  `idGroup` int(11) NOT NULL,
  `idMes` int(11) NOT NULL,
  `text` text DEFAULT NULL,
  `image` text DEFAULT NULL,
  `type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `idSend` int(11) NOT NULL,
  `sendAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `chatunknowns`
--

CREATE TABLE `chatunknowns` (
  `idReceive` int(11) NOT NULL,
  `idMes` int(11) NOT NULL,
  `idSend` text NOT NULL,
  `text` text DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'seen',
  `sendAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chatunknowns`
--

INSERT INTO `chatunknowns` (`idReceive`, `idMes`, `idSend`, `text`, `status`, `sendAt`) VALUES
(1, 1, '1', 'hello', 'seen', '2023-07-12 14:12:06'),
(1, 2, '1', 'hello', 'seen', '2023-07-12 14:12:06');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `idNote` int(11) NOT NULL,
  `text` text DEFAULT NULL,
  `sendAt` datetime NOT NULL,
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `datas`
--

CREATE TABLE `datas` (
  `idData` int(11) NOT NULL,
  `idNote` int(11) NOT NULL,
  `content` text NOT NULL,
  `image` text DEFAULT NULL,
  `doneContent` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `datas`
--

INSERT INTO `datas` (`idData`, `idNote`, `content`, `image`, `doneContent`) VALUES
(1, 3, 'Local Host123', 'http://127.0.0.1:18011/get-image/1/1_note_892195.jpg', 0),
(3, 5, 'Hôm nay là thứ năm \nHôm nay là thứ năm \nHôm nay là thứ năm \nHôm nay là thứ năm \nHôm nay là thứ năm', '', 0),
(4, 6, 'yes', '', 0),
(5, 7, 'yes', '', 0),
(6, 10, 'yes', '', 0),
(7, 14, 'yes', '', 0),
(8, 15, '98/11/2023', '', 0),
(9, 29, '1.1', '', 0),
(10, 32, '1.3', '', 0),
(11, 33, '1.3', '', 0),
(12, 43, 'long1', '', 0),
(13, 43, 'long2', '', 1),
(14, 44, 'checklist1', '', 0),
(15, 44, 'checklist2', '', 1),
(16, 44, 'checklist3', '', 1),
(17, 45, 'checklist1', '', 0),
(18, 45, 'checklist2', '', 1),
(19, 45, 'checklist3', '', 1),
(20, 46, 'checklist1', '', 0),
(21, 46, 'checklist2', '', 1),
(22, 46, 'checklist3', '', 1),
(23, 47, 'checklist1', '', 0),
(24, 47, 'checklist2', '', 0),
(25, 47, 'checklist3', '', 0),
(27, 49, 'checklist1', '', 0),
(28, 49, 'checklist2', '', 0),
(29, 49, 'checklist3', '', 0),
(30, 50, 'test1', '', 0),
(31, 50, 'test2', '', 0),
(32, 50, 'test3', '', 0),
(33, 51, 'Hello world', '', 0),
(37, 53, 'test1', '', 0),
(38, 53, 'test2', '', 0),
(39, 53, 'test3', '', 0),
(40, 54, 'test1', '', 0),
(41, 54, 'test2', '', 0),
(42, 54, 'test3', '', 0),
(43, 55, 'test1', '', 0),
(44, 55, 'test2', '', 0),
(45, 55, 'test3', '', 0),
(48, 8, 'Hello', '', 0),
(49, 8, 'hello2', '', 1),
(50, 56, '', '', 0),
(51, 56, 'test2', '', 0),
(52, 56, 'test3', '', 0),
(53, 57, '123456', '', 0),
(54, 58, 'abc', '', 0),
(55, 59, 'abc', '', 0),
(56, 60, 'Asd', '', 0),
(57, 61, 'Add', '', 0),
(58, 62, 'Saldana', '', 0),
(59, 63, 'add', '', 0),
(60, 63, 'asd', '', 0),
(61, 64, '123456', '', 0),
(63, 65, 'jagsjdgajs', '', 1),
(64, 66, 'Asdsdsd', '', 0),
(65, 67, 'test1', '', 0),
(66, 67, 'test2', '', 0),
(67, 67, 'test3', '', 0),
(68, 68, 'test1', '', 0),
(69, 68, 'test2', '', 0),
(70, 68, 'test3', '', 0),
(71, 69, 'test1-1-1', '', 0),
(72, 69, 'test2', '', 0),
(73, 69, 'test3', '', 0),
(74, 70, 'this is content', '', 0),
(75, 73, 'this text content', '', 0),
(76, 74, 'this test content', '', 0),
(77, 76, 'hello ádawdkfkadkavmadc', '', 0),
(78, 77, 'test', '', 0),
(79, 78, '235 638808 - ‹ Celebrity Mill... Celebrity Millennium 12 Night Best of Japan V2-Veranda 8031 Booking Reservation ID: 7000115 9/24 Tokyo (Yokohama), Japan 9/25 Mt. Fuji (Shimiza), Japan 9/26 At Sea 9/27 Kyoto (Osaka), Japan 9/28 Kyoto (Osalka), Japan 9/29 Hiroshima, Japan 9/30 Al Sea 10/01 Busan, South Korea 10/02 A1 Sea 10/03 Hakodate, Japan 10/04 Aomon, Japan 10/05 At Sea 10/06 Токур (Узислата), Japan Bottle of vinegar and scap for fruit flyes Monkey Kart', '', 0),
(80, 79, '\nAir France 800-237-2747 FFlyer#5165733864 \nUser: mmcurry1240@outlook.com Password:12404719Av@lon\nMarilyn Ticket Locator: P39Y2C \n\nSeat Number: 31A\nSeat Number: 29J \nSeat Number: 29J \nSeat Number: 31A \n\nSelina\'s Seat Number: 30A \nSelina\'s Seat Number: 29C \nSelina\'s Seat Number: 29C \nSelina\'s Seat Number: 30A', '', 0),
(81, 80, '\nAzul Airlines reservation code:\nLGE6NP\n\nGOL \nCynthia 9C\nMargaret 9A\nMarilyn 6D\nMIA-BSB\n\nBSB-SDU\nMarilyn 1A\nMargaret 1F\nCynthia', '', 0),
(84, 82, 'Nusskuchen', '', 0),
(91, 85, 'thứ 6', '', 0),
(92, 86, 'thứ 3', '', 0),
(93, 87, '', '', 0),
(94, 88, '', '', 0),
(95, 89, 'Google. Myshadow@11', '', 0),
(96, 90, '', '', 0),
(97, 91, 'jhjhjhjh', '', 0),
(98, 92, '', '', 0),
(99, 93, 'dgxdfgxdnfkdsnvkjdfnvkjnvlfnvfkd\n', '', 0),
(100, 94, 'bao dep chai\n', '', 0),
(101, 95, 'test note content', '', 0),
(102, 96, 'test content 2', '', 0),
(103, 97, 'Pool&schaumparty\n\ncafe del mar\n\nSauna\n\nunderbirded\n\nchrissisLustraum\n\nWhitegirls <3 Black\n\n/Appinfo\n\nBlack lives matter\n\nSwingclub\n\nAuszeit     0607\n\ncafe del mar\n\nMädchen \n\nUnheilig1x\n\nClub Angie\n\nReitstall\n\n/cl NICKNAME:Begründung\n\n/cl NICKNAME:Begründung\n\n\nBDSM\n\nfeuerderhölle. (privat Raum JJ)\nRot-weiß-rot\n\nXxschlaflosxx\n\nSamiras Lounge 1909\n\nSpielwiese\n\nHeaven&hell PW Valeria\n\nCs\n\nUnanständig\n\nFesselspiele \n\nLeonie666\n\nSexyParty\nRedligts\n\nRLP Adrian\nAlles 46 burki\n\n/cl nick:grund      / bannen für 24h\n/mute     schweigen\n\nHi zusammen, gibt es hier wen der (oder die) Interesse an vernünftigem und vor allem ausführlichen Cybersex hat? Und mit vernünftig meine ich das man mehr als nur dumme Pornosprüche drauf hat und noch dazu in der Lage ist ganze Sätze zu formulieren. Man sollte es schon schaffen 3 bis 4 Sätze am Stück zu schreiben. \n\nDas schick ich in die Channels\n\n/bl   bannen\n/Info      Channelinfo\n\n/smikeytrade nick , kann man so ein tauschfenster aufmachen Marktplatz \n\nFeelice\n\nhttps://knuddels-wiki.de/index.php/Weltreise/Weltreise_Abenteuer\n\nGoldregen: /go4gold Nick\n\n/Hero Nick: Begründung\n\n/p Shady man,Flugtschabo: text\n\nSession\n050215b9176e6ed9e8d26c93a7c8f95f8552b016e836a9401179d7421280d62c6a\n\nSuccubus\n\nSpielplatz der Lust\n\nRollenspiele 18+\n\n/ufoattack [NICK]\n\n/fotoxmaslove', '', 0),
(104, 98, 'URSSAF, Prélèvements 2022\n29 décembre VIREMENT 3000 eu 16 décembre 496 eu\n24 novembre 465 eu\n18 novembre 1334.83 eu 18 octobre 476 eu\n10 octobre 834.90 eu 16 septembre 446 eu\n8 septembre 834.90 eu 17 août 327 eu\n8 août 834.90 eu 18 juillet 786 eu 5 juillet 1285 eu\nTotal 11120.53 eu\n2023\n5 janvier 2484 eu\n7 janvier 1045 eu 6 février 2484 eu\n17 février 507 eu\n\n 6 mars 2484 eu 16 mars 494 eu 5 avril 2484 eu\n18. avril 473 eu 5 mai 2484 eu\n7mai357eu\n5 juin 2484 eu 16juin 1539eu\n5 juillet 928 eu\n5 septembre 2440 eu 5 octobre 1221 eu\n6 novembre 1331 eu 5 décembre 1216 eu\nTotal 26455 eu\n', '', 0),
(105, 99, 'URSSAF, Prélèvements 2022\n29 décembre VIREMENT 3000 eu 16 décembre 496 eu\n24 novembre 465 eu\n18 novembre 1334.83 eu 18 octobre 476 eu\n10 octobre 834.90 eu 16 septembre 446 eu\n8 septembre 834.90 eu 17 août 327 eu\n8 août 834.90 eu 18 juillet 786 eu 5 juillet 1285 eu\nTotal 11120.53 eu\n2023\n5 janvier 2484 eu\n7 janvier 1045 eu 6 février 2484 eu\n17 février 507 eu\n\n 6 mars 2484 eu 16 mars 494 eu 5 avril 2484 eu\n18. avril 473 eu 5 mai 2484 eu\n7mai357eu\n5 juin 2484 eu 16juin 1539eu\n5 juillet 928 eu\n5 septembre 2440 eu 5 octobre 1221 eu\n6 novembre 1331 eu 5 décembre 1216 eu\nTotal 26455 eu\n', '', 0),
(106, 100, '', '', 0),
(107, 101, '', '', 0),
(108, 102, '', '', 0),
(109, 103, 'Carte avantage adulte Mumu\nN° Carte : 290901 08 970271525', '', 0),
(110, 104, 'СЕЕ\nnuméro 121552\nCEE 750034951', '', 0),
(111, 105, 'Hospitalisation maman prise en charge mutuelle\nnum Finess de l\'établissement 750000523 code DMT\nnum de fax\ntype d\'hospitalisation\n0144123419 fax recouvrement@ghpsj.fr\n63128 numéro prise en charge biopsie\nInter Mutuelle Assistance tel 0970820692 ref dossier F21374009\nref dossier F21457018', '', 0),
(112, 106, '', '', 0),
(113, 107, '\nApple Helena1105\nENT mon lycée Helena20052005', '', 0),
(114, 108, 'Canal +\nMurie123456!zcxvfxzvzxv', '', 0),
(115, 109, 'pourquoi quitter votre poste ?\npour plusieurs raisons\nje suis a l\'écoute du marché, je postule a\ndes offres qui me plaisent\nparticulièrement car mon je suis bien dans mon poste aujourd\'hui, mais j\'ai fait le tour\nde mon poste, j\'aime me donner des challenges(concours en 2019) et j\'aimerais\nfaire 1gap salarial 28000 ke annuel\n33000 ke annuel\nquestions sur I INRA sur le poste\nqualités\nj\'aime le travail d\'équipe, bon\na lecoute, solaire et je suis rigoureuse (dans mon travail je m\'adresse à des\ninterlocuteur différents tels que\nrelationnel et\n\n enseignants chercheurs, étudiants,\ndoyens, directrice de labo )et ej fais en sorte de m\'organiser pour respecter les délais et demandes, en utilisant les outils à ma disposition\njai eu de très bons retours de mes\nsupérieurs et suite à l\'obtention de mon\nconcours en 2019, j\'ai été affecté d Evry, ils sont venus m e rechercher\nje sais m\'adapter selon la situation et l\'interlocuteur, c\'est à dire faire preuve de rondeurs ou\nau contraire savoir s\'imposer\ndéfauts\nje m\'impose bien de manière individuelle, en revanche j\'ai plus de mal à me mettre\nen avant dabs 1groupe pour proposer mes idées\nj\'ai besoin que les projets avancent et soient clôturés rapidement, or souvent je\n\n suis obliger de relancer mes interlocuteurs, et chose qui peut m\'agacer mais je pense avoir pris du recul sur ge sujet et je comprends que cette situation est logique, et que mes interlocuteurs ont également leurs contraintes\nquelles initiatives avez vous pris dans votre travail ?\nnous n\'avons pas une marche de\nmanœuvre énorme, mais j\'essaie d améliorer la vie de mon service en\nmettant en place des fichiers partages et en organisant des événements très\nappréciésdd\nd', '', 0),
(116, 110, 'Virements vers DRE\n19juin. 5000eu 21 juin. 1500 eu 12 juillet 3800 eu 25 juillet 3500 eu', '', 0),
(117, 111, 'GEI\nlogin 024051\nMumu2304022101!!', '', 0),
(118, 112, 'Mumu 50 ans\nAnniv Mumu invités Fred et Mumu 2 Johanna et Antoine 2 Vincent et Louise 2 Héléna 1\nAttard 2. 200 eu Germain 2. 200 eu\nBougot 2. 200 eu Cohen 2. 200 eu\nMeriau 1. 100 eu\nSabine 2. 100 eu\nReynaldo 2. 60 eu +fleurs\nJoelle et Christophe 2. 100 eu Karine et Arnaud 2. 50 eu\nIsabelle et patrice 2. 100 eu\n\n Valérie et Olivier 2. 60 eu\nMes parents 2. 200 eu Estelle 2 80 eu\nSteve 0. 80 eu Vanessa et Fafa 2 box\nKamel et Christelle 2. 120 eu Tanguy et Karima 2. 80 eu\nValentin 1\nTotal 39\nTable 1\nBougot germain cohen attard Manu 9\nTable 2\nKarine joelle Isabelle val = 8\n\n Table 3\nPapa est-elle Vanessa nous 8=\nTable 4\nReynaldo sabine Kamel tanguy =8\nTable 5\nNana Vincent Valentin Héléna =6\n\n39', '', 0),
(119, 113, 'Universite Paris-Saclay Héléna\nMot de passe ENT Helena2304022101!\nZimbra Helena2304022101!\nÉtudiant numéro 22312712\nMicrosoft Helena\nHberthault9@gmail.com Helena2304022101!', '', 0),
(120, 114, 'Num Securité Sociale\nFred 16611751145887\nVincent 100129202316504\nHéléna 205119202301339', '', 0),
(121, 115, 'PAPA et MAMAN\n1/ amelie maman 247079935105073\nRachel1508\n2 / EDF\nRachelbitan4@gmail.com 2112manahe!\n3/ ара Rachelbitan4@gmail.com Rachel2607\n4/ identifiant Banque postale 3005700964\n5/ Via Santé\nRachelbitan4@gmail.com 2112.Manahe\n\n 6/ samuelbitan92@gmail.com\n7/ macif 1663851 2112Manahe!\n8/ centre du sein Centredusein@ghpsj.fr\n9/ impôt. Gouv 2112Manahe!!\n10/ FRE Connexion à mon espace\n11/fbx28267427 Rachel1508!!\nWifi Freebox-1C1EDE\ncarchari&-togula63-bieria-protegebat8\n\n 13/\nPapa\nAujourd\'hui c\'est\nton anniversaire, tu aurais eu 75 ans et d\'habitude je réfléchis au\ncadeau que je vais t\'offrir... c\'est la 1ere\nannée où li n\'y en aura pas car tu n\'es plus parmis nous. 4 mois et demi que tu nous\nas quitté, j\'y crois sans ycroire. En écoutant en boucle tes messages vocaux,\nta voix est si belle quand tu me dis : Bonjour m a fille .......\nTu étais en pleine forme, toujours là pour ta famille et en 3 jours tu es parti, une saloprie s\'est emparée de toi, et m\'a pris\nmon papa.\nTu me manques énormément, je pense\ntoujours à toi même lorsque je suis concentrée sur autre chose.\nTu as laissé un grand vide dans ma vie, mais tu resteras à tout jamais dans mon\n\n cœur et dans ma tête mon papa chéri C\nJ\'aurais tellement aimé que tu sois encore quelques années auprès de nous.\nTu ne connaîtras pas ton arrière petite fille,\nmais on lui parlera de toi et elle te découvrira à travers des photos.\nJe te serais toujours reconnaissante de l\'éducation que tu nous as donnée à\nEstelle et moi, tes valeurs, ta droiture, ta\nbienveillance, ta sincérité, ton courage et ta pudeur ...\nJ\'oubliais, tu\nétais aussi\nun super papi et tes 5petits enfants seront d\'accord avec moi !\nJ \' e s p è r e q u e ut e s b i e n l à o ù ut e s j e n e t e vois pas mais je sais que tu veilles sur\nnous, et t\'inquiète pas nous nous occupons de maman au mieux. Та minette\nAvec tout mon amour\n\n Toute la famille se joint à moi pour te dire que l\'on t\'aime fort\n14/ Saveurs et vie maman Livraison lundi et jeudi\n15/ urssaf direct\nRachelbitan4@gmail.com 2112.Manahe!\nOu 2112Manahe!\n1 mois papa\nDimanche 18 février seouda et cimetière', '', 0),
(122, 116, 'PAPA et MAMAN\n1/ amelie maman 247079935105073\nRachel1508\n2 / EDF\nRachelbitan4@gmail.com 2112manahe!\n3/ ара Rachelbitan4@gmail.com Rachel2607\n4/ identifiant Banque postale 3005700964\n5/ Via Santé\nRachelbitan4@gmail.com 2112.Manahe\n\n 6/ samuelbitan92@gmail.com\n7/ macif 1663851 2112Manahe!\n8/ centre du sein Centredusein@ghpsj.fr\n9/ impôt. Gouv 2112Manahe!!\n10/ FRE Connexion à mon espace\n11/fbx28267427 Rachel1508!!\nWifi Freebox-1C1EDE\ncarchari&-togula63-bieria-protegebat8\n\n 13/\nPapa\nAujourd\'hui c\'est\nton anniversaire, tu aurais eu 75 ans et d\'habitude je réfléchis au\ncadeau que je vais t\'offrir... c\'est la 1ere\nannée où li n\'y en aura pas car tu n\'es plus parmis nous. 4 mois et demi que tu nous\nas quitté, j\'y crois sans ycroire. En écoutant en boucle tes messages vocaux,\nta voix est si belle quand tu me dis : Bonjour m a fille .......\nTu étais en pleine forme, toujours là pour ta famille et en 3 jours tu es parti, une saloprie s\'est emparée de toi, et m\'a pris\nmon papa.\nTu me manques énormément, je pense\ntoujours à toi même lorsque je suis concentrée sur autre chose.\nTu as laissé un grand vide dans ma vie, mais tu resteras à tout jamais dans mon\n\n cœur et dans ma tête mon papa chéri C\nJ\'aurais tellement aimé que tu sois encore quelques années auprès de nous.\nTu ne connaîtras pas ton arrière petite fille,\nmais on lui parlera de toi et elle te découvrira à travers des photos.\nJe te serais toujours reconnaissante de l\'éducation que tu nous as donnée à\nEstelle et moi, tes valeurs, ta droiture, ta\nbienveillance, ta sincérité, ton courage et ta pudeur ...\nJ\'oubliais, tu\nétais aussi\nun super papi et tes 5petits enfants seront d\'accord avec moi !\nJ \' e s p è r e q u e ut e s b i e n l à o ù ut e s j e n e t e vois pas mais je sais que tu veilles sur\nnous, et t\'inquiète pas nous nous occupons de maman au mieux. Та minette\nAvec tout mon amour\n\n Toute la famille se joint à moi pour te dire que l\'on t\'aime fort\n14/ Saveurs et vie maman Livraison lundi et jeudi\n15/ urssaf direct\nRachelbitan4@gmail.com 2112.Manahe!\nOu 2112Manahe!\n1 mois papa\nDimanche 18 février seouda et cimetière', '', 0),
(123, 117, 'Copro verrières\nsoumis au régime légal de copropriété ce serait bien d\'en faire un\nfaire une ag si travaux pv d ag\nmodèle qu\'elle va nous envoyer (projet) convocation avec récépissé\nqu\'il autorise (le commerçant serrurerie) des courriers électroniques\ndemander à Mr roux l\'adresse mail du commerçant\nagence nationale des copropriétaires\nil a juste vocation de diviser son immeuble c pas limité\n', '', 0),
(124, 118, 'Bus\n18 janvier 23h49\n19 janvier 00h20\n23h47\n20 janvier 7h41 17h48\n22h47\n21 janvier 23h47\n22 janvier 00h17\n00h48 16h25\n\n 7 février\n17h20 à accélèré sur le dis d\'âne\n8 février\n7h55 bus trop rapide\n24 mars\n9h17 trop trop rapide\n27 mai\n00h20 trop trop rapide', '', 0),
(125, 119, 'Plaque immatriculation véhicule\nSociétaire DRE 12982937\nImmatriculation expert CW752ER\nImmatriculation Ford DM144XF\nlon\nDR 029RE\n208\nF 776 CS', '', 0),
(126, 120, 'Plaque immatriculation véhicule\nSociétaire DRE 12982937\nImmatriculation expert CW752ER\nImmatriculation Ford DM144XF\nlon\nDR 029RE\n208\nF 776 CS', '', 0),
(127, 121, ' A rembourser maman 953 eu\n200 Virement le 12 dec\n100 virement le 20 dec\n150 virement le 20 déc (anniv Vincent)\n100 espèces le 24 déc 20 eu Jacques cartier 150 virement le 28 déc 25 eu amazon', '', 0),
(128, 122, ' A rembourser maman 953 eu\n200 Virement le 12 dec\n100 virement le 20 dec\n150 virement le 20 déc (anniv Vincent)\n100 espèces le 24 déc 20 eu Jacques cartier 150 virement le 28 déc 25 eu amazon', '', 0),
(129, 123, 'Banque\n55983387 55973672\n4304 h 3324 f 3468 casto\n5328 m 7755 casto\n52512359\n39261026\nCE 750034951\nsg Helena 77191967\nCarte 0211 Héléna 2333\n', '', 0),
(130, 124, 'Carte avantage adulte Mumu\nN° Carte : 290901 08 970271525', '', 0),
(131, 125, 'Num adhérent \n3304778', '', 0),
(132, 129, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_532138.jpg', 0),
(133, 130, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_268170.jpg', 0),
(134, 131, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_902267.jpg', 0),
(135, 132, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_707232.jpg', 0),
(136, 133, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_991963.jpg', 0),
(137, 134, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_222687.jpg', 0),
(138, 136, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_331575.jpg', 0),
(139, 137, 'Local Host', 'http://127.0.0.1:18011/get-image/1/1_note_679818.jpg', 0),
(141, 139, 'Local Host', 'http://127.0.0.1:18011/get-image/39/39_note_970355.jpg', 0),
(142, 140, 'ggagagagagagagagagagagag', NULL, 0),
(143, 141, 'edeasease', NULL, 0),
(144, 142, 'dadase', NULL, 0),
(145, 143, 'bvjvvjh', NULL, 0),
(146, 144, 'ewewewq', NULL, 0),
(147, 145, 'hhah123', NULL, 0),
(148, 146, 'hhah123sa', NULL, 0),
(149, 148, 'As', NULL, 0),
(151, 150, 'Local Host', 'http://samnote.mangasocial.online/get-image/56/56_note_625150.jpg', 0),
(152, 151, 'Assassin', NULL, 0),
(153, 152, 'Local Host', 'http://samnote.mangasocial.online/get-image/56/56_note_902451.jpg', 0),
(154, 153, 'Local Host', 'http://samnote.mangasocial.online/get-image/56/56_note_917613.jpg', 0),
(155, 154, 'đasadsadsadsa', NULL, 0),
(156, 157, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_496587.jpg', 0),
(157, 158, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_236232.jpg', 0),
(158, 159, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_702945.jpg', 0),
(159, 160, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_723775.jpg', 0),
(160, 161, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_284877.jpg', 0),
(161, 162, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_401470.jpg', 0),
(162, 163, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_982877.jpg', 0),
(163, 164, 'Local Hostfdsgsdggdsgdsgds', 'http://samnote.mangasocial.online/get-image/56/56_note_179416.jpg', 0),
(164, 165, '123434', 'http://samnote.mangasocial.online/get-image/56/56_note_774343.jpg', 0),
(165, 166, 'sdsadsadsa', NULL, 0),
(166, 167, 'sdsadsadsa', NULL, 0),
(167, 168, 'dsadsadsa', NULL, 0),
(168, 169, 'dsadsadsa', NULL, 0),
(169, 170, 'dsadsadsa23', NULL, 0),
(170, 171, 'dsadsadsa23', NULL, 0),
(171, 172, '123434', 'http://samnote.mangasocial.online/get-image/56/56_note_309785.jpg', 0),
(172, 173, 'tuysn', NULL, 0),
(173, 174, 'sd', NULL, 0),
(175, 176, 'Có', NULL, 0),
(176, 177, 'Wip', NULL, 0),
(178, 179, 'njnjnj', NULL, 0),
(180, 181, 'a', NULL, 0),
(183, 183, 'sdâsasasasa', NULL, 0),
(193, 189, 'Wow', NULL, 0),
(206, 199, 'hihi', NULL, 1),
(207, 199, 'hehe', NULL, 1),
(213, 203, 'xbb', NULL, 0),
(224, 204, 'hihie', NULL, 0),
(225, 204, 'hehe', NULL, 1),
(226, 204, 'we', NULL, 1),
(227, 208, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_972199.jpg', 0),
(228, 209, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_103459.jpg', 0),
(229, 210, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_203324.jpg', 0),
(232, 213, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_211724.jpg', 0),
(233, 214, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_685091.jpg', 0),
(234, 215, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_953648.jpg', 0),
(235, 216, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_426627.jpg', 0),
(236, 217, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_765095.jpg', 0),
(237, 218, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_234735.jpg', 0),
(238, 219, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_622434.jpg', 0),
(239, 220, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_697520.jpg', 0),
(240, 221, 'hjhj', NULL, 1),
(241, 221, '233df', NULL, 1),
(242, 222, 'hihie', NULL, 1),
(243, 222, 'hehe', NULL, 1),
(244, 223, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_836606.jpg', 0),
(245, 224, 'test121212121212212121', 'http://samnote.mangasocial.online/get-image/58/58_note_248570.jpg', 0),
(246, 225, '123434', 'http://samnote.mangasocial.online/get-image/56/56_note_858196.jpg', 0),
(247, 226, '123434', 'http://samnote.mangasocial.online/get-image/56/56_note_976755.jpg', 0),
(248, 227, 'test', 'http://samnote.mangasocial.online/get-image/58/58_note_484908.jpg', 0),
(249, 228, 'test121212121212212121', 'http://samnote.mangasocial.online/get-image/58/58_note_248669.jpg', 0),
(250, 229, 'test121212121212212121', 'http://samnote.mangasocial.online/get-image/58/58_note_484075.jpg', 0),
(251, 230, 'test121212121212212121', 'http://samnote.mangasocial.online/get-image/58/58_note_824881.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `folders`
--

CREATE TABLE `folders` (
  `id` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `nameFolder` text DEFAULT NULL,
  `createAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `folders`
--

INSERT INTO `folders` (`id`, `idUser`, `nameFolder`, `createAt`) VALUES
(1, 1, 'folder1.1', '2023-11-03 13:57:26');

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `idGroup` int(11) NOT NULL,
  `name` text NOT NULL,
  `describe` text DEFAULT NULL,
  `linkAvatar` text DEFAULT NULL,
  `idOwner` int(11) NOT NULL,
  `createAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `groups`
--

INSERT INTO `groups` (`idGroup`, `name`, `describe`, `linkAvatar`, `idOwner`, `createAt`) VALUES
(1, 'myGroup', 'NiceOne', NULL, 8, '2023-11-27 22:19:06'),
(2, 'myGroup2', 'hello', NULL, 9, '2023-11-28 14:27:15'),
(3, 'bap', 'sfgfgf', NULL, 33, '2023-12-28 09:37:37'),
(4, 'bao', 'bao123', NULL, 33, '2023-12-28 09:38:26'),
(5, 'bao3', '1356gdf', NULL, 33, '2023-12-28 09:43:35'),
(6, 'zxzvx', 'zxvzxv', NULL, 52, '2024-01-12 11:35:05');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `idMember` int(11) NOT NULL,
  `idGroup` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `role` varchar(50) NOT NULL DEFAULT 'Member',
  `createAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`idMember`, `idGroup`, `idUser`, `role`, `createAt`) VALUES
(1, 1, 2, 'Member', '2023-11-27 22:19:06'),
(2, 1, 8, 'Owner', '2023-11-27 22:19:06'),
(3, 2, 8, 'Member', '2023-11-28 14:27:15'),
(4, 2, 9, 'Owner', '2023-11-28 14:27:15'),
(5, 3, 1, 'Member', '2023-12-28 09:37:37'),
(6, 3, 33, 'Owner', '2023-12-28 09:37:37'),
(7, 4, 33, 'Owner', '2023-12-28 09:38:26'),
(8, 5, 33, 'Owner', '2023-12-28 09:43:35'),
(9, 6, 10, 'Member', '2024-01-12 11:35:05'),
(10, 6, 52, 'Owner', '2024-01-12 11:35:05');

-- --------------------------------------------------------

--
-- Table structure for table `nbnotes`
--

CREATE TABLE `nbnotes` (
  `id` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `nbnotes` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nbnotes`
--

INSERT INTO `nbnotes` (`id`, `idUser`, `nbnotes`) VALUES
(7, 1, 25),
(10, 2, 32),
(16, 4, 1),
(20, 7, 5),
(21, 6, 6),
(22, 8, 11),
(23, 11, 4),
(24, 12, 1),
(25, 17, 2),
(26, 10, 1),
(27, 23, 1),
(28, 27, 1),
(29, 28, 1),
(30, 30, 1),
(31, 33, 5),
(32, 39, 2),
(33, 45, 1),
(35, 48, 28),
(92, 56, 19),
(93, 58, 14);

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `idNote` int(11) NOT NULL,
  `idFolder` int(11) DEFAULT NULL,
  `idUser` int(11) NOT NULL,
  `idGroup` int(11) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `pinned` tinyint(1) NOT NULL DEFAULT 0,
  `dueAt` datetime DEFAULT NULL,
  `r` int(11) NOT NULL,
  `g` int(11) NOT NULL,
  `b` int(11) NOT NULL,
  `a` float NOT NULL,
  `lock` varchar(200) DEFAULT 'true',
  `notePublic` int(11) DEFAULT NULL,
  `metaData` text DEFAULT NULL,
  `remindAt` datetime DEFAULT NULL,
  `doneNote` tinyint(1) NOT NULL DEFAULT 0,
  `inArchived` tinyint(1) NOT NULL DEFAULT 1,
  `createAt` datetime NOT NULL,
  `updateAt` datetime NOT NULL,
  `linkNoteShare` text NOT NULL,
  `view` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notes`
--

INSERT INTO `notes` (`idNote`, `idFolder`, `idUser`, `idGroup`, `type`, `title`, `pinned`, `dueAt`, `r`, `g`, `b`, `a`, `lock`, `notePublic`, `metaData`, `remindAt`, `doneNote`, `inArchived`, `createAt`, `updateAt`, `linkNoteShare`, `view`) VALUES
(1, NULL, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-03 13:40:13', '2023-11-03 13:40:13', '123', 0),
(2, NULL, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-03 13:41:44', '2023-11-03 13:41:44', '123', 0),
(3, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 13:18:07', 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2024-01-19 13:18:07', '2024-01-31 15:53:52', '123', 14),
(5, NULL, 1, NULL, 'text', 'note 1', 0, NULL, 225, 202, 250, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-06 11:51:06', '2023-11-06 11:51:06', 'https://thinkdiff', 3),
(6, NULL, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:35:19', '2023-11-08 10:35:19', '123', 4),
(7, NULL, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:35:40', '2023-11-08 10:35:40', '', 4),
(8, NULL, 1, NULL, 'checklist', 'MyNote', 1, '2022-03-08 11:22:00', 1, 2, 3, 4, NULL, 1, NULL, NULL, 0, 0, '2023-11-08 10:36:08', '2023-11-29 23:38:06', '', 0),
(9, NULL, 1, NULL, 'checklist', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:36:38', '2023-11-08 10:36:38', '', 0),
(10, 1, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:37:35', '2023-11-08 10:37:35', '', 4),
(11, 1, 1, NULL, 'checklist', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:37:40', '2023-11-08 10:37:40', '', 0),
(12, 1, 1, NULL, 'checklist', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:50:42', '2023-11-08 10:50:42', '', 0),
(13, 1, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:51:01', '2023-11-08 10:51:01', '', 0),
(14, 1, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:52:08', '2023-11-08 10:52:08', '', 4),
(15, 1, 1, NULL, 'text', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 10:52:27', '2023-11-08 10:52:27', '', 4),
(16, 1, 1, NULL, 'checklist', 'd-b=a', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:01:08', '2023-11-08 11:01:08', '', 0),
(17, 1, 1, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:13:17', '2023-11-08 11:13:17', '', 0),
(18, 1, 1, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:14:16', '2023-11-08 11:14:16', '', 0),
(19, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:18:23', '2023-11-08 11:18:23', '', 0),
(20, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:19:19', '2023-11-08 11:19:19', '', 0),
(21, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:31:24', '2023-11-08 11:31:24', '', 0),
(22, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:46:06', '2023-11-08 11:46:06', '', 0),
(23, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:46:20', '2023-11-08 11:46:20', '', 0),
(24, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:46:57', '2023-11-08 11:46:57', '', 0),
(25, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:47:17', '2023-11-08 11:47:17', '', 0),
(26, 1, 2, NULL, 'checklist', '8/11/2023', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:51:16', '2023-11-08 11:51:16', '', 0),
(27, 1, 2, NULL, 'checklist', 'checklist1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:52:38', '2023-11-08 11:52:38', '', 0),
(28, 1, 2, NULL, 'checklist', 'checklist1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:54:48', '2023-11-08 11:54:48', '', 0),
(29, 1, 2, NULL, 'text', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:55:23', '2023-11-08 11:55:23', '', 4),
(30, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 11:55:54', '2023-11-08 11:55:54', '', 0),
(31, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 13:39:39', '2023-11-08 13:39:39', '', 0),
(32, 1, 2, NULL, 'image', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 13:43:30', '2023-11-08 13:43:30', '', 6),
(33, 1, 2, NULL, 'image', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:30:48', '2023-11-08 14:30:48', '', 6),
(34, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:30:59', '2023-11-08 14:30:59', '', 0),
(35, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:34:11', '2023-11-08 14:34:11', '', 0),
(36, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:36:26', '2023-11-08 14:36:26', '', 0),
(37, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:38:05', '2023-11-08 14:38:05', '', 0),
(38, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 14:38:22', '2023-11-08 14:38:22', '', 0),
(39, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:08:22', '2023-11-08 15:08:22', '', 0),
(40, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:09:27', '2023-11-08 15:09:27', '', 0),
(41, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:09:55', '2023-11-08 15:09:55', '', 0),
(42, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:11:04', '2023-11-08 15:11:04', '', 0),
(43, 1, 2, NULL, 'checklist', '1.1', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:12:08', '2023-11-08 15:12:08', '', 6),
(44, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:13:14', '2023-11-08 15:13:14', '', 6),
(45, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-08 15:28:18', '2023-11-08 15:28:18', '', 7),
(46, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-09 21:00:21', '2023-11-09 21:00:21', '', 7),
(47, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-15 13:36:09', '2023-11-15 13:36:09', '', 7),
(49, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-15 15:50:30', '2023-11-15 15:50:30', '', 7),
(50, 1, 2, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-15 15:53:02', '2023-11-15 15:53:02', '', 7),
(51, NULL, 4, NULL, 'text', 'note 1', 0, NULL, 225, 202, 250, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-16 12:26:30', '2023-11-16 12:26:30', 'https://thinkdiff', 8),
(53, 1, 1, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-16 15:38:41', '2023-11-16 15:38:41', '', 8),
(54, 1, 1, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-16 15:44:24', '2023-11-16 15:44:24', '', 9),
(55, 1, 1, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 0, '2023-11-27 15:08:45', '2023-11-27 15:08:45', '', 0),
(56, 1, 1, NULL, 'checklist', 'Hello', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 13:34:45', '2023-11-30 14:51:12', '535B08', 8),
(57, 1, 1, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 13:36:14', '2023-11-30 13:36:14', '', 8),
(58, 1, 1, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 13:38:01', '2023-11-30 13:38:01', '', 8),
(59, 1, 2, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 13:40:25', '2023-11-30 13:40:25', '', 8),
(60, 1, 7, NULL, 'text', 'dog', 0, NULL, 211, 239, 130, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 15:53:21', '2023-11-30 15:53:21', '', 8),
(61, 1, 6, NULL, 'text', 'note1', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 16:17:33', '2023-11-30 16:17:33', '', 9),
(62, 1, 6, NULL, 'text', 'sylae Fred2311', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 16:31:09', '2024-02-16 13:44:41', '', 13),
(63, 1, 7, NULL, 'checklist', 'assassin', 0, NULL, 255, 255, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2023-11-30 16:39:24', '2023-11-30 16:39:24', '', 0),
(64, 1, 1, NULL, 'text', 'ádasd', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 17:02:43', '2023-11-30 17:02:43', '', 9),
(65, 1, 1, NULL, 'text', 'test1', 0, NULL, 224, 252, 219, 1, NULL, 0, NULL, NULL, 0, 1, '2023-11-30 17:05:25', '2023-11-30 17:11:50', '', 8),
(66, 1, 7, NULL, 'text', 'sad as', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 17:17:05', '2023-11-30 17:17:05', '', 9),
(67, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-11-30 23:30:45', '2023-11-30 23:30:45', '', 8),
(68, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:37:32', '2023-12-01 13:37:32', '', 8),
(69, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:37:55', '2023-12-01 13:37:55', '', 8),
(70, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:38:53', '2023-12-01 13:38:53', '', 8),
(71, 1, 8, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:45:15', '2023-12-01 13:45:15', '', 0),
(72, 1, 8, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:45:41', '2023-12-01 13:45:41', '', 0),
(73, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 13:45:50', '2023-12-01 13:45:50', '', 8),
(74, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 14:00:41', '2023-12-01 14:00:41', '1234', 8),
(75, 1, 8, NULL, 'checklist', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 14:03:35', '2023-12-01 14:03:35', '1234', 0),
(76, 1, 8, NULL, 'text', 'test check list', 0, NULL, 224, 252, 219, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 14:03:43', '2023-12-01 14:03:43', '1234', 8),
(77, 1, 8, NULL, 'text', 'test', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-01 14:48:13', '2023-12-01 14:48:13', '', 8),
(78, 1, 11, NULL, 'text', 'Celebrity Millennial ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-02 02:37:10', '2023-12-02 02:37:10', '', 10),
(79, 1, 11, NULL, 'text', 'Air France Airlines', 0, NULL, 250, 226, 140, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-02 02:46:05', '2023-12-02 02:46:05', '', 10),
(80, 1, 11, NULL, 'text', 'Sao Brazil', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-02 03:02:46', '2023-12-02 03:02:46', '', 10),
(81, 1, 11, NULL, 'checklist', 'Vaccination information ', 0, NULL, 255, 255, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-02 03:22:45', '2023-12-02 03:22:45', '', 0),
(82, 1, 12, NULL, 'text', 'Rezepte ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-03 16:09:25', '2023-12-03 16:09:25', '', 8),
(83, 1, 17, NULL, 'checklist', 'Meds I Need Refilled', 0, NULL, 255, 255, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2023-12-17 10:45:25', '2023-12-17 10:45:25', '', 0),
(84, 1, 17, NULL, 'checklist', 'Goals To Discuss With New PCP', 0, NULL, 255, 255, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-19 03:36:16', '2023-12-19 03:36:16', '', 0),
(85, 1, 10, NULL, 'text', 'sylae Fred2311', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-22 11:17:26', '2024-02-16 13:44:28', '', 13),
(86, 1, 23, NULL, 'text', 'thứ 2', 1, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-22 11:18:12', '2023-12-22 11:38:22', '', 8),
(87, 1, 27, NULL, 'text', 'KẾ HOẠCH TÀI CHÍNH', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-24 08:22:34', '2023-12-24 08:22:34', '', 8),
(88, 1, 28, NULL, 'text', 'النشاط الداخلي', 0, NULL, 255, 188, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2023-12-24 16:36:36', '2024-01-31 23:55:49', '', 0),
(89, 1, 30, NULL, 'text', 'Passwords', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-27 08:47:06', '2023-12-27 08:47:06', '', 11),
(90, 1, 33, NULL, 'text', '', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-28 16:01:01', '2023-12-28 16:01:01', '', 8),
(91, 1, 33, NULL, 'text', 'jhjhjhjh', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-28 17:17:11', '2024-02-01 12:18:58', '', 10),
(92, 1, 33, NULL, 'text', 'fhjsdbfs', 0, NULL, 165, 239, 130, 1, NULL, 1, NULL, NULL, 0, 1, '2023-12-28 17:17:42', '2024-01-31 21:19:26', '', 10),
(93, 1, 33, NULL, 'text', 'kskjfhksdfksd', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2023-12-28 17:31:42', '2024-02-02 11:57:25', '6042A1', 9),
(94, 1, 33, NULL, 'text', 'sylae Fred2311', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2023-12-29 16:14:23', '2024-02-16 13:44:24', '8759B4', 13),
(95, 1, 39, NULL, 'text', 'test note 123', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-04 16:57:20', '2024-02-02 11:21:31', '1EF58E', 9),
(96, 1, 39, NULL, 'text', 'test note 2', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-04 20:30:44', '2024-02-01 00:05:02', '', 0),
(97, 1, 45, NULL, 'text', 'knuddel', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-07 23:20:36', '2024-02-02 14:32:12', 'D6244D', 9),
(98, 1, 48, NULL, 'text', 'URSSAF DRE', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 01:13:29', '2024-01-10 01:13:29', '', 0),
(99, 1, 48, NULL, 'text', 'URSSAF DRE', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 01:13:30', '2024-01-10 01:13:30', '', 0),
(100, 1, 48, NULL, 'text', ' secrétaire@mn-parissud.com 0146744190', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:38:59', '2024-01-10 01:38:59', '', 11),
(101, 1, 48, NULL, 'text', 'Num Fiscal Vincent 3030716268307', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-10 01:39:29', '2024-02-16 10:42:28', 'C75610', 14),
(102, 1, 48, NULL, 'text', 'Num Fiscal Vincent 3030716268307', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 01:39:46', '2024-01-10 01:39:46', '', 0),
(103, 1, 48, NULL, 'text', 'Mumu avantage adulte', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-10 01:41:15', '2024-02-02 16:41:25', '1F37AD', 13),
(104, 1, 48, NULL, 'text', 'CEE', 1, NULL, 130, 147, 239, 1, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:42:09', '2024-02-23 14:13:26', '', 31),
(105, 1, 48, NULL, 'text', 'Hospitalisation maman ', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 0, '2024-01-10 01:43:11', '2024-02-21 13:15:58', '61EB5E', 18),
(106, 1, 48, NULL, 'text', 'sylae Fred2311', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:43:29', '2024-01-10 01:43:29', '', 11),
(107, 1, 48, NULL, 'text', 'Helena mdr', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-10 01:45:09', '2024-02-16 18:06:47', 'E93B1A', 22),
(108, 1, 48, NULL, 'text', 'Canal + Murie123456!', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-10 01:45:29', '2024-02-16 18:06:30', '554615', 23),
(109, 1, 48, NULL, 'text', 'Entretien pro', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-10 01:46:12', '2024-02-23 11:49:51', 'C5A3D0', 41),
(110, 1, 48, NULL, 'text', 'virements DRE', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:47:14', '2024-01-10 01:47:14', '', 8),
(111, 1, 48, NULL, 'text', 'gei', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 01:47:52', '2024-02-22 19:50:05', '5ED021', 44),
(112, 1, 48, NULL, 'text', '50 ans Mumu ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:48:35', '2024-01-10 01:48:35', '', 11),
(113, 1, 48, NULL, 'text', 'UPS Héléna', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:49:05', '2024-02-23 15:49:59', '9D79D4', 11),
(114, 1, 48, NULL, 'text', 'num SS', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:49:38', '2024-02-23 15:35:28', 'F0B590', 8),
(115, 1, 48, NULL, 'text', 'Papa Maman ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 01:50:35', '2024-01-10 01:50:35', '', 11),
(116, 1, 48, NULL, 'text', 'Papa Maman ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 01:50:36', '2024-01-10 01:50:36', '', 0),
(117, 1, 48, NULL, 'text', 'copro verrieres ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:02:30', '2024-01-10 02:02:30', '', 8),
(118, 1, 48, NULL, 'text', '196', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:03:07', '2024-01-10 02:03:07', '', 8),
(119, 1, 48, NULL, 'text', 'immatriculation véhicule ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 02:04:19', '2024-01-10 02:04:19', '', 0),
(120, 1, 48, NULL, 'text', 'immatriculation véhicule ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:04:22', '2024-01-10 02:04:22', '', 12),
(121, 1, 48, NULL, 'text', 'remboursement maman', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-01-10 02:05:16', '2024-01-10 02:05:16', '', 0),
(122, 1, 48, NULL, 'text', 'remboursement maman', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:05:17', '2024-01-10 02:05:17', '', 12),
(123, 1, 48, NULL, 'text', 'Banque', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:05:55', '2024-01-10 02:05:55', '', 13),
(124, 1, 48, NULL, 'text', 'carte avantage Mumu ', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 02:08:51', '2024-01-10 02:08:51', '', 13),
(125, 1, 48, NULL, 'text', 'ENTORIA', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-10 21:01:34', '2024-01-10 21:01:34', '', 13),
(126, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 13:29:50', 255, 255, 255, 0.87, NULL, NULL, NULL, NULL, 0, 1, '2024-01-19 13:29:50', '2024-01-19 13:29:50', '1', 0),
(127, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 13:29:55', 255, 255, 255, 0.87, NULL, NULL, NULL, NULL, 0, 1, '2024-01-19 13:29:55', '2024-01-19 13:29:55', '1', 0),
(129, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 13:34:11', 255, 255, 255, 0.87, NULL, NULL, NULL, NULL, 0, 1, '2024-01-19 13:34:11', '2024-01-19 13:34:10', '1', 14),
(130, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 13:37:42', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-01-19 13:37:42', '2024-01-19 13:37:42', '1', 14),
(131, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:03:29', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-01-19 13:34:11', 0, 1, '2024-01-19 14:03:29', '2024-01-19 14:03:29', '1', 13),
(132, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:03:41', 255, 255, 255, 0.87, NULL, 0, NULL, '2024-01-19 13:34:11', 0, 1, '2024-01-19 14:03:41', '2024-01-19 14:03:40', '1', 13),
(133, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:08:11', 255, 255, 255, 0.87, NULL, 0, NULL, '2024-01-19 13:34:11', 0, 1, '2024-01-19 14:08:11', '2024-01-19 14:08:11', '1', 13),
(134, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:11:49', 255, 255, 255, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-19 14:11:49', '2024-01-19 14:11:49', '1', 13),
(136, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:37:42', 255, 255, 255, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-19 14:37:42', '2024-01-19 14:37:42', 'http://127.0.0.1:18011/share-note/136', 13),
(137, NULL, 1, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 14:41:40', 255, 255, 255, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-01-19 14:41:40', '2024-01-19 14:41:40', 'http://127.0.0.1:18011/share-note/137', 13),
(139, NULL, 39, NULL, 'image', 'Devil May Cry', 0, '2024-01-19 15:28:07', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-01-19 13:34:11', 0, 1, '2024-01-19 15:28:07', '2024-01-19 15:28:07', 'http://127.0.0.1:18011/share-note/139', 14),
(140, 1, 56, NULL, 'text', 'sylae Fred2311sdgdsgdgsdgsdgsdgsagagagagag', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-16 13:42:17', '2024-02-23 15:30:55', 'FD7A0D', 13),
(141, 1, 56, NULL, 'text', 'okee123', 0, '2024-02-18 00:20:00', 130, 147, 239, 1, NULL, 0, NULL, '2024-02-16 00:20:00', 0, 1, '2024-02-16 13:44:04', '2024-02-27 11:35:37', '6BBD05', 10),
(142, 1, 56, NULL, 'text', 'luc123', 0, '2024-02-17 00:00:00', 255, 125, 125, 0.87, '$pbkdf2-sha256$29000$sHbOee/9n9P6n/M.5/y/tw$Hj.5vP2.r8WJthS6FmJLJWN10k.h2wgMJhUJTeXz7TQ', 0, NULL, '2024-02-16 00:15:00', 0, 1, '2024-02-16 13:47:21', '2024-02-16 14:02:17', '765FB5', 12),
(143, 1, 56, NULL, 'image', 'okokoko', 0, '2024-02-17 00:20:00', 130, 200, 239, 1, NULL, 1, 'https://i.ibb.co/xJSD83d/banner.png', '2024-02-16 00:05:00', 0, 1, '2024-02-16 15:45:05', '2024-02-16 15:45:05', '', 12),
(144, 1, 56, NULL, 'image', 'luc13', 0, '2024-02-17 00:10:00', 255, 125, 125, 0.87, NULL, 1, 'https://i.ibb.co/94fN0sX/nestjs.png', '2024-02-16 01:05:00', 0, 1, '2024-02-16 15:56:43', '2024-02-27 12:23:14', '', 14),
(145, 1, 56, NULL, 'image', 'luc2003', 0, '2024-02-17 16:25:00', 130, 147, 239, 1, NULL, 1, 'https://i.ibb.co/c6930qb/react-native.png', '2024-02-16 02:10:00', 0, 1, '2024-02-16 16:02:28', '2024-02-16 16:02:28', '', 15),
(146, 1, 56, NULL, 'image', 'luc20035', 0, '2024-02-17 16:25:00', 130, 147, 239, 1, NULL, 1, 'https://i.ibb.co/c6930qb/react-native.png', '2024-02-16 02:10:00', 0, 1, '2024-02-16 16:03:43', '2024-02-23 22:39:22', '', 16),
(147, 1, 56, NULL, 'image', '', 0, NULL, 255, 125, 125, 0.87, NULL, 1, '', NULL, 0, 1, '2024-02-16 17:10:37', '2024-02-16 17:10:37', '', 0),
(148, 1, 7, NULL, 'text', 'abc', 0, NULL, 250, 226, 140, 1, NULL, 1, NULL, NULL, 0, 0, '2024-02-19 14:32:51', '2024-02-19 14:32:51', '', 10),
(150, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-19 14:59:57', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-19 14:59:57', '2024-02-19 14:59:57', 'http://samnote.mangasocial.online/share-note/150', 0),
(151, 1, 6, NULL, 'text', '19/2/2023', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-19 15:06:51', '2024-02-19 15:06:51', '', 22),
(152, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-19 15:32:03', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-19 15:32:03', '2024-02-19 15:32:03', 'http://samnote.mangasocial.online/share-note/152', 0),
(153, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-19 15:32:58', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-19 15:32:58', '2024-02-19 15:32:58', 'http://samnote.mangasocial.online/share-note/153', 0),
(154, 1, 56, NULL, 'image', 'dsadsahay', 0, '2024-02-20 12:00:00', 211, 239, 130, 1, NULL, 1, 'https://i.ibb.co/3BNX1ZK/vue.jpg', '2024-02-19 00:00:00', 0, 1, '2024-02-19 17:20:56', '2024-02-19 17:20:56', '', 23),
(155, 1, 56, NULL, 'image', '', 0, NULL, 255, 125, 125, 0.87, NULL, 1, '', NULL, 0, 1, '2024-02-20 09:53:49', '2024-02-20 09:53:49', '', 0),
(156, 1, 56, NULL, 'image', '', 0, NULL, 255, 125, 125, 0.87, NULL, 1, 'https://i.ibb.co/3ThkxNf/redis.png', NULL, 0, 1, '2024-02-20 10:02:52', '2024-02-20 10:02:52', '', 0),
(157, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-20 10:10:14', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-20 10:10:14', '2024-02-20 10:10:14', 'http://samnote.mangasocial.online/share-note/157', 0),
(158, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-20 10:10:53', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-20 10:10:53', '2024-02-20 10:10:53', 'http://samnote.mangasocial.online/share-note/158', 0),
(159, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-20 10:23:05', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-20 10:23:05', '2024-02-20 10:23:05', 'http://samnote.mangasocial.online/share-note/159', 0),
(160, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 10:36:31', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 10:36:31', '2024-02-21 10:36:31', 'http://samnote.mangasocial.online/share-note/160', 0),
(161, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 10:38:00', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 10:38:00', '2024-02-21 10:38:00', 'http://samnote.mangasocial.online/share-note/161', 0),
(162, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 10:38:08', 255, 255, 255, 0.877, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 10:38:08', '2024-02-21 10:38:08', 'http://samnote.mangasocial.online/share-note/162', 0),
(163, NULL, 56, NULL, 'Image', '123', 0, '2024-02-21 10:38:17', 255, 255, 255, 0.87, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 10:38:17', '2024-02-21 10:38:17', 'http://samnote.mangasocial.online/share-note/163', 0),
(164, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 11:02:51', 0, 0, 0, 0, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 11:02:51', '2024-02-21 11:02:51', 'http://samnote.mangasocial.online/share-note/164', 0),
(165, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 11:07:24', 0, 0, 0, 0, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 11:07:24', '2024-02-21 11:07:24', 'http://samnote.mangasocial.online/share-note/165', 0),
(166, 1, 56, NULL, 'image', 'okeee', 0, '2024-02-12 00:00:00', 165, 239, 130, 1, NULL, 1, 'https://i.ibb.co/LxbCqpD/php.jpg', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:14:58', '2024-02-21 11:14:58', '', 19),
(167, 1, 56, NULL, 'image', 'okeee', 0, '2024-02-12 00:00:00', 165, 239, 130, 1, NULL, 1, 'https://i.ibb.co/LxbCqpD/php.jpg', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:21:12', '2024-02-21 11:21:12', '', 23),
(168, 1, 56, NULL, 'image', 'dsdsa', 0, '2024-02-22 10:00:00', 255, 125, 125, 0.87, NULL, 1, 'https://i.ibb.co/pW5Z1zw/react-native.png', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:33:40', '2024-02-27 12:22:08', '4450FC', 25),
(169, 1, 56, NULL, 'image', 'dsdsa123', 0, '2024-02-22 10:00:00', 165, 239, 130, 1, NULL, 1, 'https://i.ibb.co/pW5Z1zw/react-native.png', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:46:27', '2024-02-21 11:46:27', '', 29),
(170, 1, 56, NULL, 'image', 'dsdsavue', 0, '2024-02-22 10:00:00', 165, 239, 130, 1, NULL, 1, 'https://i.ibb.co/RCF5tsJ/vue.jpg', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:52:29', '2024-02-27 11:30:16', '', 47),
(171, 1, 56, NULL, 'image', 'dsdsavue', 0, '2024-02-22 10:00:00', 165, 239, 130, 1, NULL, 1, 'https://i.ibb.co/RCF5tsJ/vue.jpg', '2024-02-21 00:00:00', 0, 1, '2024-02-21 11:59:51', '2024-02-23 16:02:57', '', 84),
(172, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-21 13:55:57', 0, 0, 0, 0, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-21 13:55:57', '2024-02-21 13:55:57', 'http://samnote.mangasocial.online/share-note/172', 0),
(173, 1, 58, NULL, 'text', 'tuysn', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 0, '2024-02-23 11:19:34', '2024-02-23 11:20:53', '', 2),
(174, 1, 58, NULL, 'text', 'a', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 11:43:04', '2024-02-23 11:43:04', '', 72),
(176, 1, 6, NULL, 'text', 'rice', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 13:30:30', '2024-02-23 13:30:30', '', 1),
(177, 1, 6, NULL, 'text', 'wip', 0, NULL, 165, 239, 130, 1, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 13:43:31', '2024-02-23 13:43:31', '', 1),
(179, 1, 56, NULL, 'text', 'okee1234', 0, '2024-02-24 00:00:00', 130, 239, 187, 1, NULL, 1, NULL, '2024-02-23 00:00:00', 0, 1, '2024-02-23 14:11:27', '2024-02-27 14:38:56', '', 17),
(181, 1, 58, NULL, 'text', 'ae', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 14:27:47', '2024-02-23 14:44:00', '', 90),
(182, 1, 58, NULL, 'checklist', 'd', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 14:42:59', '2024-02-23 14:42:59', '', 7),
(183, 1, 58, NULL, 'text', 'a2', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 14:48:17', '2024-02-23 14:48:17', '', 89),
(184, 1, 58, NULL, 'checklist', 'f', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 14:50:22', '2024-02-23 14:50:22', '', 6),
(185, 1, 58, NULL, 'checklist', 'd', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 14:50:45', '2024-02-23 14:50:45', '', 3),
(186, 1, 58, NULL, 'checklist', 'v', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 14:53:36', '2024-02-23 14:53:36', '', 2),
(187, 1, 58, NULL, 'checklist', 'd', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:10:19', '2024-02-23 15:10:19', '', 3),
(188, 1, 58, NULL, 'checklist', 'fd', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:11:58', '2024-02-23 15:11:58', '', 3),
(189, 1, 6, NULL, 'text', 'blur', 0, NULL, 130, 147, 239, 1, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 15:12:59', '2024-02-23 15:12:59', '', 0),
(190, 1, 58, NULL, 'checklist', 'r', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:32:59', '2024-02-23 15:32:59', '', 2),
(191, 1, 58, NULL, 'checklist', 'gh', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:35:58', '2024-02-23 15:35:58', '', 2),
(192, 1, 58, NULL, 'checklist', 'r', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:40:30', '2024-02-23 15:40:30', '', 2),
(193, 1, 58, NULL, 'checklist', 'ttt', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:47:13', '2024-02-23 15:47:13', '', 2),
(194, 1, 58, NULL, 'checklist', 'ds', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:49:53', '2024-02-23 15:49:53', '', 3),
(195, 1, 58, NULL, 'checklist', 'dsd', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 15:55:55', '2024-02-23 15:55:55', '', 2),
(196, 1, 58, NULL, 'checklist', 'ds', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 16:02:09', '2024-02-23 16:02:09', '', 2),
(197, 1, 58, NULL, 'checklist', 'sa', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 16:03:45', '2024-02-23 16:03:45', '', 5),
(198, 1, 58, NULL, 'text', 'a', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 16:07:54', '2024-02-23 16:07:54', '', 0),
(199, 1, 58, NULL, 'checklist', 'a', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 16:25:34', '2024-02-23 16:25:34', '', 69),
(200, 1, 58, NULL, 'checklist', 'ayy', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 16:27:09', '2024-02-23 16:27:09', '', 3),
(201, 1, 58, NULL, 'checklist', 'ayyiiiii', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-23 17:07:43', '2024-02-23 17:07:43', '', 10),
(202, 1, 58, NULL, 'checklist', 'yu', 0, NULL, 143, 210, 239, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-23 17:22:32', '2024-02-23 17:22:32', '', 3),
(203, 1, 58, NULL, 'text', 'yk', 0, NULL, 165, 239, 130, 0.87, NULL, 0, NULL, NULL, 0, 0, '2024-02-25 21:22:26', '2024-02-25 21:22:26', '', 1),
(204, 1, 58, NULL, 'checklist', 'ayye', 0, NULL, 255, 125, 125, 0.87, NULL, 0, NULL, NULL, 0, 1, '2024-02-26 09:39:23', '2024-02-26 09:45:34', '82926F', 56),
(205, 1, 58, NULL, 'text', 'testImg', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 09:58:58', '2024-02-26 09:58:58', '', 0),
(206, 1, 58, NULL, 'text', 'testImg', 0, NULL, 255, 125, 125, 0.87, NULL, 1, '', NULL, 0, 1, '2024-02-26 09:59:28', '2024-02-26 09:59:28', '', 0),
(207, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 10:16:49', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 10:16:49', '2024-02-26 10:16:49', 'http://samnote.mangasocial.online/share-note/207', 0),
(208, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 10:22:23', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 10:22:23', '2024-02-26 10:22:23', 'http://samnote.mangasocial.online/share-note/208', 49),
(209, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 10:37:12', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 10:37:12', '2024-02-26 10:37:12', 'http://samnote.mangasocial.online/share-note/209', 59),
(210, NULL, 58, NULL, 'image', 'Test Image1', 0, '2024-02-26 10:58:16', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 10:58:16', '2024-02-26 10:58:16', 'http://samnote.mangasocial.online/share-note/210', 56),
(213, NULL, 58, NULL, 'image', 'Test Image1', 0, '2024-02-26 13:31:42', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 13:31:42', '2024-02-26 13:31:42', 'http://samnote.mangasocial.online/share-note/213', 38),
(214, NULL, 58, NULL, 'image', 'Test Image1', 0, '2024-02-26 13:32:53', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 13:32:53', '2024-02-26 13:32:53', 'http://samnote.mangasocial.online/share-note/214', 45),
(215, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 13:33:19', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 13:33:19', '2024-02-26 13:33:19', 'http://samnote.mangasocial.online/share-note/215', 49),
(216, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 14:49:51', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 14:49:51', '2024-02-26 14:49:51', 'http://samnote.mangasocial.online/share-note/216', 41),
(217, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-26 15:05:15', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-26 15:05:15', '2024-02-26 15:05:15', 'http://samnote.mangasocial.online/share-note/217', 43),
(218, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 00:15:20', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 00:15:20', '2024-02-27 00:15:20', 'http://samnote.mangasocial.online/share-note/218', 22),
(219, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 09:51:06', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 09:51:06', '2024-02-27 09:51:06', 'http://samnote.mangasocial.online/share-note/219', 24),
(220, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 10:03:19', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 10:03:19', '2024-02-27 10:03:19', 'http://samnote.mangasocial.online/share-note/220', 24),
(221, 1, 56, NULL, 'checklist', 'lokee', 0, '2024-02-28 00:00:00', 211, 226, 140, 1, NULL, 1, NULL, '2024-02-27 00:00:00', 0, 1, '2024-02-27 12:32:24', '2024-02-27 12:32:24', '', 0),
(222, 1, 58, NULL, 'checklist', 'ayyiiiii', 0, NULL, 255, 125, 125, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 14:01:28', '2024-02-27 14:01:28', '', 8),
(223, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 14:04:56', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 14:04:56', '2024-02-27 14:04:56', 'http://samnote.mangasocial.online/share-note/223', 12),
(224, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 14:05:12', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 14:05:12', '2024-02-27 14:05:12', 'http://samnote.mangasocial.online/share-note/224', 15),
(225, NULL, 56, NULL, 'Image', 'duongluc', 0, '2024-02-27 14:07:05', 0, 0, 0, 0, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-27 14:07:05', '2024-02-27 14:07:05', 'http://samnote.mangasocial.online/share-note/225', 0),
(226, NULL, 56, NULL, 'Image', 'duongluc123', 0, '2024-02-27 14:08:48', 0, 0, 0, 0, NULL, 1, NULL, '2024-02-19 00:00:00', 0, 1, '2024-02-27 14:08:48', '2024-02-27 14:08:48', 'http://samnote.mangasocial.online/share-note/226', 0),
(227, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 14:12:36', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 14:12:36', '2024-02-27 14:12:36', 'http://samnote.mangasocial.online/share-note/227', 15),
(228, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 15:59:50', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 15:59:50', '2024-02-27 15:59:50', 'http://samnote.mangasocial.online/share-note/228', 9),
(229, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 16:00:06', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 16:00:06', '2024-02-27 16:00:06', 'http://samnote.mangasocial.online/share-note/229', 11),
(230, NULL, 58, NULL, 'image', 'Test Image', 0, '2024-02-27 16:38:33', 255, 255, 255, 0.87, NULL, 1, NULL, NULL, 0, 1, '2024-02-27 16:38:33', '2024-02-27 16:38:33', 'http://samnote.mangasocial.online/share-note/230', 6);

-- --------------------------------------------------------

--
-- Table structure for table `relationship`
--

CREATE TABLE `relationship` (
  `id` int(11) NOT NULL,
  `idSend` int(11) NOT NULL,
  `idReceive` int(11) NOT NULL,
  `relation` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `relationship`
--

INSERT INTO `relationship` (`id`, `idSend`, `idReceive`, `relation`) VALUES
(1, 1, 2, 1),
(2, 2, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `token_device`
--

CREATE TABLE `token_device` (
  `id` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `device` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenid` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `token_device`
--

INSERT INTO `token_device` (`id`, `idUser`, `device`, `tokenid`) VALUES
(1, 1, 'ios', 'hjgakjsdhgakjshdgaksjdh'),
(2, 1, 'ios', 'hjgakjsdhgakjshdgaksjdh'),
(3, 1, 'ios3', 'hjgakjsdhgakjshdgaksjdh'),
(4, 2, 'andriod', 'hjgakjsdhgakjshdgaksjdh'),
(5, 1, 'andriod2', 'hjgakjsdhgakjshdgaksjdh'),
(6, 2, 'andriod2', 'hjgakjsdhgakjshdgaksjdh');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `gmail` text NOT NULL,
  `user_name` text NOT NULL,
  `password_hash` text NOT NULL,
  `password_hash_2` text DEFAULT NULL,
  `r` int(11) DEFAULT 255,
  `g` int(11) DEFAULT 125,
  `b` int(11) DEFAULT 125,
  `a` float DEFAULT 0.87,
  `df_screen` varchar(20) DEFAULT 'Archived',
  `df_fontsize` varchar(20) DEFAULT 'Default',
  `createAt` datetime DEFAULT NULL,
  `linkAvatar` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png',
  `linkAvtprofile` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png',
  `statesLogin` tinyint(1) DEFAULT NULL,
  `last_activity_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `gmail`, `user_name`, `password_hash`, `password_hash_2`, `r`, `g`, `b`, `a`, `df_screen`, `df_fontsize`, `createAt`, `linkAvatar`, `linkAvtprofile`, `statesLogin`, `last_activity_time`) VALUES
(1, 'Nguyen Dung', 'dungnguyen2077@gmail.com', 'dungnguyen2077', '$pbkdf2-sha256$29000$3ZtzzjlnTIlRas35P.d87w$VXGXd0mM.UvawaOoMzlTjuaK7cMVNayzGVJewXnfTCg', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-03 10:28:06', 'http://0.0.0.0:18011/get-image/1/1_avatar_657404.jpg', 'http://0.0.0.0:18011/get-image/1/1_profile_489312.jpg', 1, '2024-01-19 14:00:50'),
(2, '123', 'long16072001@gmail.com', '1234', '$pbkdf2-sha256$29000$DME4h1BqDeFcSwmB0FrrvQ$Av0T/cdVtAcPre1XJ0GUvn6ACYB4aJ5jftXiJCQR3/Q', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-03 14:03:41', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(4, 'GalyDev', 'ngoclam130197@gmail.com', 'galydev', '$pbkdf2-sha256$29000$m3OOMaYU4lwLoZTynnPunQ$2WKH0aX/y0rSLX.wm5c04GKX5UDLPaFCQ2EAQQ56IsE', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-16 12:25:19', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(6, 'name', 'anhungtrnc@gmail.com', 'user_name', '$pbkdf2-sha256$29000$q5Vybm1NibF2DuEcY6zVOg$H4WfoopqJj4PdcTMSkQ9Ni2l/xTZC5sD3ADMQbMIoqw', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-23 13:52:39', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(7, 'anhungtrtt@gmail.com', 'anhungtrtt@gmail.com', 'anhungtrtt@gmail.com', '$pbkdf2-sha256$29000$ytl7r9Was1YK4fw/h7C2Ng$aI7IhOgMJLDK5bddvU4K1pookcHpFxsSzqmedkGCRgA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-23 16:09:16', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(8, 'minhlsks2', 'quockhanhlsls44@gmail.com', 'quockhanh', '$pbkdf2-sha256$29000$khJiLOWcU.r9vxdCiDGmNA$cjalBVwAlL.KxG3kjAHzoB/0k0Eur70oFuaDi6OmTFg', '$pbkdf2-sha256$29000$Tel9730PwZgTotQaoxQCwA$AOgsMBVVaeoKaLrCoAPROWf1mvNpbSjthxh0ESaT5aU', 255, 125, 125, 0.87, 'calendar', 'Default', '2023-11-27 17:28:36', 'https://i.ibb.co/dQMp4GZ/Phuong-Di-Dau.jpg', 'https://i.ibb.co/TBWrN3d/vinh-Ha-Long.jpg', 1, '2024-01-18 15:12:57'),
(9, 'duy', '19a10010294@students.hou.edu.vn', 'duymanh', '$pbkdf2-sha256$29000$GMO4N6YUonSOMQag1DrnfA$UipsTuUfN7saemFI9wfmsm6QKuznh92QANESAYsyVrc', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-11-28 14:26:11', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(10, 'janie.lin09@gmail.com', 'janie.lin09@gmail.com', 'janie.lin09@gmail.com', '$pbkdf2-sha256$29000$0BojpLQWQsgZwxhjTOkd4w$/9OIr93DTkGSdDWtE67ebnyR9msA5L3/fddZumHi0fs', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-01 12:54:20', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(11, 'mmcurry1240@outlook.com', 'mmcurry1240@outlook.com', 'mmcurry1240@outlook.com', '$pbkdf2-sha256$29000$T2nt3Xtv7V2LsfZea6211g$z1DmyF.3iAHzCLeAJvR1gs0MwY3Sf.WdBiiRBIwwg7g', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-02 02:33:55', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-16 11:21:59'),
(12, 'doc.jek55@gmail.com', 'doc.jek55@gmail.com', 'doc.jek55@gmail.com', '$pbkdf2-sha256$29000$JcTYew9hLMX4v/f.P4cQgg$4Sw50rQwM.evTCdDYALlfDNv/cQrMJhNCbniqCnFN/c', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-03 15:57:35', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(13, 'dfa', 'vubaolong2000pro@gmail.com', 'asfasfasf', '$pbkdf2-sha256$29000$.z/nfG/NuVdqzVlLyVkLQQ$1IoQe0V9kblq84jksdUWbLzTJMCuB16oS2c/aFlAM9k', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-11 22:31:42', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(14, 'benito.carrillo@gmail.com', 'benito.carrillo@gmail.com', 'benito.carrillo@gmail.com', '$pbkdf2-sha256$29000$5FyrVeodA.DcG0Po/Z9TKg$3Zgsw1rNIKupB8CUnj/nZRKzGAli1k2fktvekEc4MVA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-13 06:59:06', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(15, 'carolsmith899@aol.com', 'carolsmith899@aol.com', 'carolsmith899@aol.com', '$pbkdf2-sha256$29000$UwqhFGIM4VzrPac0BsDYOw$45.P73A0xOtEhNaVAfyyauH1slMwPE1p0fqgKCgkQNE', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-14 18:22:31', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(17, 'kelley.bxx@yahoo.com', 'kelley.bxx@yahoo.com', 'kelley.bxx@yahoo.com', '$pbkdf2-sha256$29000$nbP2ntO6t9b6/997T2kNIQ$C7HgtqVsciCCmn5TX0Ooyp6VhCHh11nDAsH3CGL6sv0', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-17 10:41:34', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(18, 'hoseinmardi_mohsen@yahoo.com', 'hoseinmardi_mohsen@yahoo.com', 'hoseinmardi_mohsen@yahoo.com', '$pbkdf2-sha256$29000$knIuxZjzHiOEEKI0xvjfuw$rMhZ15dDmfXxsenpgBqD3X5/4eYKy9qYT8FtOw7BOBA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-18 01:03:57', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(19, 'berkowitzgoldy@gmail.com', 'berkowitzgoldy@gmail.com', 'berkowitzgoldy@gmail.com', '$pbkdf2-sha256$29000$8V4rpVTqfc8ZI2QMgXAOQQ$HGqs/EtdlOFjTlFg284ZBX.cCsMDn0kfHGdwVvYfH7U', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-18 23:52:29', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(21, 'dorkaprzemek@gmail.com', 'dorkaprzemek@gmail.com', 'dorkaprzemek@gmail.com', '$pbkdf2-sha256$29000$1xrjvJdSCqE0JoSQMsZ4rw$.ocOEqK2FwNUvGXzhFELo2ATtsCfQwVSsVIjZ6bN3Tg', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-20 06:34:48', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(22, 'Thuận', 'thuannguyen21052002@gmail.com', 'thuan2105', '$pbkdf2-sha256$29000$g7C21ro35lyL0dp7jzFmbA$uqL5ForWFhz3Rr1pRAPhkXCY6IY7MHP0FG5x2YY6yNk', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-21 09:37:08', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(23, 'thuan', 'nvt210502@gmail.com', 'thuan210502', '$pbkdf2-sha256$29000$OgfgnLM2JgSgFAKAEOLcWw$Tgwxhpq2dgxsA/MM3SdbuWISHw8Et8EMzchrFagpW2I', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-21 10:00:05', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 0, '2024-01-18 15:12:57'),
(25, 'Abdou.gee.10@gmail.com', 'Abdou.gee.10@gmail.com', 'Abdou.gee.10@gmail.com', '$pbkdf2-sha256$29000$I6T03lsrZaw1hnCutVYK4Q$SbZFJk1K8SqPfq6AhnS1lGNxidHuTSVIMwZDTGyiEYA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-23 02:27:21', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(26, 'mariafelker14@gmail.com', 'mariafelker14@gmail.com', 'mariafelker14@gmail.com', '$pbkdf2-sha256$29000$6j2HEAJAqFVqrTXG.L83xg$Pib41C6/2xM3E.oZE42/Psa.x37C3IKHBattqDuBaic', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-23 17:37:36', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(27, 'vuvantrang.hn@gmail.com', 'vuvantrang.hn@gmail.com', 'vuvantrang.hn@gmail.com', '$pbkdf2-sha256$29000$1Vrr/f//X0vp/Z.zNmbsfQ$/2CtEf12h4OIazFdnREIHZVE8czhkpsvB0j6d4In7Xk', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-24 08:18:42', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(28, 'aborayanalgamdi@gmail.com', 'aborayanalgamdi@gmail.com', 'aborayanalgamdi@gmail.com', '$pbkdf2-sha256$29000$vtfaGwNACGFsLYVwbs3ZWw$HUxVBeNssLyLZ/KAu0AthptwXRGq.SN/0vtMHzawbhI', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-24 16:35:10', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(29, 'test123', 'tuananhdao2862@gmail.com', 'test123', '$pbkdf2-sha256$29000$Mub8fw.h9P7fu/e.l5Kydg$upf2.uooliEiHNMuOmLwtxuQ6iZD.HqjRi3cHoSMUTI', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-25 02:07:59', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(30, 'pfeest56@gmail.com', 'pfeest56@gmail.com', 'pfeest56@gmail.com', '$pbkdf2-sha256$29000$NiYEgPD.X6vVuteaM6a0Vg$P6wkoJwN2TuKLpzsdJlNRXZlbKmoY5sJ9Bx98ldgezI', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-27 08:22:05', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(31, 'zarembaklaus@gmail.com', 'zarembaklaus@gmail.com', 'zarembaklaus@gmail.com', '$pbkdf2-sha256$29000$cs75P0eI8T5njFEKAQDg3A$J9cRQgimk5VttfnTPQSRAPqxerltTj3CR1DRrNxcTVI', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-27 22:41:09', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(32, 'monica.rt09@gmail.com', 'monica.rt09@gmail.com', 'monica.rt09@gmail.com', '$pbkdf2-sha256$29000$m5Oy9t7b.7.3dk7JWctZ6w$m63mQI0609whm9VrHKnRdHGuw6j5w8zUnWCfwh7nqM4', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-28 03:35:22', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(33, 'thinh van bao', 'thinhvanbao312002@gmail.com', 'thinhvanbao', '$pbkdf2-sha256$29000$pRTC.L.XMoaQMkaIcU5prQ$D/xYRiB/QYt/oydmEtY87lGQ3ZnHKZwmPd1NDHggMUA', '$pbkdf2-sha256$29000$PscYA6AUImTsPUfIee99Tw$0Ib6ehQNSsKiFOuQfkQ8HjoMug9F/YyYBaO/eQIILKs', 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-28 09:34:43', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(34, 'klauszaremba@gmail.com', 'klauszaremba@gmail.com', 'klauszaremba@gmail.com', '$pbkdf2-sha256$29000$J.Tcm7O2llLKOWdMKQWAMA$VTPA7HdAC2VIq4RB1wYUfX9OJReFFCQ8E0aVbpjqLfA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-28 20:11:38', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(35, 'baronleonardo@hotmail.com', 'baronleonardo@hotmail.com', 'baronleonardo@hotmail.com', '$pbkdf2-sha256$29000$PqeUMsa4t/b.vxdi7P2fMw$kBWS5yFb5jUkfrtTV38QMSGW2DbjUPUSO6opg5vY7wg', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-29 05:58:45', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(36, 'baronleonardo1970@gmail.com', 'baronleonardo1970@gmail.com', 'baronleonardo1970@gmail.com', '$pbkdf2-sha256$29000$n9OaE6I0hnCOMSYkJARgzA$XQ3GsurZr6177DEL5ao2SZclEWG3ubnSxFSBfJ7aMcY', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-29 07:29:13', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(37, 'laviniafernandasouza@gmail.com', 'laviniafernandasouza@gmail.com', 'laviniafernandasouza@gmail.com', '$pbkdf2-sha256$29000$MgbA.J9z7h0jJISQck7pXQ$J3.lgMgks.R3hnTJceDkViAOCZmSRCY/I2vHZ4/5NgM', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2023-12-30 09:06:48', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(38, 'nikky0909@gmail.com', 'nikky0909@gmail.com', 'nikky0909@gmail.com', '$pbkdf2-sha256$29000$JMT4n5OSUso5p1TK.d/bew$QeFONfcPDKQhlJsnLuZtlAcr6hm9paF3oODfwLtLYlw', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-02 11:12:15', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(39, 'WB0301496718', 'binhhuunguyen2811@gmail.com', 'asdasd', '$pbkdf2-sha256$29000$5BwDgFBKSUmpNUaI8d4bYw$DoFxl0mplwceoKmt4GmFHzdib64MpeXTXnBuj5w2yww', '$pbkdf2-sha256$29000$OYfwXstZq7VWqrX2fq.19g$BzEWk9mgKiVHBGqAFu6UbfaPhmDHxfJAxUfhOZMuXco', 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-02 15:11:19', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-22 11:18:32'),
(40, '1397abohatm1397@gmail.com', '1397abohatm1397@gmail.com', '1397abohatm1397@gmail.com', '$pbkdf2-sha256$29000$r7XW2rsXopRyjtGaM2bMmQ$s07MRkXU4uP1uOraXBwsBvxR6wSbJFtJdrLnhggd0N4', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-04 11:01:29', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(41, 'jongwiwat2024@gmail.com', 'jongwiwat2024@gmail.com', 'jongwiwat2024@gmail.com', '$pbkdf2-sha256$29000$X.vd23uv9b7XmjMmRChljA$E2mqi9vveL4UShMhfU4vG.4QfD882/8GyPNGFuKe0No', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-05 13:53:39', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(42, 'johnsinteraction@gmail.com', 'johnsinteraction@gmail.com', 'johnsinteraction@gmail.com', '$pbkdf2-sha256$29000$zfn/fy9lzPnfuxeCUIqRcg$GN/4jCT5ZXf3dW46v16L9LfMvES1pqNKsrLUfDQ73qE', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-07 02:21:39', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(44, 'konebye2@gmail.com', 'konebye2@gmail.com', 'konebye2@gmail.com', '$pbkdf2-sha256$29000$DGFszRnDWGtN6d3bG4Nwrg$uNYE09gSZP3vsKLUguP8g1JxEBhHda0MRi0IFrUrGxQ', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-07 04:06:36', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(45, 'mariodischer@gmail.com', 'mariodischer@gmail.com', 'mariodischer@gmail.com', '$pbkdf2-sha256$29000$l5Ly3juH0Lp3bm0tBeA8Zw$iWEpvWu/3DdEe8zz866tWn2d4AxX4PlCvX0DIUHXuhs', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-07 23:16:42', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(46, 'ragonha@me.com', 'ragonha@me.com', 'ragonha@me.com', '$pbkdf2-sha256$29000$PwfAWAsBQKhVKiXEmJOydg$Iixk2WEjjCI5JAkIzY4LDQnP1DNE7ABWRc6rhcYJplQ', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-08 08:00:23', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(47, 'najimtaher84@hotmail.com', 'najimtaher84@hotmail.com', 'najimtaher84@hotmail.com', '$pbkdf2-sha256$29000$HiPknJMy5jynNAag9F7rPQ$f1HIU5dF32Bi3XDv9SsQXXq8vjLL1kpy6zB44xd0k1k', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-09 15:09:09', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(48, 'berthault04@icloud.com', 'berthault04@icloud.com', 'berthault04@icloud.com', '$pbkdf2-sha256$29000$Y4xxrvWeszYm5DynFGJszQ$zCplkPny60KpFmRRmIqVhu5li1/2.FWS1zlMsA9nefo', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-10 00:51:15', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(49, 'berthault04@gmail.com', 'berthault04@gmail.com', 'berthault04@gmail.com', '$pbkdf2-sha256$29000$E2IMIYSwdo4xhnDOee.dEw$KNuAOxPoY.OSm7aSY8QHmwtzy8ILooJxFyRQtSxfduw', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-10 01:16:34', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(50, 'asdfa', 'kwangheeheo1988@gmail.com', 'asfsaf', '$pbkdf2-sha256$29000$LcVY6/1fq5WSEiLkPEcIAQ$Sf8E26Smk8X8Ix3Lctc6Dlzq9M3.HqrERGhAgP0xWjI', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-10 22:19:32', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', NULL, '2024-01-18 15:12:57'),
(51, 'newardy@gmail.com', 'newardy@gmail.com', 'newardy@gmail.com', '$pbkdf2-sha256$29000$jjHm3HuPUaq1tjZGaK21Vg$HDoN2lPLbCLg/mFT1Hj52C5Fk7Ec0M5EcueLFk2yy40', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-11 04:40:22', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(52, 'son', 'danquantinh@gmail.com', 'ngp32', '$pbkdf2-sha256$29000$U4pxTknJeS8FYAwhpLQ2xg$LCndZAomuj72FipMotUaJ7ACaqfzmjksg68aFn7X5bg', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-01-12 11:34:23', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-01-18 15:12:57'),
(53, 'tuan', 'dinhkhactuan18@gmail.com', 'tuan22', '$pbkdf2-sha256$29000$RijFmDMGQIiR8l4rJWQsxQ$ImYbtPBvdoIa4KsMqYQfRJUrM6N2Y0YEb/a2nvUUGEA', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-02-01 13:38:04', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-01 13:38:04'),
(54, 'fall40035@gmail.com', 'fall40035@gmail.com', 'fall40035@gmail.com', '$pbkdf2-sha256$29000$IyTEuPfeW0uptRYCIOQ8hw$j1zndIh4CoRz5xa40tFFstmBEslxz8hAcUfi.1PUmQo', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-02-04 01:56:08', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-04 01:56:08'),
(55, 'mariela.houega@gmail.com', 'mariela.houega@gmail.com', 'mariela.houega@gmail.com', '$pbkdf2-sha256$29000$zDmnFOKck5KyVmqt9X4PwQ$DSXOqGKmAiM33Ny.c3/.572CUcujxp.mgVTeSRZofSE', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-02-07 17:34:45', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-07 17:34:45'),
(56, 'Duong', 'lucck131103@gmail.com', 'Van Luc', '$pbkdf2-sha256$29000$hvD.33sv5fyfcy4FQIhxrg$IcZ7w.myQ3YBWTDX.tVxtroIJcr09fxfXbw.Ruu7aKo', NULL, 255, 125, 125, 0.87, 'settings', 'Default', '2024-02-16 13:37:45', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://i.ibb.co/vk84FHW/php.jpg', 1, '2024-02-27 14:58:47'),
(57, 'so pro', 'sonnh7289@gmail.com', 'sonpro', '$pbkdf2-sha256$29000$2huDEAKAUGqtVcrZO0cohQ$JEI/Ti2WJHEFu/u4cm37uxsZAvq04K1cL9mow7IfUto', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-02-16 23:44:55', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-16 23:44:55'),
(58, 'tuyen', 'trinhtuyen1202@gmail.com', 'tuyentv', '$pbkdf2-sha256$29000$dw5hDGFMSck5Z4yxNsZ4Lw$9YOSqGkPrWEyrXtfzeMKhiLA/21SILopKcc5SN37m90', NULL, 255, 125, 125, 0.87, 'Archived', 'Default', '2024-02-23 09:53:41', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 'https://github.com/sonnh7289/python3-download/raw/main/Screenshot%202023-05-04%20at%205.33.53%20PM.png', 1, '2024-02-23 13:34:48');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chat1vs1`
--
ALTER TABLE `chat1vs1`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idRecevece` (`idReceive`);

--
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`idMes`),
  ADD KEY `idGroup` (`idGroup`);

--
-- Indexes for table `chatunknowns`
--
ALTER TABLE `chatunknowns`
  ADD PRIMARY KEY (`idMes`),
  ADD KEY `idReceive` (`idReceive`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idUser` (`idUser`),
  ADD KEY `idNote` (`idNote`);

--
-- Indexes for table `datas`
--
ALTER TABLE `datas`
  ADD PRIMARY KEY (`idData`),
  ADD KEY `idNote` (`idNote`);

--
-- Indexes for table `folders`
--
ALTER TABLE `folders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idUser` (`idUser`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`idGroup`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`idMember`),
  ADD KEY `idUser` (`idUser`),
  ADD KEY `idGroup` (`idGroup`);

--
-- Indexes for table `nbnotes`
--
ALTER TABLE `nbnotes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idUser` (`idUser`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`idNote`),
  ADD KEY `idFolder` (`idFolder`),
  ADD KEY `idGroup` (`idGroup`),
  ADD KEY `notes_ibfk_3` (`idUser`);

--
-- Indexes for table `relationship`
--
ALTER TABLE `relationship`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idRecevece` (`idReceive`);

--
-- Indexes for table `token_device`
--
ALTER TABLE `token_device`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idUser` (`idUser`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chat1vs1`
--
ALTER TABLE `chat1vs1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `chats`
--
ALTER TABLE `chats`
  MODIFY `idMes` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chatunknowns`
--
ALTER TABLE `chatunknowns`
  MODIFY `idMes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `datas`
--
ALTER TABLE `datas`
  MODIFY `idData` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=252;

--
-- AUTO_INCREMENT for table `folders`
--
ALTER TABLE `folders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `idGroup` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `idMember` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `nbnotes`
--
ALTER TABLE `nbnotes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `idNote` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=231;

--
-- AUTO_INCREMENT for table `relationship`
--
ALTER TABLE `relationship`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `token_device`
--
ALTER TABLE `token_device`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chat1vs1`
--
ALTER TABLE `chat1vs1`
  ADD CONSTRAINT `chat1vs1_ibfk_1` FOREIGN KEY (`idReceive`) REFERENCES `users` (`id`);

--
-- Constraints for table `chats`
--
ALTER TABLE `chats`
  ADD CONSTRAINT `chats_ibfk_1` FOREIGN KEY (`idGroup`) REFERENCES `groups` (`idGroup`);

--
-- Constraints for table `chatunknowns`
--
ALTER TABLE `chatunknowns`
  ADD CONSTRAINT `chatunknowns_ibfk_1` FOREIGN KEY (`idReceive`) REFERENCES `users` (`id`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`idNote`) REFERENCES `notes` (`idNote`);

--
-- Constraints for table `datas`
--
ALTER TABLE `datas`
  ADD CONSTRAINT `datas_ibfk_1` FOREIGN KEY (`idNote`) REFERENCES `notes` (`idNote`);

--
-- Constraints for table `folders`
--
ALTER TABLE `folders`
  ADD CONSTRAINT `folders_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`);

--
-- Constraints for table `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `members_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `members_ibfk_2` FOREIGN KEY (`idGroup`) REFERENCES `groups` (`idGroup`);

--
-- Constraints for table `nbnotes`
--
ALTER TABLE `nbnotes`
  ADD CONSTRAINT `nbnotes_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`);

--
-- Constraints for table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`idFolder`) REFERENCES `folders` (`id`),
  ADD CONSTRAINT `notes_ibfk_2` FOREIGN KEY (`idGroup`) REFERENCES `groups` (`idGroup`),
  ADD CONSTRAINT `notes_ibfk_3` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`);

--
-- Constraints for table `relationship`
--
ALTER TABLE `relationship`
  ADD CONSTRAINT `relationship_ibfk_1` FOREIGN KEY (`idReceive`) REFERENCES `users` (`id`);

--
-- Constraints for table `token_device`
--
ALTER TABLE `token_device`
  ADD CONSTRAINT `token_device_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
