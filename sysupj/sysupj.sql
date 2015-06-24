CREATE TABLE Student
(sid int auto_increment, 
sname text not null check(sname != ''), 
spwd text not null,
PRIMARY KEY(sid));
CREATE TABLE Teacher
(tid int auto_increment, 
tname text not null check(tname != ''), 
brief text,
PRIMARY KEY(tid));
create table Course
(cid int auto_increment,
cname text not null, 
classroom text not null, 
capasity smallint not null, 
courseCredit int,
brief text,
primary key(cid));
create table Followings
(id int auto_increment,
 follower int,
 followee int,
primary key(id),
foreign key(follower) references Student(sid) on delete cascade on update cascade,
foreign key(followee) references Course(cid) on delete cascade on update cascade);
create table Teachings
(id int auto_increment, 
teacher int not null, 
course int not null,
primary key(id),
foreign key(teacher) references Teacher(tid) on delete cascade on update cascade,
foreign key(course) references Course(cid) on delete cascade on update cascade);
create table Material
(mid int auto_increment, 
uploader int not null, 
course int not null, 
filepath text not null,
primary key(mid),
foreign key(uploader) references Student(sid),
foreign key(course) references Course(cid));
create table Discussion
(did int auto_increment, 
poster int not null, 
dtype int not null, 
target int, 
content text, 
primary key(did),
foreign key(poster) references Student(sid),
foreign key(target) references Course(cid));
create table Ratnig
(rid int auto_increment, 
rater int not null, 
target int not null, 
rating tinyint not null,
primary key(rid),
foreign key(rater) references Student(sid),
foreign key(target) references Teacher(tid));
DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;