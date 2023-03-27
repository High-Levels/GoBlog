from app import app
from app.controllers import auth,user,category,tag

#Auth
app.route('/login',methods=['POST'])(auth.login)


#User
app.route('/register',methods=['POST'])(user.createUser)
app.route('/profile/<id>',methods=['GET'])(user.readUser)
app.route('/update/profile/<id>',methods=['PATCH'])(user.updateUser)
app.route('/delete/profile/<id>',methods=['DELETE'])(user.deleteUser)


#CATEGORY
app.route('/list/categories',methods = ['GET'])(category.listCategory)
app.route('/create/category',methods = ['POST'])(category.createCategory)
app.route('/read/category/<id>',methods = ['GET'])(category.readCategory)
app.route('/update/category/<id>',methods = ['PATCH'])(category.updateCategory)
app.route('/delete/category/<id>',methods = ['DELETE'])(category.deleteCategory)

#TAGS
app.route('/list/tags',methods = ['GET'])(tag.listTag)
app.route('/create/tag',methods = ['POST'])(tag.createTag)

