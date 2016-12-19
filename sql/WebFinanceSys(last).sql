create schema WebFinanceSystem character set utf8;
use WebFinanceSystem;

create table bank(
  id int(4) NOT NULL,
  name varchar(20) NULL,
  code char(2) unique,
  primary key (id)
);

create table client(
  id int(4) NOT NULL,
  name varchar(20) NULL,
  address varchar(80) NULL,
  tel varchar(20) NULL,
  primary key (id)
);

create table device(
  deviceid int(4) NOT NULL,
  clientid int(4) NOT NULL,
  type char(2) NULL,
  balance float(7,2) NULL,
  primary key (deviceid),
  foreign key (clientid) references client(id)
);
 
create table electricity(   
  id int(4) NOT NULL,
  deviceid int(4) NOT NULL,
  yearmonth char(6) NULL,
  snum int(10) NULL,
  primary key (id),
  foreign key (deviceid) references device(deviceid)
);

create table receivables(
  id int(4) NOT NULL,
  yearmonth char(6) NULL,
  deviceid int(4) NOT NULL,
  basicfee float(7,2) NULL,
  flag char(1) NULL,
  primary key (id),
  foreign key (deviceid) references device(deviceid)
);

create table payfee(
  id int(4) NOT NULL,
  deviceid int(4) NOT NULL,
  paymoney varchar(20) NULL,
  paydate datetime NULL,
  bankcode char(2) NULL,
  type char(4) NULL,
  bankserial varchar(20) NULL,
  primary key (id),
  foreign key (deviceid) references device(deviceid),
  foreign key (bankcode) references bank(code)
);

create table bankrecord(
  id int(4) NOT NULL,
  payfee float(7,2) NULL,
  bankcode char(2) NULL,
  bankserial varchar(20) NULL,
  primary key (id),
  foreign key (bankcode) references bank(code)
);

create table checkresult(
  id int(4) NOT NULL,
  checkdate datetime NULL,
  bankcode char(2) NULL,
  banktotalcount int(4) NULL,
  banktotalmoney float(10,2) NULL,
  ourtotalcount int(4) NULL,
  ourtotalmoney float(10,2) NULL,
  primary key (id),
  foreign key (bankcode) references bank(code)
);

create table check_exception(
  id int(4) NOT NULL,
  checkdate datetime NULL,
  bankcode char(2) NULL,
  bankserial varchar(20) NULL,
  bankmoney float(7,2) NULL,
  ourmoney float(7,2) NULL,
  exceptiontype char(3) NULL,
  primary key (id),
  foreign key (bankcode) references bank(code)
);
