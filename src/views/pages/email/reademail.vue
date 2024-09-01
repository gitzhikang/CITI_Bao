<script>
import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

import Layout from "../../layouts/main";
import PageHeader from "@/components/page-header";

import Toolbar from "./toolbar";

/**
 * Email-read component
 */
export default {
  page: {
    title: "Read Email",
    meta: [{ name: "description" }]
  },
  components: {
    Layout,
    PageHeader,
    Toolbar,
    ckeditor: CKEditor.component
  },
  data() {
    return {
      title: "Read Email",
      email: {},
      items: [
        {
          text: "Email",
          href: "/"
        },
        {
          text: "Inbox",
          active: true
        }
      ],
      showModal: false,
      editor: ClassicEditor,
      editorData: "<p>Content of the editor.</p>",
      origin: "",
      emailtitle: "",
      To: "To",
      sentDisable: false,
      hasReply: true,
      btn: "Reply",
      content: '<p>Content of the editor.</p><figure class="table"><table><tbody><tr><td>&nbsp;</td><td>dfesf</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>fes</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>fesfes</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table></figure>'
    };
  },
  methods:{
    direct(){
      this.$router.push({
        path: '/email'
      })
    },
    init(){
      let email_id = this.$route.query.index
      const path = '/getemail';
          this.$axios.post(path, {"index": email_id})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.email = res.data.email
                    this.origin = this.email[1]
                    this.emailtitle = this.email[3]
                    this.content = this.email[4]
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });
          this.sentDisable = false
    },
    toSend(){
      let to = document.getElementById("to")
      let subject = document.getElementById("subject")
      let email = {
        'origin': "zx",
        'target': to.value,
        'title': subject.value,
        'content': this.editorData,

      }

      const path = '/sendemail';
          this.$axios.post(path, {"email": email})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.$message({
                        type: 'success',
                        message: '发送成功!'
                      });
                  }
                  else{
                      this.$message.error('发送失败');
                  }
                  this.showModal = false
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });  
    },
    toReply(){
      this.showModal = true
      this.To = "To:" + this.origin
      this.sentDisable = true
      
    },
    toReturn(){
      let to = document.getElementById("to")
      let subject = document.getElementById("subject")
      if (subject.value.length > 0 && this.editorData.length > 0){
        let email = {
          'origin': "zx",
          'target': this.origin,
          'title': subject.value,
          'content': this.editorData,

        }
        this.$confirm('是否将此邮件放入草稿箱?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            const path = '/adddraft';
            this.$axios.post(path, {"email": email})
                .then((res) => {
                    if (res.data.state == "success")
                    {
                      this.$message({
                        type: 'success',
                        message: '已加入草稿箱!'
                      });
                    }
                    else{
                        this.$message.error('加入草稿箱失败');
                    }
                }
            ).catch((error) => {
                console.error(error);
            });  
            
          }).catch(() => {
            this.$message({
              type: 'info',
              message: '已丢弃'
            });          
          });
      }
      
      this.showModal = false
    }
  },
  created() {
    this.init()
    if (this.$route.query.type=="draft")
      this.btn = "Send"
    if (this.$route.query.type=="sent" || this.$route.query.type=="trash")
      this.hasReply = false
  }
};
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />

    <div class="row">
      <div class="col-12">
        <!-- Left sidebar -->
        <div class="email-leftbar card">
          <b-button variant="danger" @click="showModal = true">Compose</b-button>
          <div class="mail-list mt-4">
            <a href="javascript: void(0);" class="active" @click="direct()">
              <i class="mdi mdi-email-outline mr-2"></i> Inbox
              <span class="ml-1 float-right"></span>
            </a>
            <a href="javascript: void(0);" @click="direct()">
              <i class="mdi mdi-star-outline mr-2"></i>Starred
            </a>
            <a href="javascript: void(0);" @click="direct()">
              <i class="mdi mdi-file-outline mr-2"></i>Draft
            </a>
            <a href="javascript: void(0);" @click="direct()">
              <i class="mdi mdi-email-check-outline mr-2"></i>Sent Mail
            </a>
            <a href="javascript: void(0);" @click="direct()">
              <i class="mdi mdi-trash-can-outline mr-2"></i>Trash
            </a>
          </div>

        </div>
        <!-- End Left sidebar -->

        <!-- Right Sidebar -->
        <div class="email-rightbar mb-3">
          <div class="card">
            <div class="btn-toolbar p-3" role="toolbar">
              <Toolbar />
            </div>

            <div class="card-body">
              <div class="media mb-4">
                <img
                  class="d-flex mr-3 rounded-circle avatar-sm"
                  src="@/assets/images/users/avatar-2.jpg"
                  alt="Generic placeholder image"
                />
                <div class="media-body">
                  <h5 class="font-size-14 my-1">{{origin}}</h5>
                  <small class="text-muted">support@domain.com</small>
                </div>
              </div>

              <h4 class="mt-0 font-size-16">{{emailtitle}}</h4>
              <p v-html="content"></p>
              <hr />

              <a href="javascript: void(0);" class="btn btn-secondary waves-effect mt-4"  @click="toReply()" v-if="hasReply">
                <i class="mdi mdi-reply"></i> {{btn}}
              </a>
            </div>
          </div>
        </div>
        <!-- card -->
      </div>
      <!-- end Col-9 -->
    </div>
    <b-modal v-model="showModal" title="New Message" centered>
      <form name="send_email">
        <div class="form-group">
          <input type="email" class="form-control" :placeholder="To" id="to" :disabled="sentDisable"/>
        </div>

        <div class="form-group">
          <input type="text" class="form-control" placeholder="Subject" id="subject"/>
        </div>
        <div class="form-group">
          <ckeditor v-model="editorData" :editor="editor" id="content"></ckeditor>
        </div>
      </form>
      <template v-slot:modal-footer>
        <b-button variant="secondary" @click="toReturn()">Close</b-button>
        <b-button variant="primary" @click="toSend()">
          Send
          <i class="fab fa-telegram-plane ml-1"></i>
        </b-button>
      </template>
    </b-modal>
  </Layout>
</template>
