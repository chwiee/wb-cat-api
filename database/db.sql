create user 'devops'@'%' identified by 'mestre';
grant all privileges on *.* to devops@'%' identified by 'mestre';
flush privileges;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS `cats` (
  `id` int(5) NOT NULL,
  `id_api` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `origin` varchar(255) NOT NULL,
  `temperament` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `img_url1` varchar(255) NOT NULL,
  `img_url2` varchar(255) NOT NULL,
  `img_url3` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


ALTER TABLE `cats`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `cats`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;