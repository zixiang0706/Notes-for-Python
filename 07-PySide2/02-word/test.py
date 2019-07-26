a="我是人，你是猪"
import unicodedata
print(a.encode('UTF-8'))
print(a.encode('gbk'))

print(unicodedata.unicode(a))