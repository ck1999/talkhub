<template>
    <div class="my-footer-root">
        <my-widget>
            <div slot="mytitle">
                <img src="@/static/logo.svg" alt="">
                Bitreon
            </div>
            <div class="description-wrapper">
              But I must explain to you how all
              this mistaken idea of denouncing
              pleasure and praising pain was 
              born and I will give you a complete 
              account of the system, and expound 
              the actual teachings of the great 
              explorer of the truth, the master-builder 
              of human happiness.No one rejects, 
              dislikes, or avoids 
              pleasure itself, because it
              is pleasure, but because those who 
              do not know how to
            pursue pleasure rationally encounter consequences that are 
            extremely painful. 
            </div>
             
        </my-widget>
        <my-widget :title="link.title" v-for="(link, i) in links" :key="i">
            <my-links :links="link.urls"></my-links>
        </my-widget>
    </div>
</template>
<style lang="scss">
.my-footer-root{
    display: flex;
    justify-content: space-around;
    background-color: #11233D;
}
.description-wrapper{
    max-width: 200px;
}
</style>

<script>
import MyWidget from '@/components/Footer/MyWidget'
import MyLinks from '@/components/Footer/MyLinks'
export default {
    data(){
        return {
            links:[
                {
                    title: 'About',
                    urls: [{
                        label: 'About the team',
                        href: '/about'
                    },
                    {
                        label: 'Affiliate Program',
                        href: '/about'
                    },
                    {
                        label: 'Careers',
                        href: '/about'
                    },
                    {
                        label: 'Privacy Policy',
                        href: '/about'
                    },
                    {
                        label: 'Security',
                        href: '/about'
                    },
                    {
                        label: 'Terms of Service',
                        href: '/about'
                    }]
                },
                {
                    title: 'Data',
                    urls: [{
                        label: 'Fees',
                        href: '/data'
                    },
                    {
                        label: 'Bitcoin / USD',
                        href: '/data'
                    },
                    {
                        label: 'Ethereum Futures',
                        href: '/data'
                    }]
                },
                {
                    title: 'References',
                    urls: [{
                        label: 'API',
                        href: '/references'
                    },
                    {
                        label: 'FAQ',
                        href: '/references'
                    },
                    {
                        label: 'Futures Guide',
                        href: '/references'
                    },
                    {
                        label: 'Perpetuals Guide',
                        href: '/references'
                    },
                    {
                        label: 'Trading On',
                        href: '/references'
                    }]
                },
                {
                    title: 'Social',
                    urls: [{
                        label: 'Blog',
                        href: '/social'
                    },
                    {
                        label: 'IRC',
                        href: '/social'
                    },
                    {
                        label: 'Reddit',
                        href: '/social'
                    },
                    {
                        label: 'Twitter',
                        href: '/social'
                    }]
                },
            ]
        }
    },
    components: {
        MyWidget,
        MyLinks,
    }
}
</script>
