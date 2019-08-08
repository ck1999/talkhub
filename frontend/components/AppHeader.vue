<template>
<div class="header-root">
    <div class="header-top">
        <img class="project-logo" src="@/static/logo.svg" alt="">
        <div class="header-buttons">
            <div class="header-button">
                Language
            </div>
            <div class="header-button">
                About
            </div>
            <div class="header-button">
                Sign up
            </div>
            <div class="login-button">
                Sign in
            </div>
        </div>
    </div>

    <div class="header-center">
        <div class="header-slogan">
            But i must must must must must must must must 
        </div>
        <div class="header-description">
            No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. 
        </div>
        <div>
            <button class="header-try-button" @click="$modal.show('mymodal')">Try simulated trading</button>
        </div>
    </div>

    <div class="header-bottom-labels">
        <div class="header-bottom-button">
            64.3 billion <span>per month</span>
        </div>
         <div class="header-bottom-button">
            985.32 billion <span>per year</span>
        </div>
        <div class="header-bottom-button">
            6.09 billion <span>per day</span>
        </div>
    </div>

    <no-ssr>
        <modal name='mymodal'>
            <div class='modal'>
                <div class='modal-header'>
                    Оформить заявку:
                </div>
                <div class='modal-body'>
                    <div class='modal-input'>
                        Имя:
                        <input v-model="name">
                    </div>
                    <div class='modal-input'>
                        Email:
                        <input v-model="email">
                    </div>
                    <div class='modal-input'>
                        Телефон:
                        <input v-model="phone">
                    </div>
                </div>
                <div class='modal-footer'>
                    <button class='modal-footer' @click="submit"> Отправить </button>
                </div>
            </div>
        </modal>
    </no-ssr>
</div> 
</template>
<style lang="scss">
.modal {
    background-color: #242424;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    width: 100%;
    height: 100%;
}
.modal-header {
    color: white;
}
.modal-body {
    display: flex;
    flex-direction: column;
}
.modal-input {
    color: #858585;
    display: flex;
    justify-content: space-between;
}
.modal-footer {
    background: linear-gradient(103.76deg, #193EC2 -7.71%, #660987 92.84%);
}
.header-root {
    min-height: 100vh;
    background-color: #11233D;
    background-image: url(/bgheader.svg);
    background-position: right center;
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: relative;
}
.header-top{
    display: flex;
    justify-content: space-between;
    align-items: center;

    img.project-logo, div.header-buttons {
        padding: 2em;
    }
    img.project-logo {
        height: 3em;
    }
    .login-button{
        background-image: url(/login.svg);
        background-repeat: no-repeat;
        background-position: center;
        padding: 1em 1.5em;
        color: white;

        &:hover {
            color: yellow;
            cursor: pointer;
        }        
    }

    .header-buttons{
        display: flex;
        justify-content: space-between;
        align-items: center;

        .header-button{
            font-weight: 300;
            padding: 1em 3.5em;
            color: white;
            &:hover {
                color: red;
                cursor: pointer;
                text-decoration: underline;
            }
        }
    }
}
.header-center {
    max-width: 400px;
    display: flex;
    flex-direction: column;
    margin-left: 6em;
    margin-top: 6em;
    .header-slogan {
        font-size: 2em;
        color: white;
    }
    .header-description {
        color: #566B8A;
        font-family: 'Roboto';
        font-weight: normal;
        margin-top: 1em;
    }
    .header-try-button{
        margin-top: 2em;
        padding: 1em 2em;
        font-weight: 700;
        width: 12em;
        text-align: center;
        color: white;
        background-image: url(/trytrading.svg);
        background-repeat: no-repeat;
        background-position: center;
        &:hover {
            color: yellow;
            cursor: pointer;
        }
    }
}
.header-bottom-labels{
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    position: absolute;
    bottom: 10px;
    width: 100%;
    left: 0;
    .header-bottom-button{
        background-color: #0B5B89;
        padding: .8em 1.7em;
        margin: .5em;
        font-size: 2em;
        span {
            font-size: .5em;
            color: #87A6D4;
            font-family: 'Roboto';
        }
    }
}
</style>
<script>
export default {
    data(){
        return {
            phone: '',
            name: '',
            email: ''
        }
    },
    methods:{
        submit(){
            this.$axios.post('/api/submit', {
                phone: this.phone,
                email: this.email,
                name: this.name
            }).then(success=>{
                console.log('success', success)
            }).catch(err=>{
                console.log('err', err)
            })
        }
    }
}
</script>
