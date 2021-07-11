<template>
  <div>
    <el-form
      label-width="80px"
      size="small"
      label-position="right"
      style="margin: 20px"
    >
      <el-form-item label="留言标题">
        <el-input
          type="text"
          placeholder="请输入标题"
          v-model="headline"
          maxlength="100"
          show-word-limit
        >
        </el-input>
      </el-form-item>
      <el-form-item label="留言内容">
        <div>
          <quill-editor
            v-model="content"
            ref="myQuillEditor"
            :options="editorOption"
            @focus="onEditorFocus($event)"
            @blur="onEditorBlur($event)"
            @change="onEditorChange($event)"
            class="editor"
          ></quill-editor>

          <form
            action
            method="post"
            enctype="multipart/form-data"
            id="uploadFormMulti"
          >
            <input
              style="display: none"
              :id="uniqueId"
              type="file"
              name="file"
              multiple
              accept="image/jpg, image/jpeg, image/png, image/gif"
              @change="uploadImg('uploadFormMulti')"
            />
          </form>
        </div>

        <!-- <el-input
          type="textarea"
          :autosize="{ minRows: 10, maxRows: 50 }"
          placeholder="请输入内容"
          v-model="content"
          maxlength="200"
          show-word-limit
        >
        </el-input> -->
      </el-form-item>
      <el-form-item label="留言类型">
        <div style="position: absolute; left: 10px; display: inline-block">
          <el-select size="medium" v-model="value" placeholder="请选择类型">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
        <div style="position: absolute; right: 10px; display: inline-block">
          <el-button plain type="primary" @click="post">发布留言</el-button>
          <el-button plain type="danger" @click="clear">清空留言</el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";
import {request} from '../network/request'
import { quillEditor } from "vue-quill-editor";

// 工具栏配置
const toolbarOptions = [
  ["bold", "italic", "underline", "strike"], // 加粗 斜体 下划线 删除线 -----['bold', 'italic', 'underline', 'strike']
  ["blockquote", "code-block"], // 引用  代码块-----['blockquote', 'code-block']
  [{ header: 1 }, { header: 2 }], // 1、2 级标题-----[{ header: 1 }, { header: 2 }]
  [{ list: "ordered" }, { list: "bullet" }], // 有序、无序列表-----[{ list: 'ordered' }, { list: 'bullet' }]
  [{ script: "sub" }, { script: "super" }], // 上标/下标-----[{ script: 'sub' }, { script: 'super' }]
  [{ indent: "-1" }, { indent: "+1" }], // 缩进-----[{ indent: '-1' }, { indent: '+1' }]
  [{ direction: "rtl" }], // 文本方向-----[{'direction': 'rtl'}]
  [{ size: ["small", false, "large", "huge"] }], // 字体大小-----[{ size: ['small', false, 'large', 'huge'] }]
  [{ header: [1, 2, 3, 4, 5, 6, false] }], // 标题-----[{ header: [1, 2, 3, 4, 5, 6, false] }]
  [{ color: [] }, { background: [] }], // 字体颜色、字体背景颜色-----[{ color: [] }, { background: [] }]
  [{ font: [] }], // 字体种类-----[{ font: [] }]
  [{ align: [] }], // 对齐方式-----[{ align: [] }]
  ["clean"], // 清除文本格式-----['clean']
  ["image", "video"], // 链接、图片、视频-----['link', 'image', 'video']
];

export default {
  name: "",
  components: {
    quillEditor,
  },
  beforeCreate() {
    (localStorage.messageId = 0), (localStorage.messageList = []);
  },
  data() {
    return {
      options: [
        {
          value: "学习交流",
          label: "学习交流",
        },
        {
          value: "影视文学",
          label: "影视文学",
        },
        {
          value: "吃喝玩乐",
          label: "吃喝玩乐",
        },
        {
          value: "情感树洞",
          label: "情感树洞",
        },
      ],
      messageId: parseInt(localStorage.messageId),
      messageList: [],
      headline: "",
      content: "",
      value: "",
      uniqueId: "uniqueId",
      //富文本编辑器配置
      editorOption: {
        modules: {
          toolbar: toolbarOptions,
        },
        theme: "snow",
        placeholder: "请输入留言内容",
      },
    };
  },
  computed: {
    //当前富文本实例
    editor() {
      return this.$refs.myQuillEditor.quill;
    },
  },

  methods: {
    post() {
      this.$confirm("是否发布留言?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          if (this.headline == "") {
            this.$message({
              type: "warning",
              message: "留言标题不能为空",
            });
          } else if (this.content == "") {
            this.$message({
              type: "warning",
              message: "留言内容不能为空",
            });
          } else if (this.value == "") {
            this.$message({
              type: "warning",
              message: "请选择留言类型",
            });
          } else {
            var that = this;
            request({
              method: "post",
              url: "http://127.0.0.1:5000/createMessage",
              data: {
                headline: that.headline,
                content: that.content,
                type: that.value,
                username: localStorage.username,
              },
            })
              .then(function (res) {
                if (res.data[0] == "success") {
                  localStorage.headline = that.headline;
                  localStorage.content = that.content;
                  localStorage.value = that.value;
                  localStorage.createTime = res.data[1];
                  localStorage.readCount = res.data[2];
                  localStorage.replyCount = res.data[3];
                  localStorage.messageId = res.data[0];
                  that.$message({
                    type: "success",
                    message: "发布成功",
                  });
                  that.$router.push({
                    path: "messageDetail",
                  });
                }
              })
              .catch(function (err) {
                console.log(err);
              });
          }
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消发布",
          });
        });
    },

    clear() {
      this.$confirm("是否清空留言?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.content = "";
          this.headline = "";
          this.value = "";
          this.$message({
            type: "success",
            message: "清空成功",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消清空",
          });
        });
    },

    // 准备富文本编辑器
    onEditorReady() {},
    // 富文本编辑器 失去焦点事件
    onEditorBlur() {},
    // 富文本编辑器 获得焦点事件
    onEditorFocus() {},
    // 富文本编辑器 内容改变事件
    onEditorChange() {},
  },
};
</script>


<style scoped>
</style>