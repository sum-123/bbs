<template>
  <div class="row col-12 comment" style="text-align: center">
    <div class="col-1" style="padding: 0">
      <img :src="img" alt="" style="height: 48px; float: left" />
    </div>
    <div class="row col-11 textarea-container" style="">
      <el-input
        type="text"
        maxlength="50"
        show-word-limit
        autosize
        placeholder="请发表文明合法言论"
        v-model="comment"
      >
      </el-input>
      <el-button @click="postComment"> 发表评论</el-button>
      <el-button @click="back"> 返回</el-button>
    </div>
    <div
      class="col-11"
      style="margin: 15px 20px 10px 20px; border-bottom: 1px solid #cccccc"
    ></div>

    <div id="commentDiv" class="row col-12" style="margin: 0; padding: 0"></div>
  </div>
</template>

<script>
import {request} from '../network/request'
export default {
  data() {
    return {
      comment: "",
      url: localStorage.avatar,
    };
  },
  computed: {
    img() {
      return require("../assets/" + this.url);
    },
  },
  methods: {
    postComment() {
      var that1 = this;
      this.$confirm("是否评论?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          var that = that1;
          request({
              method: "post",
              url: "http://127.0.0.1:5000/createComment",
              data: {
                messageId: localStorage.messageId,
                username: localStorage.username,
                comment: that.comment,
              },
            })
            .then((res) => {
              console.log(res);
            })
            .catch(function (err) {
              console.log(err);
            });
          this.$message({
            type: "success",
            message: "评论成功!",
          });
          that1.comment = ""
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消评论",
          });
        });
    },
    back() {
      this.$router.push({
        path: "messageDetail",
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