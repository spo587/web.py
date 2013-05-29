import web
import random
import math

render = web.template.render('testdirectory/')
urls = (
	'/', 'boom','tatas'
)


		
class tatas:
	def GET(self):
		i=web.input(name=None)
		return render.index(i.name,'test')
		
	
		

	

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()