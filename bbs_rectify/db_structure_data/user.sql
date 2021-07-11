/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : our_bbs

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 08/07/2021 21:23:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `avatar` varchar(683) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '头像文件名称',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`) USING BTREE,
  KEY `user_id` (`user_id`,`username`,`password`,`avatar`,`create_time`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=335 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (320, 'fzs', '123', 'monster.jpg', '2021-07-07 09:59:01');
INSERT INTO `user` VALUES (321, 'sxy', '1234', 'xiaoxin.jpg', '2021-07-01 19:48:51');
INSERT INTO `user` VALUES (322, 'sh', '12345', 'monster.jpg', '2021-06-30 12:47:14');
INSERT INTO `user` VALUES (323, 'zjm', '123456', 'monster.jpg', '2021-06-30 12:47:12');
INSERT INTO `user` VALUES (324, 'test', '123', 'monster.jpg', '2021-06-30 12:47:10');
INSERT INTO `user` VALUES (325, '666', '666', 'monster.jpg', '2021-06-30 12:47:08');
INSERT INTO `user` VALUES (326, '555', '555', 'monster.jpg', '2021-06-30 12:47:06');
INSERT INTO `user` VALUES (327, '777', '777', 'monster.jpg', '2021-06-30 12:47:21');
INSERT INTO `user` VALUES (328, '888', '888', 'monster.jpg', '2021-06-30 12:47:23');
INSERT INTO `user` VALUES (329, '999', '999', 'monster.jpg', '2021-06-30 12:45:30');
INSERT INTO `user` VALUES (330, '000', '000', 'monster.jpg', '2021-06-30 12:46:38');
INSERT INTO `user` VALUES (331, 'lsy', '123', 'xiaoxin.jpg', '2021-07-01 20:05:46');
INSERT INTO `user` VALUES (333, 'xyx', '123', 'monster.jpg', '2021-07-07 11:42:59');
INSERT INTO `user` VALUES (334, 'sh_1', 'jmTOhz8XTbskI/zYFFgOFQ==', 'monster.jpg', '2021-07-08 21:21:07');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
