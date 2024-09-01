<script>
import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

import Layout from "../../layouts/main";
import PageHeader from "@/components/page-header";

import Toolbar from "./toolbar";

/**
 * Email-inbox component
 */
export default {
  page: {
    title: "Inbox",
    meta: [{ name: "description" }]
  },
  components: { Layout, PageHeader, Toolbar, ckeditor: CKEditor.component },
  data() {
    return {
      emailData: [],
      paginatedEmailData: [],
      title: "Inbox",
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
      // page number
      currentPage: 1,
      // default page size
      perPage: 15,

      // start and end index
      startIndex: 1,
      endIndex: 15,
      showModal: false,
      editor: ClassicEditor,
      editorData: "<p>Content of the editor.</p>",
      choosed: [],
      isInbox: true,
      isStarrend: false,
      isDraft: false,
      isSent: false,
      isTrash: false,
      inbox_total: 0,
      star_total: 0,
      draft_total: 0,
      sent_total: 0,
      trash_total: 0
    };
  },
  computed: {
    rows() {
      return this.emailData.length;
    }
  },
  created() {
    this.getInboxEmails()

    this.startIndex = 0;
    this.endIndex = this.perPage;

    this.paginatedEmailData = this.emailData.slice(
      this.startIndex,
      this.endIndex
    );
  },
  methods: {
    getInboxEmails(){
      this.isInbox = true
      this.isStarrend = false
      this.isDraft = false
      this.isSent = false
      this.isTrash = false
      const path = '/getemails';
          this.$axios.post(path, {"user": 'test'})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.emailData = []
                    console.log(res.data)
                      for (let i = 0; i < res.data.unreaded.length; i++){
                        this.emailData.push({
                          index: res.data.unreaded[i][0],
                          unread: false,
                          title: res.data.unreaded[i][3],
                          subject: res.data.unreaded[i][4],
                          date: res.data.unreaded[i][10],
                          starred: false
                        })
                      }
                      for (let i = 0; i < res.data.readed.length; i++){
                        this.emailData.push({
                          index: res.data.readed[i][0],
                          unread: true,
                          title: res.data.readed[i][3],
                          subject: res.data.readed[i][4],
                          date: res.data.readed[i][10],
                          starred: false
                        })

                      }
                      for (let i = 0; i < res.data.starred.length; i++){
                        this.emailData.push({
                          index: res.data.starred[i][0],
                          unread: true,
                          title: res.data.starred[i][3],
                          subject: res.data.starred[i][4],
                          date: res.data.starred[i][10],
                          starred: true
                        })

                      }
                      this.startIndex = 0;
                      this.endIndex = this.perPage;
                      this.inbox_total = this.emailData.length

                      this.paginatedEmailData = this.emailData.slice(
                        this.startIndex,
                        this.endIndex
                      );
                      
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });
    },

    getStarredEmails(){
      this.isInbox = false
      this.isStarrend = true
      this.isDraft = false
      this.isSent = false
      this.isTrash = false
      const path = '/getemails';
          this.$axios.post(path, {"user": 'test'})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.emailData = []
                    for (let i = 0; i < res.data.starred.length; i++){
                        
                        this.emailData.push({
                          index: res.data.starred[i][0],
                          unread: true,
                          title: res.data.starred[i][3],
                          subject: res.data.starred[i][4],
                          date: res.data.starred[i][10],
                          starred: true
                        })

                      }
                      this.startIndex = 0;
                      this.endIndex = this.perPage;
                      this.star_total = this.emailData.length

                      this.paginatedEmailData = this.emailData.slice(
                        this.startIndex,
                        this.endIndex
                      );
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });
    },

    onPageChange() {
      this.startIndex = (this.currentPage - 1) * this.perPage;
      this.endIndex = (this.currentPage - 1) * this.perPage + this.perPage;

      this.paginatedEmailData = this.emailData.slice(
        this.startIndex,
        this.endIndex
      );
    },

    getDraftEmails(e){
      this.isInbox = false
      this.isStarrend = false
      this.isDraft = true
      this.isSent = false
      this.isTrash = false
      const path = '/getemails';
          this.$axios.post(path, {"user": 'test'})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.emailData = []
                    for (let i = 0; i < res.data.drafted.length; i++){
                        
                        this.emailData.push({
                          index: res.data.drafted[i][0],
                          title: res.data.drafted[i][3],
                          subject: res.data.drafted[i][4],
                          date: res.data.drafted[i][10],
                          starred: false
                        })
                      }
                      this.startIndex = 0;
                      this.endIndex = this.perPage;
                      this.draft_total = this.emailData.length

                      this.paginatedEmailData = this.emailData.slice(
                        this.startIndex,
                        this.endIndex
                      );
                      
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });
    },

    getSentEmails(){
        this.isInbox = false
        this.isStarrend = false
        this.isDraft = false
        this.isSent = true
        this.isTrash = false
          const path = '/getemails';
          this.$axios.post(path, {"user": 'test'})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                      this.emailData = []
                      for (let i = 0; i < res.data.sent.length; i++){
                        this.emailData.push({
                          index: res.data.sent[i][0],
                          title: res.data.sent[i][3],
                          subject: res.data.sent[i][4],
                          date: res.data.sent[i][10],
                          starred: false
                        })
                      }
                      this.startIndex = 0;
                      this.endIndex = this.perPage;
                      this.sent_total = this.emailData.length

                      this.paginatedEmailData = this.emailData.slice(
                        this.startIndex,
                        this.endIndex
                      );
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });
    },

    getTrashEmails(e){
      this.isInbox = false
      this.isStarrend = false
      this.isDraft = false
      this.isSent = false
      this.isTrash = true
      const path = '/getemails';
          this.$axios.post(path, {"user": 'test'})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                      this.emailData = []
                      for (let i = 0; i < res.data.trashed.length; i++){
                        this.emailData.push({
                          index: res.data.trashed[i][0],
                          title: res.data.trashed[i][3],
                          subject: res.data.trashed[i][4],
                          date: res.data.trashed[i][10],
                          starred: false
                        })
                      }
                      this.startIndex = 0;
                      this.endIndex = this.perPage;
                      this.trash_total = this.emailData.length

                      this.paginatedEmailData = this.emailData.slice(
                        this.startIndex,
                        this.endIndex
                      );
                      console.log(this.emailData)
                  }
                  else{
                      
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });  
    },
    toChoose(index){
      let has = false
      let pos = 0
      for (let i = 0; i < this.choosed.length; i++){
        if (this.choosed[i].index == this.paginatedEmailData[index].index)
          has = true
          pos = i
      }
      if (!has){
        this.choosed.push(this.paginatedEmailData[index])
      }
      else{        
        this.choosed.splice(pos, 1)       
      }
    },
    toTrash(){
      
    },
    toDiscard(){
      this.$confirm('此操作将永久删除该邮件且不可恢复, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          const path = '/throwemail';
          this.$axios.post(path, {"emails": this.choosed})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    this.$message({
                      type: 'success',
                      message: '删除成功!'
                    });
                  }
                  else{
                      this.$message({
                        type: 'success',
                        message: '删除失败!'
                      });
                  }
                  this.choosed = []
              }
              
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });  
          this.getInboxEmails()
          
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
      
    },
    toStarred(e, index){
      console.log(this.emailData[index])
        const path = '/staremail';
          this.$axios.post(path, {"email": this.emailData[index]})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    if (res.data.op == 1)
                      e.target.className = "star-toggle fas fa-star"
                    else
                      e.target.className = "star-toggle far fa-star"
                  }
                  else{
                      this.$notify.error({
                        title: '错误',
                        message: '收藏失败'
                      });
                  }
              }
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });  
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
    toRead(index){
      let type = ""
      if (this.isSent)
        type = "sent"
      if (this.isDraft)
        type = "draft"
      if (this.isTrash)
        type = "trash"
      this.$router.push({
        path: '/email/read',
        query: {
          index:index,
          type: type
        }
      })
    },
    toReturn(){
      console.log("subject.value.length")
      let to = document.getElementById("to")
      let subject = document.getElementById("subject")
      
      if (subject.value.length > 0 && this.editorData.length > 0){
        let email = {
          'origin': "zx",
          'target': to.value,
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
    },
    toReadAll(){
      this.$confirm('把所有选中邮件已读, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          const path = '/readall';
          this.$axios.post(path, {"emails": this.choosed})
              .then((res) => {
                  if (res.data.state == "success")
                  {
                    for (let i = 0; i < this.paginatedEmailData.length; i++){
                      let node = document.getElementById("chk-" + i)
                      console.log(node)
                      node.checked = false
                    }
                    this.$message({
                      type: 'success',
                      message: '全部已读!'
                    });
                  }
                  else{
                      this.$message({
                        type: 'success',
                        message: '读取失败!'
                      });
                  }
                  this.choosed = []
              }
              
          ).catch((error) => {
             // eslint-disable-next-line
              console.error(error);
          });  
          this.getInboxEmails()
          
        }).catch(() => {
       
        });
    }
  }
};
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <!-- Right Sidebar -->
      <div class="col-12">
        <div class="email-leftbar card">
          <b-button variant="danger" @click="showModal = true">Compose</b-button>
          <div class="mail-list mt-4">
            <a href="javascript: void(0);" :class="isInbox ? 'active' : ''"  @click="getInboxEmails()">
              <i class="mdi mdi-email-outline mr-2"></i> Inbox
              <span class="ml-1 float-right">({{inbox_total}})</span>
            </a>
            <a href="javascript: void(0);" :class="isStarrend ? 'active' : ''" @click="getStarredEmails()">
              <i class="mdi mdi-star-outline mr-2"></i>Starred
              <span class="ml-1 float-right">({{star_total}})</span>
            </a>
            <a href="javascript: void(0);" :class="isDraft ? 'active' : ''" @click="getDraftEmails()">
              <i class="mdi mdi-file-outline mr-2"></i>Draft
              <span class="ml-1 float-right">({{draft_total}})</span>
            </a>
            <a href="javascript: void(0);" :class="isSent ? 'active' : ''" @click="getSentEmails()">
              <i class="mdi mdi-email-check-outline mr-2"></i>Sent Mail
              <span class="ml-1 float-right">({{sent_total}})</span>
            </a>
            <a href="javascript: void(0);" :class="isTrash ? 'active' : ''" @click="getTrashEmails()">
              <i class="mdi mdi-trash-can-outline mr-2"></i>Trash
              <span class="ml-1 float-right">({{trash_total}})</span>
            </a>
          </div>
        </div>
        <div class="email-rightbar mb-3">
          <div class="card">
            <div class="btn-toolbar p-3">
              <Toolbar @toDiscard="toDiscard()" @toReadAll="toReadAll()"/>
            </div>
            <div class="mt-3">
              <ul class="message-list">
                <li
                  v-for="(email,index) in paginatedEmailData"
                  :key="email.index"
                  :class="{ 'unread': `${email.unread}` === 'true' }"
                >
                  <div class="col-mail col-mail-1">
                    <div class="checkbox-wrapper-mail" >
                      <input :id="`chk-${index}`" type="checkbox" @click="toChoose(index)" :disabled="isTrash"/>
                      <label :for="`chk-${index}`"></label>
                    </div>
                    <span 
                    :class="email.starred ? 'star-toggle fas fa-star' : 'star-toggle far fa-star'" 
                    @click="toStarred($event, index)"
                     v-if="!isTrash">
                     </span>
                    <a class="title">{{email.title}}</a>
                  </div>
                  <div class="col-mail col-mail-2" @click="toRead(email.index)">
                    <a class="subject">{{email.subject}}</a>
                    <div class="date">{{email.date}}</div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div class="row justify-content-md-between align-items-md-center">
            <div class="col-xl-7">Showing {{startIndex}} - {{endIndex}} of {{rows}}</div>
            <!-- end col-->
            <div class="col-xl-5">
              <div class="text-md-right float-xl-right mt-2 pagination-rounded">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  @input="onPageChange"
                ></b-pagination>
              </div>
            </div>
            <!-- end col-->
          </div>
        </div>
      </div>
    </div>
    <b-modal v-model="showModal" title="New Message" centered>
      <form name="send_email">
        <div class="form-group">
          <input type="email" class="form-control" placeholder="To" id="to"/>
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