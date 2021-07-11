<template>
  <div>
    <el-tabs tab-position="left" type="border-card" style="height: 700px">
      <el-tab-pane label="个人信息">
        <el-row>
          <el-col :span="8">
            <el-card :body-style="{ padding: '10px', margin: '20px' }">
              <!-- <img :src="src" class="image" /> -->
              <div style="padding: 14px">
                <div class="bottom clearfix">
                  <el-upload
                    class="avatar-uploader"
                    action="action"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload"
                    :http-request="uploadFile"
                    disabled
                  >
                    <img v-if="img" :src="img" class="avatar" />
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                    <el-button
                      slot="tip"
                      class="el-upload__tip"
                      style="margin: 30px"
                      @click="changeAvatar"
                    >
                      点击修改头像
                    </el-button>
                  </el-upload>
                </div>
              </div>
            </el-card>
          </el-col>

          <el-col :span="16">
            <el-card :body-style="{ padding: '17px', margin: '20px' }">
              <div slot="header" class="clearfix">
                <span>基本资料</span>
              </div>
              <div>
                <el-form label-width="80px" size="small" label-position="right">
                  <el-form-item label="用户名">
                    {{ username }}
                  </el-form-item>
                  <el-form-item label="注册时间">
                    {{ registerTime }}
                  </el-form-item>
                  <el-form-item label="邮箱">
                    {{ email }}
                  </el-form-item>
                  <el-form-item label="发表留言">
                    {{ message }}篇
                  </el-form-item>
                  <el-form-item label="发表评论">
                    {{ comment }}条
                  </el-form-item>
                </el-form>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <!-- <el-row v-if="state == 0">
         <div>未登录</div>
        </el-row> -->
      </el-tab-pane>

      <el-tab-pane label="修改密码">
        <el-button type="primary" @click="changePass">修改密码</el-button>
      </el-tab-pane>

      <el-tab-pane label="安全邮箱">安全邮箱</el-tab-pane>
    </el-tabs>
  </div>
</template>



<script>
import {request} from '../network/request'
export default {
  data() {
    return {
      // state: 0,
      username: localStorage.username,
      registerTime: localStorage.createTime,
      email: "896202576@qq.com",
      message: localStorage.message,
      comment: localStorage.comment,
      url: localStorage.avatar,
    };
  },
  computed: {
    img() {
      return require("../assets/" + this.url);
    },
  },
  created() {
    request({
      method: "post",
      url: "http://127.0.0.1:5000/personal",
      data: {
        username: localStorage.username,
      },
    })
      .then(function (res) {
          console.log(res.data);  
          localStorage.createTime = res.data[0];
          localStorage.message = res.data[1];
          localStorage.comment = res.data[2];
      })
      .catch(function (err) {
        console.log(err);
      });
  },

  methods: {
    async uploadFile(params) {
      let form = new FormData();
      form.append("file", params.file);

      const res = await this.$axios.post(
        "http://127.0.0.1:5000/personal",
        form
      );
      console.log(res);
      this.img = res.data;
    },

    changePicture() {
      alert("修改头像");
    },
    handleAvatarSuccess(res, file) {
      this.img = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },

    changePass() {
      this.$router.push({
        path: "changePass",
      });
    },
    changeAvatar() {
      this.$router.push({
        path: "changeAvatar",
      });
    },
  },
};
</script>



<style>
.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.image {
  width: 50%;
  /* display: block; */
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

