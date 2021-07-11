
<template>
  <div style="margin-top: 15px" class="moban">
    <el-input
      placeholder="请输入内容"
      v-model="input"
      class="input-with-select"
    >
      <el-select v-model="select" slot="prepend" placeholder="请选择">
        <el-option label="留言" value="1"></el-option>
        <el-option label="用户" value="2"></el-option>
      </el-select>
      <el-button
        slot="append"
        icon="el-icon-search"
        @click="searchData"
      ></el-button>
    </el-input>
    <div class="search-message">
      <div
        class="departmentContent"
        v-for="(item, index) in current_messages"
        :key="index"
      >
        <img class="rounded-circle avatar" :src="img(item[6])" alt="" />
        <div class="departmentInfo">
          <div class="departmentNamesty" @click="jump(item['0'])">
            {{ item[1] }}
          </div>

          <div class="info">
            作者: {{ item[7] }}&nbsp;&nbsp;&nbsp; 日期:
            {{ item[2] }}
            &nbsp;&nbsp;&nbsp; 阅读数: {{ item[3] }}&nbsp;&nbsp;&nbsp; 回复数:
            {{ item[4] }}
          </div>

          <div class="message-detail" v-html="item[5]"></div>
        </div>
      </div>
      
    </div>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="total"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="queryInfo.pagenum"
      :page-size="3"
    >
    </el-pagination>
    <el-footer height="100px">
      <div class="mod_copyright">
        <div class="copyright">
          地址：北京市昌平区华北电力大学 &nbsp;&nbsp; 电话：400-618-4000
          &nbsp;&nbsp;邮箱: xxxxxxxxx.cn <br />
          Github地址：xxxxxxxxx
        </div>
      </div>
    </el-footer>
  </div>
  
</template>

<style>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
</style>
<style scoped>
.moban {
  width: 1100px;
  margin: 0 auto;
}

.search-message {
  box-shadow: 0 0 28px #dee9fe, 0 0 15px rgba(0, 0, 0, 0.04);
  margin-top: 10px;
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
}
</style>
<script>
import {request} from '../network/request'
export default {
  data() {
    return {
      input: "",
      select: "",
      queryInfo: {
        query: "",
        pagenum: 1,
      },
      id: "",

      current_messages: [],
      all_messages: [],
      total: 0,
    };
  },
  computed: {
    img: function () {
      return function (url) {
        return require("../assets/" + url);
      };
    },
  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(newPage) {
      this.queryInfo.pagenum = newPage;
      // console.log(`当前页: ${this.queryInfo.pagenum}`);
      var a = this.queryInfo.pagenum;
      // console.log(a);
      this.current_messages = this.all_messages.slice(3 * a - 3, 3 * a);
      // console.log(`当前curret_messages长度: ${this.current_messages}`);
    },
    jump(messageId, type) {
      localStorage.messageId = messageId;
      localStorage.type = type;
      this.$router.push({
        path: "messageDetail",
      });
    },

    searchData() {
      console.log(this.input);
      console.log(this.select);

      request({
        method: "POST",
        url: "http://127.0.0.1:5000/search",
        data: {
          select: this.select,
          input: this.input,
        },
      })
        .then((res) => {
          console.log(res.data);
          if(this.select==""){
            alert("请选择搜索分类");
            return
          }
          if(res.data=="invalid"){
            alert("请输入搜索内容")
            return
          }
          if(res.data!="invalid"){
          for (var i in res.data) {
            this.all_messages[i] = res.data[i];
          }
          this.total = this.all_messages.length;
          this.current_messages = this.all_messages.slice(0, 3);}
          // console.log(res.data)
          // for(var i in res.data){
          //   that.all_messages[i]=res.data[i]
        })

        .catch(function (err) {
          console.log(err);
        });
    },
  },
  // created() {
  //   this.flag = this.$route.query.id;
  //   console.log(this.flag);
  //   var that = this;
  //   this.$axios({
  //     method: "",
  //     url: "http://127.0.0.1:5000/search",
  //     data: {},
  //   })
  //     .then((res) => {
  //       // that.all_messages = res.data;
  //       console.log(res.data[0]);
  //       // for(var i in res.data){
  //       //   that.all_messages[i]=res.data[i]
  //       // }
  //       // JSON.parse(that.all_messages)
  //       this.id = res.data
  //       if (this.id == "invalid") {
  //         alert("请输入搜索内容");
  //       }
  //       if (res.data != "invalid") {
  //         for (var i in res.data) {
  //           that.all_messages[i] = res.data[i];
  //         }
  //         that.total = that.all_messages.length;
  //         that.current_messages = that.all_messages.slice(0, 3);
  //         console.log(that.all_messages);

  //         console.log();

  //         console.log(this.url);
  //       }
  //     })

  //     .catch(function (err) {
  //       console.log(err);
  //     });
  // },
};
</script>