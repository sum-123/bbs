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

 Date: 06/07/2021 18:25:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message`  (
  `message_id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `head` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `read_count` int(0) NOT NULL DEFAULT 0 COMMENT '阅读次数',
  `reply_count` int(0) NOT NULL DEFAULT 0,
  `create_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `update_time` datetime(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`message_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES (2, 331, '吃喝玩乐', 'lalala', '<p>123456789</p>', 0, 0, '2021-07-01 20:59:02', '2021-07-01 20:59:02');
INSERT INTO `message` VALUES (3, 320, '学习交流', 'ssss', '<p>sss</p>', 0, 6, '2021-07-03 17:03:46', '2021-07-03 17:03:46');
INSERT INTO `message` VALUES (4, 320, '情感树洞', 'ssss', '<p>ssssssss</p>', 0, 4, '2021-07-03 17:05:20', '2021-07-03 17:05:20');
INSERT INTO `message` VALUES (5, 320, '学习交流', 'asdlkasd', '<p>fgdgsdf</p>', 0, 0, '2021-07-02 17:48:57', '2021-07-02 17:48:57');
INSERT INTO `message` VALUES (6, 320, '学习交流', '实现送i回来的话上的', '<p>fgdgsdsadassssssssssssss</p>', 0, 0, '2021-07-02 17:54:33', '2021-07-02 17:54:33');
INSERT INTO `message` VALUES (7, 320, '学习交流', '实现送i回来的话上的', '<p>fgdgsdsadassssssssssssss阿里看见分厘卡机分厘卡经理反馈</p>', 2, 1, '2021-07-06 18:06:51', '2021-07-06 18:06:51');
INSERT INTO `message` VALUES (8, 320, '吃喝玩乐', '实现送i回来的话上的', '<p>234</p>', 0, 0, '2021-07-02 17:59:51', '2021-07-02 17:59:51');
INSERT INTO `message` VALUES (9, 320, '吃喝玩乐', '实现送i回来的话上的', '<p>26457643wf</p>', 2, 1, '2021-07-06 18:12:33', '2021-07-06 18:12:33');
INSERT INTO `message` VALUES (10, 320, '影视文学', '123', '<p>sagasdg</p>', 0, 1, '2021-07-03 17:04:42', '2021-07-03 17:04:42');
INSERT INTO `message` VALUES (11, 320, '学习交流', '我我我我我我', '<p>如题</p>', 8, 0, '2021-07-06 18:08:26', '2021-07-06 18:08:26');
INSERT INTO `message` VALUES (12, 320, '情感树洞', 'testtest', '<p>etststdajlkjl</p>', 1, 1, '2021-07-06 18:12:11', '2021-07-06 18:12:11');
INSERT INTO `message` VALUES (13, 321, '影视文学', '测试', '<p>测试</p>', 2, 1, '2021-07-06 18:12:42', '2021-07-06 18:12:42');

SET FOREIGN_KEY_CHECKS = 1;
