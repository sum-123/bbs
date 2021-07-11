<template>
  <div style="margin: 20px">
    <el-form
      :model="ruleForm"
      status-icon
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="用户名">
        {{ username }}
      </el-form-item>
      <el-form-item label="旧密码" prop="Oldpass">
        <el-input
          type="password"
          v-model="ruleForm.Oldpass"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="pass">
        <el-input
          type="password"
          v-model="ruleForm.pass"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="checkPass">
        <el-input
          type="password"
          v-model="ruleForm.checkPass"
          autocomplete="off"
        ></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')"
          >提交</el-button
        >
        <el-button @click="resetForm('ruleForm')">重置</el-button>
        <el-button @click="back">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>



<script>
import {request} from '../network/request'
import Crypto from "@/crypto/index.js";
export default {
  data() {
    var validateOldpass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入旧密码"));
      } else if (value != localStorage.password) {
        callback(new Error("请输入正确的旧密码"));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入新密码"));
      } else if (value == localStorage.password) {
        callback(new Error("两次密码不能相同！"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };

    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入新密码"));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error("两次输入新密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      username: localStorage.username,
      ruleForm: {
        Oldpass: localStorage.password,
        pass: "",
        checkPass: "",
      },
      rules: {
        Oldpass: [{ validator: validateOldpass, trigger: "blur" }],
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
      },
    };
  },

  methods: {
    submitForm() {
      var that = this;
      request({
        method: "post",
        url: "/changePass",
        data: {
          username: localStorage.username,
          password: Crypto.set(this.ruleForm.pass),
        },
      })
        .then(function (res) {
          if (res.data == "success") {
            localStorage.password = that.ruleForm.pass;
            localStorage.state = 0;
            alert("更改成功!请重新登陆!");
            that.$router.push({
              path: "login",
            });
            location.reload();
          }
        })
        .catch(function (err) {
          console.log(err);
        });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
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

