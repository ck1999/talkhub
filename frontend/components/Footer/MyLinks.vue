<template>
    <div class="links">
        <a  :href="link.href"
            v-for="(link, i) in links"
            :key="i">
            {{link.label}}
        </a>
    </div>
</template>
<script>
export default {
    props: {
        links: {
            type: Array,
            required: true,
        }
    }
}
</script>
<style lang="scss">
    .links {
        display: flex;
        flex-direction: column;
    }
    a {
        color: #566B8A;
        text-decoration: none;
    }
</style>

