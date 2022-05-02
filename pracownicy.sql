-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 02 Maj 2022, 12:43
-- Wersja serwera: 10.4.19-MariaDB
-- Wersja PHP: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `matura2020`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownicy`
--

CREATE TABLE `pracownicy` (
  `nr_p` int(11) NOT NULL,
  `nazwisko` text NOT NULL,
  `imie` text NOT NULL,
  `staz` varchar(2) NOT NULL,
  `pensja` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pracownicy`
--

INSERT INTO `pracownicy` (`nr_p`, `nazwisko`, `imie`, `staz`, `pensja`) VALUES
(736, 'Smitko', 'Alan', '10', 2000),
(7499, 'Nowak', 'Kazimierz', '15', 3000),
(7521, 'Więcek', 'Mariusz', '11', 3500),
(7566, 'Jonas', 'Kamil', '12', 2500),
(7654, 'Martin', 'Leon', '20', 2300),
(7698, 'Bracki', 'Bartosz', '15', 1530),
(7782, 'Celerek', 'Agnieszka', '12', 1680),
(7788, 'Skotnik', 'Natalia', '21', 2000),
(7839, 'King', 'Mirosław', '22', 1500);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
