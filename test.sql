-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2024 at 03:55 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sbn`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `AdminID` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`AdminID`, `password`) VALUES
('Bns_0000', 'Bns_0000');

-- --------------------------------------------------------

--
-- Table structure for table `allowed`
--

CREATE TABLE `allowed` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `configure_camera`
--

CREATE TABLE `configure_camera` (
  `id` int(11) NOT NULL,
  `privilage_id` varchar(150) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `ip` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `configure_camera`
--

INSERT INTO `configure_camera` (`id`, `privilage_id`, `User_id`, `ip`) VALUES
(5, 'public_741852963741@rohan', 'gk_rohan', '192.168.1.52:8080/video'),
(6, 'public_741852963741@rohan', 'gk_rohan', '192.168.1.52:8080/video'),
(7, 'public_741852963741@rohan', 'gk_rohan', '192.168.1.52:8080/video'),
(8, 'public_741852963741@rohan', 'gk_rohan', '192.168.1.52:8080/video');

-- --------------------------------------------------------

--
-- Table structure for table `criminals`
--

CREATE TABLE `criminals` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `founded_person`
--

CREATE TABLE `founded_person` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `db_image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `typeOfPerson` varchar(50) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `general_panel`
--

CREATE TABLE `general_panel` (
  `general_ID` varchar(150) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `gov_panel`
--

CREATE TABLE `gov_panel` (
  `gov_ID` varchar(150) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `proof_path` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `missing_person`
--

CREATE TABLE `missing_person` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `missing_person`
--

INSERT INTO `missing_person` (`_id`, `name`, `age`, `image_path`, `gender`, `information`, `date`, `User_id`) VALUES
(1, 'sharath', 23, 'static\\persons\\gk_rohan\\missing_person\\1.jpg', 'male', 'dhfhkjsddbvcvmnsdbvmjsd\r\ndsdjkjvsbjb,svb\r\nsdlklkfsd,dkvk', '2024-02-21 13:39:54', 'gk_rohan');

-- --------------------------------------------------------

--
-- Table structure for table `not_allowed`
--

CREATE TABLE `not_allowed` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `person_count`
--

CREATE TABLE `person_count` (
  `id` int(11) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `criminals_count` int(11) DEFAULT NULL,
  `missing_count` int(11) DEFAULT NULL,
  `wanted_count` int(11) DEFAULT NULL,
  `allowed_count` int(11) DEFAULT NULL,
  `not_allowed_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `person_count`
--

INSERT INTO `person_count` (`id`, `User_id`, `criminals_count`, `missing_count`, `wanted_count`, `allowed_count`, `not_allowed_count`) VALUES
(1, 'gk_rohan', 0, 1, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `private_panel`
--

CREATE TABLE `private_panel` (
  `private_ID` varchar(150) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `public_panel`
--

CREATE TABLE `public_panel` (
  `public_ID` varchar(150) NOT NULL,
  `User_id` varchar(50) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `public_panel`
--

INSERT INTO `public_panel` (`public_ID`, `User_id`, `date`) VALUES
('public_741852963741@rohan', 'gk_rohan', '2024-02-21 13:38:35');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` varchar(50) NOT NULL,
  `firstName` varchar(80) NOT NULL,
  `secondName` varchar(80) DEFAULT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(100) NOT NULL,
  `addharID` varchar(100) NOT NULL,
  `profile_path` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `catagory` varchar(80) DEFAULT NULL,
  `verify` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `firstName`, `secondName`, `phone`, `email`, `password`, `addharID`, `profile_path`, `date`, `catagory`, `verify`) VALUES
('demo', 'demo', 'demo', '123', 'demo', 'demo', 'demo', NULL, '2024-06-23 07:11:18', NULL, NULL),
('gk_rohan', 'rohan', 'gk', '7418529526', 'gkrohan53@gmail.com', 'Rohan_2001', '741852963741', 'static\\profile_image\\gk_rohan.jpg', '2024-02-21 13:35:58', 'public', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `wanted_person`
--

CREATE TABLE `wanted_person` (
  `_id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `age` int(11) NOT NULL,
  `image_path` text DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `information` text DEFAULT NULL,
  `date` datetime NOT NULL,
  `User_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`AdminID`);

--
-- Indexes for table `allowed`
--
ALTER TABLE `allowed`
  ADD PRIMARY KEY (`_id`);

--
-- Indexes for table `configure_camera`
--
ALTER TABLE `configure_camera`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `criminals`
--
ALTER TABLE `criminals`
  ADD PRIMARY KEY (`_id`);

--
-- Indexes for table `founded_person`
--
ALTER TABLE `founded_person`
  ADD PRIMARY KEY (`_id`);

--
-- Indexes for table `general_panel`
--
ALTER TABLE `general_panel`
  ADD PRIMARY KEY (`general_ID`),
  ADD UNIQUE KEY `User_id` (`User_id`);

--
-- Indexes for table `gov_panel`
--
ALTER TABLE `gov_panel`
  ADD PRIMARY KEY (`gov_ID`),
  ADD UNIQUE KEY `User_id` (`User_id`);

--
-- Indexes for table `missing_person`
--
ALTER TABLE `missing_person`
  ADD PRIMARY KEY (`_id`);

--
-- Indexes for table `not_allowed`
--
ALTER TABLE `not_allowed`
  ADD PRIMARY KEY (`_id`);

--
-- Indexes for table `person_count`
--
ALTER TABLE `person_count`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `private_panel`
--
ALTER TABLE `private_panel`
  ADD PRIMARY KEY (`private_ID`),
  ADD UNIQUE KEY `User_id` (`User_id`);

--
-- Indexes for table `public_panel`
--
ALTER TABLE `public_panel`
  ADD PRIMARY KEY (`public_ID`),
  ADD UNIQUE KEY `User_id` (`User_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `addharID` (`addharID`);

--
-- Indexes for table `wanted_person`
--
ALTER TABLE `wanted_person`
  ADD PRIMARY KEY (`_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `allowed`
--
ALTER TABLE `allowed`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `configure_camera`
--
ALTER TABLE `configure_camera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `criminals`
--
ALTER TABLE `criminals`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `founded_person`
--
ALTER TABLE `founded_person`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `missing_person`
--
ALTER TABLE `missing_person`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `not_allowed`
--
ALTER TABLE `not_allowed`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `person_count`
--
ALTER TABLE `person_count`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `wanted_person`
--
ALTER TABLE `wanted_person`
  MODIFY `_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
