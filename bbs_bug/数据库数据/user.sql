/*
 Navicat MySQL Data Transfer

 Source Server         : project
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : localhost:3306
 Source Schema         : our_bbs

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 06/07/2021 18:24:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `user_id` int(0) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `avatar` varchar(683) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像文件名称',
  `create_time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`user_id`) USING BTREE,
  INDEX `user_id`(`user_id`, `username`, `password`, `avatar`, `create_time`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 333 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (320, 'fzs', '123', 'monster.jpg', '2021-07-03 17:17:20');
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

SET FOREIGN_KEY_CHECKS = 1;
