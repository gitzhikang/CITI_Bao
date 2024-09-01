<template>
  <div>
    <div class="btn-group mr-2 mb-2 mb-sm-0">
      <button type="button" class="btn btn-primary" @click="readAll()">
        <i class="fa fa-inbox"></i>
      </button>
      <button type="button" class="btn btn-primary" @click="disCard()">
        <i class="far fa-trash-alt"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{

    }
  },
  emits:['toDiscard', 'toReadAll'],
  methods:{
    disCard(){
      this.$emit('toDiscard')
    },
    readAll(){
      this.$emit('toReadAll')
    }
  }
}
</script>