# coding=utf-8
import sys
import time
# 打开文件
# with open('test.txt') as f:
# 	f.seek(0,2)
# 	while True:
# 		last_pos = f.tell()
# 		line = f.readline()
# 		if line:
# 			print line


class Tail():
	def __init__(self,file_name,callback=sys.stdout.write):
		self.file_name = file_name
		self.callback = callback
	def follow(self,n=10):


		with open(self.file_name) as f:
			self._file = f
			self._file.seek(0,2)
			self.file_length = self._file.tell()
			self.showLastLine(n)
			while True:
				line = self._file.readline()
				if line:
					self.callback(line)
		try:
			pass
		except Exception,e:
			print '打开文件失败，囧，看看文件是不是不存在，或者权限有问题'
			print e
	def showLastLine(self, n):
		# 一行大概100个吧 
		len_line = 100
		print -n*len_line
		self._file.seek(-n*len_line, 2)
		last_words = self._file.read()
	
		if last_words.count('\n')>10:

			last_lines = last_words.split('\n')[-10:]
			for line in last_lines:
				self.callback(line+'\n')
		else:
			
			print last_words.count('\n')


# print range(20)[-10:]
# py_tail = Tail('test.txt')
# py_tail.follow()

d1 = {'a':1,'b':2}
d2 = {'b':2,'a':1}
import json
print json.dumps(d1)

# def test_tail(line):
#     print 'xx'+line+'xx'

# py_tail1 = Tail('test.txt', test_tail)
# py_tail1.follow()
