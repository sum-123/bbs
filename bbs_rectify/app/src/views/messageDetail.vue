<template>
  <div class="container" style="border: 0px solid red">
    <div class="row" style="border: 0px solid blue">
      <div id="mainContent" class="row col-9" style="margin: 10px 0 0 0">
        <div class="col-12 message-detail">
          <div class="col-12 title" v-html="headline">
          <!-- <div class="col-12 title" v-html="$escape(headline)"> -->
          </div>
          <div class="col-12 info">
            作者: {{ username }}&nbsp;&nbsp;&nbsp; 类别:
            {{ value }}&nbsp;&nbsp;&nbsp; 日期:
            {{ createTime }}&nbsp;&nbsp;&nbsp; 阅读数:
            {{ readCount }}&nbsp;&nbsp;&nbsp; 回复数: {{ replyCount }}
          </div>
          <div class="col-12 content">
            <div v-html="content"></div>
          </div>

          <div class="row col-12 comment" style="text-align: center">
            <div class="row col-11 textarea-container" style="">
              <el-button @click="postComment"> 发表评论</el-button>
            </div>
            <div
              class="col-11"
              style="
                margin: 15px 20px 10px 20px;
                border-bottom: 1px solid #cccccc;
              "
            ></div>

            <div
              id="commentDiv"
              class="row col-12"
              style="margin: 0; padding: 0"
            ></div>
          </div>

          <div class="row col-12 comment" style="text-align: center">
            <div
              class="row col-11 textarea-container"
              v-for="(item, index) in commentList"
              :key="index"
            >
              <div class="col-1" style="padding: 0">
                <img
                  :src="commentImg(item[3])"
                  alt=""
                  style="height: 48px; float: left"
                />
                <!-- 修改 -->
              </div>

              <span style="float: left; padding: 10px">{{ item[2] }}</span>
              <br /><el-divider> </el-divider>
              <span>{{ item[0] }}</span>

              <el-divider></el-divider>
              <div
                style="
                  font-size: 14px;
                  border-bottom: 1px solid #cccccc;
                  line-height: 25px;
                  padding-bottom: 10px;
                  margin-bottom: 20px;
                "
              >
                评论时间：{{ item[1] }}
              </div>
            </div>
            <div
              class="col-11"
              style="
                margin: 15px 20px 10px 20px;
                border-bottom: 1px solid #cccccc;
              "
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { request } from '../network/request';
export default {
  created() {
    var that = this;
    request({
      method: "post",
      url: "/messageDetail",
      data: {
        messageId: localStorage.messageId,
      },
    })
      .then((res) => {
      
        that.dataList = res.data;
        console.log(that.dataList);
        for(var i in that.dataList){
          if(that.index == 0){
            that.headline = that.dataList[i]
          }
          else if(that.index == 1){
            that.content = that.dataList[i];
          }else if(that.index == 2){
            that.createTime = that.dataList[i];
          }else if(that.index == 3){
            that.username = that.dataList[i];
          }else if(that.index == 4){
            that.readCount = that.dataList[i];
          }else if(that.index == 5){
            that.replyCount = that.dataList[i];
          }else if(that.index == 6){
            that.value = that.dataList[i];
          }else{
            that.commentList.push(that.dataList[i]);
          }
          that.index++
        }
  
        console.log(that.headline);
        console.log(that.commentList);
        
      })
      .catch(function (err) {
        console.log(err);
      });
  },
  
  data() {
    return {
      index:0,
      username: "",
      createTime: "",
      readCount: "",
      replyCount: "",
      headline: "",
      content: "",
      value: "",
      url: localStorage.avatar,
      commentUrl: "cat.jpg",
      commentList: []
    };
  },
  computed: {
    img() {
      return require("../assets/" + this.url);
    },
    commentImg: function () {
      return function (comment_url) {
        return require("../assets/" + comment_url);
      };
    },
  },
  methods: {

    postComment() {
      this.$router.push({
        path: "createComment",
      });
    },
  },
};
</script>

<style scoped>
.message-detail {
  padding: 15px;
  border: 2px solid rgba(221, 221, 221, 0.7);
  background-color: #f8f9fa;
  box-shadow: 8px 8px 8px rgba(0, 0, 0, 0.12);
}

.message-detail .title {
  padding: 5px 15px;
  color: #00bfff;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 10px;
}

.message-detail .info {
  font-size: 14px;
  border-bottom: 1px solid #cccccc;
  line-height: 25px;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.comment {
  margin: 20px 0 0 0;
  padding: 20px 20px 5px 20px;
  border: 2px solid rgba(221, 221, 221, 0.7);
  background-color: #f8f9fa;
  box-shadow: 8px 8px 8px rgba(0, 0, 0, 0.12);
}

.comment .textarea-container textarea {
  font-size: 14px;
  display: inline-block;
  box-sizing: border-box;
  background-color: #f4f5f7;
  border: 1px solid #e5e9ef;
  overflow: auto;
  border-radius: 4px;
  color: #555;
  width: 100% !important;
  height: 65px;
  transition: 0s;
  padding: 5px 10px;
  line-height: normal;
  resize: none;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>