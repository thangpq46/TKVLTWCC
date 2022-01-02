<template>
    <div>
        <span if="status !=null">{{status}}</span>
        <span>Chọn chủ đề :<select v-model="feedback.topic">
                  <option value="Lỗi A" selected>Lỗi A</option>
                  <option value="Lỗi B">Lỗi B</option>
                  <option value="Lỗi C">Lỗi C</option>
        </select> </span>
        <span> Tiêu đề: <input type="text" v-model="feedback.title"> </span>
        <span> Tiêu đề: <input type="text" v-model="feedback.name"> </span>
        <span> Tiêu đề: <input type="text" v-model="feedback.email"> </span>
        <span> Tiêu đề: <input type="text" v-model="feedback.phone"> </span>
        <span> Tiêu đề: <input type="text" v-model="feedback.des"> </span>
        <button type="button" @click="submitFeed()">Guwir</button>
    </div>
</template>
<script>

export default {
  data() {
    return {
      feedback: {
        topic: '',
        title: '',
        name: '',
        email: '',
        phone: '',
        des:'',
      },
      status: null,
    }
  },
  methods: {
      async submitFeed(){
          const response = await this.$axios.$post('/submitfeed/',{
            feedback: this.feedback,
          })
          this.status = response.status
      }
  }
}
</script>
