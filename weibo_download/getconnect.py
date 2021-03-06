# -*- coding:utf-8 -*-
import sys
import MySQLdb
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

class GetConnect(object):
	def __init__(self):
		self.host = None
		self.user = None
		self.passwd = None
		self.port = None
		self.db = None
		self.charset = None
		self.use_unicode = None
		self.initParams()
		self.conn = None
		self.cur = None
		self.initDb()

	def initParams(self):
		'从配置文件中初始化参数变量'
		cf = ConfigParser.ConfigParser()
		cf.read('config.ini')
		self.host = cf.get('db', 'host')
		self.port = int(cf.get('db', 'port'))
		self.user = cf.get('db', 'user')
		self.passwd = cf.get('db', 'passwd')
		self.db = cf.get('db', 'db')
		self.charset = cf.get('db', 'charset')
		self.use_unicode = cf.get('db', 'use_unicode')

	def initDb(self):
		try:
			self.conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, \
							passwd=self.passwd, db=self.db, charset=self.charset, use_unicode=self.use_unicode)
			self.cursor = self.conn.cursor()
		except MySQLdb.Error, e:
			print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
			print 'Failed to connect to database! Please check your config file and confirm your database is open'
			sys.exit(-1)
		print 'Success connect database'

	def getCount(self, sql):
		count = self.cursor.execute(sql)
		return count
		
	def getData(self, sql):
		count = self.cursor.execute(sql)
		print 'There has %d rows record' % count
		if count != 0:
			results = self.cursor.fetchall()
			return results
		else:
			return None

	def executeDB(self, sql):
		self.cursor.execute(sql)
		self.conn.commit()
		print 'Success execute sql'

	def closeResource(self):
		if self.cur:
			self.cur.close()
		if self.conn:
			self.conn.close()


def main():
	pass
if __name__ == '__main__':
	main()