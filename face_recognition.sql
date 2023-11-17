-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2023 at 04:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `Is_id` int(11) NOT NULL,
  `Student_ID` int(11) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Issue` varchar(20) NOT NULL,
  `Description` varchar(150) NOT NULL,
  `Response` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stdattendance`
--

CREATE TABLE `stdattendance` (
  `std_att_id` int(11) NOT NULL,
  `std_id` varchar(40) NOT NULL,
  `std_department` varchar(11) NOT NULL,
  `std_name` varchar(40) NOT NULL,
  `std_time` varchar(40) NOT NULL,
  `std_date` varchar(40) NOT NULL,
  `std_attendance` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stdattendance`
--

INSERT INTO `stdattendance` (`std_att_id`, `std_id`, `std_department`, `std_name`, `std_time`, `std_date`, `std_attendance`) VALUES
(15, '1', ' MTECH', ' Jacob', ' 09:42:50', ' 09/07/2023', ' Present'),
(16, '2', ' MCA', ' John', ' 09:43:26', ' 09/07/2023', ' Present'),
(17, '1', 'MTECH', 'Jacob', '22:32:57', '23/07/2023', 'Present');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `StudentID` int(10) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Department` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`StudentID`, `Name`, `Email`, `Password`, `Department`) VALUES
(1, 'Jacob', 'jacob@gmail.com', '123', 'MTECH'),
(2, 'John', 'john@gmail.com', '123', 'BTECH');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`Is_id`),
  ADD KEY `Student_ID` (`Student_ID`);

--
-- Indexes for table `stdattendance`
--
ALTER TABLE `stdattendance`
  ADD PRIMARY KEY (`std_att_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`StudentID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `Is_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `stdattendance`
--
ALTER TABLE `stdattendance`
  MODIFY `std_att_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `issue`
--
ALTER TABLE `issue`
  ADD CONSTRAINT `Student_ID` FOREIGN KEY (`Student_ID`) REFERENCES `student` (`StudentID`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
