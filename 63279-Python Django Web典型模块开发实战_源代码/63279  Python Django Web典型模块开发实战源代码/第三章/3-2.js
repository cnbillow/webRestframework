<script>
export default {
  name: 'app',
  data () {
    return {
      one:['һ����Ŀ','һ����Ŀ','һ����Ŀ','һ����Ŀ','һ����Ŀ'],
      two:['������Ŀ1','������Ŀ2','������Ŀ3','������Ŀ4','������Ŀ5'],
      three:[],
      four:['�ļ���Ŀ','�ļ���Ŀ','�ļ���Ŀ','�ļ���Ŀ','�ļ���Ŀ'],
      flag:false
    }
  },
  methods: {
    open(index){
      var index=index+1;
      var i=index+"";
      this.three=['����Ŀ¼'+i,'����Ŀ¼'+i,'����Ŀ¼'+i,'����Ŀ¼'+i,'����Ŀ¼'+i]
      this.flag=true
    },
    close(){
      this.flag=false
    }
  },
}
</script>
