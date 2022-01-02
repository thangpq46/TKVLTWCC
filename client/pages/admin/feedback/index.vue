<template>
    <div>
        {{feedbacks}}
    </div>
</template>
<script>

export default {
    async asyncData({ $axios}){
        const feedbacks = await $axios.$get('/feedview/')
        return { feedbacks}
    }
}
</script>