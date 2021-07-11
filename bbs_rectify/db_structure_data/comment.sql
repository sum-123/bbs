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

 Date: 08/07/2021 21:24:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL COMMENT '发表回复的用户ID',
  `message_id` int NOT NULL COMMENT '回复的留言的ID',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`comment_id`) USING BTREE,
  KEY `user_id1` (`user_id`) USING BTREE,
  KEY `message_id` (`message_id`) USING BTREE,
  CONSTRAINT `message_id` FOREIGN KEY (`message_id`) REFERENCES `message` (`message_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `user_id1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of comment
-- ----------------------------
BEGIN;
INSERT INTO `comment` VALUES (2, 320, 3, '水水水水水水', '2021-07-03 15:00:23');
INSERT INTO `comment` VALUES (3, 320, 3, '硕硕硕硕硕硕', '2021-07-03 15:26:37');
INSERT INTO `comment` VALUES (4, 321, 3, '啦啦啦啦啦', '2021-07-03 15:59:06');
INSERT INTO `comment` VALUES (5, 320, 3, 'shixingyushizhu', '2021-07-03 16:35:40');
INSERT INTO `comment` VALUES (6, 320, 3, 'shixingyushizhu', '2021-07-03 16:47:27');
INSERT INTO `comment` VALUES (7, 320, 3, '6666', '2021-07-03 16:48:54');
INSERT INTO `comment` VALUES (8, 320, 4, 'test', '2021-07-03 16:51:16');
INSERT INTO `comment` VALUES (9, 320, 4, 'ssssss', '2021-07-03 16:52:12');
INSERT INTO `comment` VALUES (10, 320, 4, '3333', '2021-07-03 16:52:34');
INSERT INTO `comment` VALUES (11, 320, 4, 'etst', '2021-07-03 16:53:00');
INSERT INTO `comment` VALUES (12, 320, 10, '1111111111', '2021-07-03 17:04:42');
INSERT INTO `comment` VALUES (13, 320, 7, '1', '2021-07-03 17:06:49');
INSERT INTO `comment` VALUES (14, 320, 9, 's', '2021-07-03 17:07:26');
INSERT INTO `comment` VALUES (15, 320, 12, 'dddddd', '2021-07-03 17:16:54');
INSERT INTO `comment` VALUES (16, 321, 13, '漂亮！', '2021-07-03 17:20:44');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
