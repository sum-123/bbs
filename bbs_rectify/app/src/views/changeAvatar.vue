<template>
  <div style="margin: 20px">
    <el-upload
      class="avatar-uploader"
      action="action"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload"
      :http-request="uploadFile"
    >
      <img v-if="img" :src="img" class="avatar" />
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      <div slot="tip" class="el-upload__tip" style="margin: 30px">
        点击头像更改
      </div>
    </el-upload>
    <el-button @click="back">返回</el-button>
  </div>
</template>

<script>
import {request} from '../network/request'
export default {
  data() {
    return {
      username: localStorage.username,
      url: localStorage.avatar,
    };
  },
  
  computed: {
        img () {
            return require('../assets/'+this.url)
        }
  },

  methods: {
    async uploadFile(params) {
      localStorage.img = params.file.name;
      var that = this;
      request({
        method: "post",
        url: "/changeAvatar",
        data: {
          username: that.username,
          img: params.file.name,
        },
      }).then(function (res) {
        if (res.data == "success") {
          alert("更改成功!");
          localStorage.avatar = localStorage.img;
          localStorage.state = 0;
          sessionStorage.clear();
          that.$router.push({
            path: "index",
          });
          location.reload();
        }
      });
      console.log(params.file.name);
    },

    changePicture() {
      alert("修改头像");
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
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
    back() {
      this.$router.push({
        path: "personal",
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

