# 格式化输出的三种模式
name='Tom'
age=25
classgroup=6
partner='Jerry'
gender='male'
# 1.print('{},{}...'.format(变量1，变量2...))
print('{},{}'.format(name,age))
# 2.print("%s字符串 %d十进制整数 %c字符 %o八进制 %x十六进制 %e科学计数法 %f浮点数"%(变量1，变量2...))
print("%s的年龄是%d"%(name,age))
# 3.print(f'{变量1}直接输出部分{变量2}...')
print(f'{name}的年龄是{age}')