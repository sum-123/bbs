<!--     首页     -->

<template>
  <div class="pop">
    <el-container>
      <div>
        <el-aside width="220px" class="side_lan">
          <div class="jing">
            <a class="col-2" href="#">新注册用户</a>
            <a class="col-2-1" href="#" v-html="dataList[4]"></a>
            <a class="col-2-1" href="#" v-html="dataList[5]">zs</a>
            <a class="col-2-1" href="#" v-html="dataList[6]">ls</a>
            <a class="col-2-1" href="#" v-html="dataList[7]">we</a>
          </div>
          <div class="dong">
            <a class="col-2" href="#">留言分类</a>
            <a class="col-2-1" @click="chuancan(1)">学习交流</a>
            <a class="col-2-1" @click="chuancan(2)">影视文学</a>
            <a class="col-2-1" @click="chuancan(3)">吃喝玩乐</a>
            <a class="col-2-1" @click="chuancan(4)">情感树洞</a>
            <a class="col-2" href="#">回到顶部</a>
          </div>
        </el-aside>
      </div>

      <el-main>
        <div class="content-1" id="one">
          <div class="head-1">
            <a href="#" class="head-1-1" @click="chuancan(1)"
              >学习交流<el-button type="primary" class="mess_count">{{
                dataList[0]
              }}</el-button></a
            >
          </div>
          <div
            class="departmentContent"
            v-for="(item, index1) in studyList"
            :key="index1"
          >
            <img class="rounded-circle avatar" :src="img(item[8])" alt="" />
            <div class="departmentInfo">
              <div
                class="departmentNamesty"
                @click="jump(item['7'], item['5'])"
              >
                {{ item[0] }}
              </div>

              <div class="info">
                作者: {{ item[6] }}&nbsp;&nbsp;&nbsp; 日期:
                {{ item[4] }}
                &nbsp;&nbsp;&nbsp; 阅读数:
                {{ item[2] }}&nbsp;&nbsp;&nbsp; 回复数:
                {{ item[3] }}
              </div>

              <div class="message-detail" v-html="item[1]"></div>
            </div>
          </div>
        </div>
        <div>
          <div class="content-2" id="two">
            <div class="head-1">
              <a class="head-1-1" @click="chuancan(2)"
                >影视文学<el-button type="primary" class="mess_count">{{
                  dataList[1]
                }}</el-button></a
              >
            </div>
            <div
              class="departmentContent"
              v-for="(item, index2) in movieList"
              :key="index2"
            >
              <img class="rounded-circle avatar" :src="img(item[8])" alt="" />
              <div class="departmentInfo">
                <div
                  class="departmentNamesty"
                  @click="jump(item['7'], item['5'])"
                >
                  {{ item[0] }}
                </div>

                <div class="info">
                  作者: {{ item[6] }}&nbsp;&nbsp;&nbsp; 日期:
                  {{ item[4] }}
                  &nbsp;&nbsp;&nbsp; 阅读数:
                  {{ item[2] }}&nbsp;&nbsp;&nbsp; 回复数:
                  {{ item[3] }}
                </div>

                <div class="message-detail" v-html="item[1]"></div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <div class="content-3" id="three">
            <div class="head-1">
              <a href="#" class="head-1-1" @click="chuancan(3)"
                >吃喝玩乐<el-button type="primary" class="mess_count">{{
                  dataList[2]
                }}</el-button></a
              >
            </div>
            <div
              class="departmentContent"
              v-for="(item, index3) in eatList"
              :key="index3"
            >
              <img class="rounded-circle avatar" :src="img(item[8])" alt="" />
              <div class="departmentInfo">
                <div
                  class="departmentNamesty"
                  @click="jump(item['7'], item['5'])"
                >
                  {{ item[0] }}
                </div>

                <div class="info">
                  作者: {{ item[6] }}&nbsp;&nbsp;&nbsp; 日期:
                  {{ item[4] }}
                  &nbsp;&nbsp;&nbsp; 阅读数:
                  {{ item[2] }}&nbsp;&nbsp;&nbsp; 回复数:
                  {{ item[3] }}
                </div>

                <div class="message-detail" v-html="item[1]"></div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <div class="content-4" id="four">
            <div class="head-1">
              <a href="#" class="head-1-1" @click="chuancan(4)"
                >情感树洞<el-button type="primary" class="mess_count">{{
                  dataList[3]
                }}</el-button></a
              >
              <div
                class="departmentContent"
                v-for="(item, index4) in emotionList"
                :key="index4"
              >
                <img
                  class="rounded-circle avatar"
                  :src="img(item[8])"
                  alt=""
                />
                <div class="departmentInfo">
                  <div
                    class="departmentNamesty"
                    @click="jump(item['7'], item['5'])"
                  >
                    {{ item[0] }}
                  </div>

                  <div class="info">
                    作者: {{ item[6] }}&nbsp;&nbsp;&nbsp; 日期:
                    {{ item[4] }}
                    &nbsp;&nbsp;&nbsp; 阅读数:
                    {{ item[2] }}&nbsp;&nbsp;&nbsp; 回复数:
                    {{ item[3] }}
                  </div>

                  <div class="message-detail" v-html="item[1]"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
    <el-footer height="100px">
      <div class="mod_copyright">
        <div class="copyright">
          地址：北京市昌平区华北电力大学 &nbsp;&nbsp; 电话：400-618-4000
          &nbsp;&nbsp;邮箱: xxxxxxxxx.cn <br />
          Github地址：xxxxxxxxx
        </div>
      </div>
    </el-footer>
    <!-- <el-footer height="100px">
      <div class="mod_copyright">
      
        <div class="copyright">
          地址：北京市昌平区华北电力大学 &nbsp;&nbsp;
          电话：400-618-4000 &nbsp;&nbsp;邮箱: xxxxxxxxx.cn <br />
          Github地址：xxxxxxxxx
        </div>
      </div>
    </el-footer> -->
  </div>
