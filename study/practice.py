import cmath;
print("-----------数据类型st-------------------");
bool = False ;
unbool = True ;
print(bool);
print(unbool);
a=1;
b=2;
c=3;
print(a)
print(b,c)
del a;
del b, c;
#print(a) #删除a变量后，再调用a变量会报错

'''
number 类型
知识点1 类型转换
知识点2 math函数 cmatch函数
'''
print('---数字类型--')
a='1'
a=int(a)
print(a==1)
print(cmath.sin(1))
print('---字符类型--')
'''
字符类型：python没有单独的字符 只有字符串，单个字符也是字符串

字符串的格式化：和c语言有点像
字符串的三引号：三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
'''
var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print ("My name is %s and weight is %d kg!" % ('Zara', 21))
#print ("My name is %s and weight is %d kg!" % ('Zara', '21')) 会报错

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)

print(u'Hello World !')

print('---列表类型--')
