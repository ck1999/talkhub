<template>
    <div>
        <div class="widget-title">
            <slot name="mytitle">
                {{title}}
            </slot> 
        </div>
        <div class="widget-description">
            <slot>
                {{description}}
            </slot> 
        </div>
        
    </div>
</template>
<script>
export default {
    props:{
        title: {
            type: String,
            default: ''
        },
        description: {
            type: String,
            default: ''
        }
    }
}
</script>
<style lang="scss">
    .widget-title {
        font-family: 'Roboto';
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 30px;
        letter-spacing: 0.02em;

        color: #FFFFFF;

    }
    .widget-description {
        font-family: Roboto;
        font-style: normal;
        font-weight: normal;
        font-size: 12px;
        line-height: 20px;
        letter-spacing: 0.02em;

        color: #566B8A;
    }
</style>