</template>


<script>
import { request } from '../network/request';
export default {
  created() {
    var a = 0;
    var b = 0;
    var c = 0;
    var d = 0;
    var that = this;
    request({
      method: "GET",
      url: "http://127.0.0.1:5000/index",
    })
      .then((res) => {
        that.dataList = res.data;
        // console.log(that.dataList);

        for (var i in that.dataList) {
          // console.log(that.dataList[i][5]);
          if (that.dataList[i][5] == "学习交流") {
            // console.log(that.dataList[i]);
            that.studyList[a] = that.dataList[i];
            a++;
          }
          if (that.dataList[i][5] == "影视文学") {
            // console.log(that.dataList[i]);
            that.movieList[b] = that.dataList[i];
            b++;
          }
          if (that.dataList[i][5] == "吃喝玩乐") {
            // console.log(that.dataList[i]);
            that.eatList[c] = that.dataList[i];
            c++;
          }
          if (that.dataList[i][5] == "情感树洞") {
            // console.log(that.dataList[i]);
            that.emotionList[d] = that.dataList[i];
            d++;
          }
          this.$set(that.studyList);
          this.$set(that.eatList);
          this.$set(that.emotionList);
          this.$set(that.movieList);
        }

        // console.log(that.studyList);
        // console.log(that.eatList);
        console.log(that.dataList);
        // console.log(that.studyList[0][7]);
      })
      .catch(function (err) {
        console.log(err);
      });
  },
  data() {
    return {
      dataList: [],
      studyList: [],
      movieList: [],
      eatList: [],
      emotionList: [],
      activeName: "1",
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
    goOne() {
      document.querySelector("#one").scrollIntoView(true);
    },
    goTwo() {
      document.querySelector("#two").scrollIntoView(true);
    },
    goThree() {
      document.querySelector("#three").scrollIntoView(true);
    },
    goFour() {
      document.querySelector("#four").scrollIntoView(true);
    },
    chuancan(flag) {
      this.$router.push({ name: "myMessage1", query: { id: flag } });
    },
    jump(messageId, type) {
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
.head-1-1 {
  text-decoration: none;
  color: #6c757d;
}
.mess_count {
  vertical-align: middle;
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