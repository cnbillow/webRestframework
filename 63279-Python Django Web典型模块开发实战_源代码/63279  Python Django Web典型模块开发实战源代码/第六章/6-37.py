class VIP(object):
	������
	��֤VIPȨ��
	������
    def has_permission(self,request,view):
        if request.user.user_type<2:
            return False
        return True
class SVIP(object):
	������
	��֤SVIPȨ��
	������
    def has_permission(self,request,view):
        if request.user.user_type<3:
            return False
        return True
