/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : webfinancesystem

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2016-12-09 11:19:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Procedure structure for bank1
-- ----------------------------
DROP PROCEDURE IF EXISTS `bank1`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `bank1`(IN `user_id` int,OUT `total_pay` float(7,2))
BEGIN
	#Routine body goes here...
DECLARE user_info VARCHAR(20);
DECLARE done int default -1;  -- to control the loop
DECLARE tmp0 int;
DECLARE tmp1 char(2);
DECLARE tmp2 FLOAT(7,2);


DECLARE user_device CURSOR for SELECT device.deviceid, device.type, receivables.basicfee
																FROM (receivables JOIN device ON device.deviceid=receivables.deviceid) 
																WHERE device.clientid=user_id and receivables.flag=1;

DECLARE continue handler for not found set done=1;

-- SELECT client.`name` INTO user_info FROM client, device WHERE device.clientid=client.id and client.id = 11;
-- SELECT * FROM (receivables LEFT JOIN device ON device.deviceid=receivables.deviceid) WHERE device.clientid=user_id;
-- SET total_pay=2;
OPEN user_device;
set total_pay = 0;
myloop:LOOP

		 
        fetch user_device into tmp0,tmp1,tmp2; 
				-- exit
        if done = 1 then   
        leave myLoop;  
        end if;  
          
        /* do something */  
				set total_pay = total_pay + tmp2*1.08;

				if tmp1 = "01" then
				set total_pay = total_pay + tmp2*0.1;
				end if;
				if tmp1 = "02" then
				set total_pay = total_pay + tmp2*0.15;
				end if;

        -- output
				-- select tmp0,tmp1 ;

END LOOP myloop;

CLOSE user_device;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for bank2
-- ----------------------------
DROP PROCEDURE IF EXISTS `bank2`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `bank2`(IN `user_id` int,IN `pay_money` float,OUT `bool_result` int)
BEGIN
	#Routine body goes here...
DECLARE money_should_pay int DEFAULT 0;


CALL bank1(user_id, money_should_pay);

if pay_money > money_should_pay THEN
set bool_result = 1;
else
set bool_result = 0;
END IF;
INSERT INTO user_pay VALUES(user_id, "存款", pay_money, "random_serial_number");
SELECT * FROM user_pay;
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for bank3
-- ----------------------------
DROP PROCEDURE IF EXISTS `bank3`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `bank3`(IN `user_id` int,IN `pay_money` float(7,2),IN `serial` varchar(20),OUT `bool_result` int)
BEGIN
	#Routine body goes here...
DECLARE serial_number VARCHAR(20);
DECLARE payfee_paymoney int DEFAULT 0;
DECLARE device_deviceid int DEFAULT 0;

SELECT payfee.bankserial, payfee.paymoney, device.deviceid
	FROM (payfee JOIN device ON device.deviceid=payfee.deviceid)
  WHERE payfee.bankserial = serial INTO serial_number, payfee_paymoney, device_deviceid;

set payfee_paymoney = payfee_paymoney*(-1);

INSERT INTO user_pay VALUES(user_id, "冲正", payfee_paymoney, serial_number);

UPDATE receivables set receivables.flag=0 WHERE receivables.deviceid=device_deviceid;

SELECT * FROM user_pay;

-- 10,200,'ZS201608080010',@temp
END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for bank4
-- ----------------------------
DROP PROCEDURE IF EXISTS `bank4`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `bank4`(IN `bank_id` int,IN `pay_number` int,IN `total_money` float,IN `pay_date` datetime,OUT `bool_result` int)
BEGIN
	#Routine body goes here...

END
;;
DELIMITER ;

-- ----------------------------
-- Procedure structure for fund_device
-- ----------------------------
DROP PROCEDURE IF EXISTS `fund_device`;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `fund_device`(IN `user_id` int,IN `money` float(7,2),IN `serial` varchar(20),OUT `bool_result` int)
BEGIN
	#Routine body goes here...

END
;;
DELIMITER ;
