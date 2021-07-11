<template>
  <div class="pop">
    <el-container>
      <el-main>
        <div>
          <div class="content-2" v-for="(item,index) in messageList" :key="index">
            <div class="departmentContent" >  
              <div class="departmentInfo">
                <div class="departmentNamesty">标题：{{ item['1'] }} 类型：{{item['6']}}</div>

                <div class="info">
                  作者: {{ username }}&nbsp;&nbsp;&nbsp; 日期:
                  {{ item['2'] }} &nbsp;&nbsp;&nbsp; 阅读数:
                  {{ item['3'] }}&nbsp;&nbsp;&nbsp; 回复数:
                  {{ item['4'] }}
                </div>
                <el-divider></el-divider>
                <div class="message-detail">
                  <span class="departmentNamesty">内容：</span>
                  <div v-html="item['5']"></div>
                </div>
                <el-divider></el-divider>
                <el-button type="primary" round style="float:right"   @click="jump(item['0'],item['6'])"
                  >查看详情</el-button
                >
              </div>
              
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>


<script>
import { request } from '../network/request';
export default {
  created() {
    //在生成页面时自动获取当前用户的所发表过的message
    var that = this;
    request({
      method: "post",
      url: "http://127.0.0.1:5000/myMessage2",
      data: {
        username: localStorage.username,
      },
    })
      .then((res) => {
        that.messageList = res.data;
        // console.log(res.data)
      })

      .catch(function (err) {
        console.log(err);
      });
  },
  data() {
    return {
      username:localStorage.username,
      messageList: [],
      activeName: "1",
      url:localStorage.avatar
    };
  },
  
  computed: {
        img () {
            return require('../assets/'+this.url)
        }
  },
  methods: {
    jump(messageId,type) {
      localStorage.messageId = messageId;
      localStorage.type = type;
      this.$router.push({
        path: "messageDetail",
      });
    },
  },
};
</script>

<style scoped>
.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-footer {
  background-color: #fefeff;
  color: rgb(51, 51, 51);
  text-align: center;
  line-height: 60px;
}

a {
  display: block;
}

.col-2,
.col-2-1 {
  display: block;
  width: 190px;
  height: 55px;
  background-color: #e5e2f0;
  font-size: 14px;
  color: #fff;
  text-decoration: none;
  padding-left: 30px;
  line-height: 40px;
  text-align: center;
}
.col-2-1:hover {
  background-color: #d0dbe6;
}
.col-2-1 {
  color: #333;
}
.col-2 {
  background-color: #5faaf0;
  font-size: 16px;
}

.side_lan {
  display: inline;
}
.dong {
  position: sticky;
  top: 100px;
}
.content-1,
.content-2,
.content-3,
.content-4 {
  width: 900px;
  margin: 0 auto;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.801);
}
.coll-1 {
  text-align: center;
}
.head-1 {
  font-size: 32px;
  display: inline;
  color: #6c757d;
  font-family: inherit;
  font-weight: 600;
}
.rounded-circle {
  border-radius: 50% !important;
}

.avatar {
  margin: 15px 0;
  width: 64px;
  height: 64px;
}
.col-left {
  display: inline;
}
.departmentContent {
  padding: 10rpx 0 10rpx 0;
  display: flex;
  align-items: center;
  margin-bottom: 80px;
  margin-top: 10px;
}
.departmentContent .departmentInfo {
  padding-left: 20px;
}
.departmentInfo .departmentNamesty {
  font-weight: bold;
  font-size: 18px;
  padding-bottom: 5rpx;
}
.departmentContent .departmentInfo .departmentNamesty {
  text-align: left;
  margin-bottom: 16px;
}
.info {
  font-family: inherit;
  font-size: 14px;
  text-align: left;
}
.departmentInfo .message-detail {
  margin-top: 20px;
  font-size: 16px;
  line-height: 25px;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  /* 弹性伸缩盒子模型显示 */
  display: -webkit-box;
  /* 限制在一个块元素显示的文本的行数 */
  -webkit-line-clamp: 3;
  /* 设置或检索伸缩盒对象的子元素的排列方式 */
  -webkit-box-orient: vertical;
}
</style>