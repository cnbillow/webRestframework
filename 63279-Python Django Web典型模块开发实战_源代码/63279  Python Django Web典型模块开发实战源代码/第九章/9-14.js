'/api': { //�滻�����ַ����
        target: 'http://127.0.0.1:8000/', //�����ַ
       changeOrigin: true, //�ɷ����
       pathRewrite: {
       '^/api': '' //��д�ӿڣ�ȥ��/api
        }
      }
