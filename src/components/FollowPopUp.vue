<template>
<el-dialog title="关注调查单" :visible.sync="Visible" id="dialog">
    <p>如果花上您宝贵的一分钟认真填写，并设置企业可见，将大大提高您与被关注者的沟通效率</p>
    <div>
        <el-checkbox-group v-model="checkboxGroup0" size="small" style="margin-top: 20px" class="follow-select">
            <el-checkbox label="ESG整体数据满意" border></el-checkbox>
            <el-checkbox label="ESG整体潜力数据满意" border></el-checkbox>
        </el-checkbox-group>
    </div>
    <p style="margin-top: 20px">（如果您选择了以上总体选项，则再选择的分别选项无效）</p>
    <div>
        <el-checkbox-group v-model="checkboxGroup1" size="small" style="margin-top: 20px" class="follow-select">
            <el-checkbox label="E数据满意" border></el-checkbox>
            <el-checkbox label="S数据满意" border></el-checkbox>
            <el-checkbox label="G数据满意" border></el-checkbox>
        </el-checkbox-group>
    </div>
    <div>
        <el-checkbox-group v-model="checkboxGroup2" size="small" style="margin-top: 20px" class="follow-select">
            <el-checkbox label="E潜力数据满意" border></el-checkbox>
            <el-checkbox label="S潜力数据满意" border></el-checkbox>
            <el-checkbox label="G潜力数据满意" border></el-checkbox>
        </el-checkbox-group>
    </div>
    <div slot="footer" class="dialog-footer">
        <el-button @click="Cancel()">取 消</el-button>
        <el-button type="primary" @click="Submit()">确 定</el-button>
    </div>
</el-dialog>
</template>

<script>
export default {
    data(){
        return{
            form: {
                name: '',
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: ''
            },
            formLabelWidth: '120px',
            Visible : false,
            radio3: '1',
            checkboxGroup0: [],
            checkboxGroup1: [],
            checkboxGroup2: [],
            resultList: []
        }
    },
    props: {
        dialogFormVisible: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        Cancel(){
            this.Visible = false;
        },

        Submit(){
            if (this.checkboxGroup0.includes("ESG整体数据满意")){
                this.checkboxGroup1 = []
                this.resultList.push("ESG整体数据满意")
            }
            if (this.checkboxGroup0.includes("ESG整体潜力数据满意")){
                this.checkboxGroup1 = []
                this.resultList.push("ESG整体潜力数据满意")
            }
            for (let i = 0; i < this.checkboxGroup1.length; i++){
                this.resultList.push(this.checkboxGroup1[i])
            }
            for (let i = 0; i < this.checkboxGroup2.length; i++){
                this.resultList.push(this.checkboxGroup2[i])
            }
            const path = '/follow';
            this.$axios.post(path, {"label": this.resultList})
                .then((res) => {
                    if (res.data.state == "success")
                    {
                        this.$message({
                            message: '恭喜你，这是一条成功消息',
                            type: 'success'
                        });
                    }
                    else{
                        if (res.data.errorcode == 1062)
                            this.$message.error('不能重复关注');
                    }

                }
            ).catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });
            this.Visible = false
        },

        
    },
    watch:{
        dialogFormVisible(val, valOld){
            if (!this.dialogFormVisible)
                this.Visible = true;
            else
                this.Visible = false;
        }
    }
}
</script>

<style scoped>
/deep/ .el-dialog{
    border-radius: 10px;
    background-color: rgb(190, 190, 190);
}

/deep/ .is-checked{
    color: black;
    background-color: rgb(54, 54, 54);
}

/deep/ .el-button--primary{
    background-color: black;
    border: solid 3px #409EFF;
    border-radius: 8px;
}
</style>