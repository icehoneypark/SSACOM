<template>
  <h3>loginpage</h3>
  <div>
    <input-group>
      <input-text>이메일</input-text>
      <input type="text">
    </input-group>
  </div>
  <div>
    <input-group>
      <input-text>비번</input-text>
      <input type="text">
    </input-group>
  </div>
  <button type="submit" class="btn btn-sm btn-primary m-1">로그인</button>



</template>

<script>
import { mapActions } from "vuex";

export default {
  name: 'Login',
  data() {
    return {
      email:'',
      password:'',
      error: {
        email: false,
        password: false,
      },
      isCheck:false,
      isAlert:false,

    }
  },
  components:{},
  created() {},
  watch : {
    email: function() {
      this.email = this.email.trim().toLowerCase(); //대문자 방지
    }
  },
  methods: {
    ...mapActions(memberStore, ["memberConfirm", "signInMemberInfo"]),
    async login() {
      const memberInfo = {
        email: this.email,
        password: this.password,
      }
      await this.memberConfirm(memberInfo);
      let accessToken = localStorage.getItem("accessToken");
      if (this.isSignin) {
        await this.signInMemberInfo(accessToken);
        this.$router.push({name:"home"});  // 일단은 메인화면으로 보내는데, 나중에 대시보드로 돌려놓던가 해야 함
      }else{
        this.isAlert = true;
      }
    },
    checkForm() {
      if (this.email.trim().length >= 0 && !EmailValidator.validate(this.email))
        this.error.email = true;
      else this.error.email = false;
    }
  }


}
</script>

<style>

</style>