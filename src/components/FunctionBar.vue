<template>
    <div>
        <ul id="func-lis">
            <li>
                <i :class="icon"  @click="changeFollow()" @mouseenter="changeFollowIcon()" @mouseleave="changeFollowIcon()">{{follow_text}}</i>
                <pop-up :dialogFormVisible = 'dialogFormVisible'></pop-up>
            </li>
            <li>
                <i class="el-icon-warning-outline">数据不实反馈</i>
            </li>
            <li>
                <i class="el-icon-download">相关数据下载</i>
            </li>
            <li>
                <i class="el-icon-goods">进入投资洽谈</i>
            </li>
        </ul>
    </div>
</template>

<script>
import PopUp from "../components/FollowPopUp.vue"

export default {
    data(){
        return{
            dialogFormVisible: false,
            icon: "el-icon-star-off",
            follow_text: "关注企业"
        }
    },
    methods: {
        changeFollow(e) {
            if (!this.dialogFormVisible)
                this.dialogFormVisible = true;
            else
                this.dialogFormVisible = false;
        },

        changeFollowIcon(){
            if (this.icon == "el-icon-star-off"){
                this.icon = "el-icon-star-on"
            }else{
                this.icon = "el-icon-star-off"
            }
        }
    },
    components: { "pop-up" :PopUp},
    props: {
        followed: {
            type: Boolean,
            default: false
        }
    },
    watch:{
        followed(val, valOld){
            if (!this.followed)
            {
                this.icon = "el-icon-star-off";
                console.log("dddA")
            }

            else
            {
                this.icon = "el-icon-star-on";
                this.follow_text =  "取消关注"
                console.log("dddS")
            }
                
        }
    }
}
</script>

<style scoped>
div{
    width: 90vw;
    background-color: transparent;
    text-align: center;
    margin-top: 20px;
    padding-bottom: 5px;
}

ul{
   display: flex;
   justify-content: space-around;
   list-style: none;
}

ul li{
    font-size: 17px;
    color: rgb(236, 236, 236);
}

ul li:nth-child(n+1){
       
}
</style>