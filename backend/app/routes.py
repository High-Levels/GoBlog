from app import app
from app.controllers import auth,user,category,tag, article, articleLikes, comment

#Auth
app.route('/login',methods=['POST'])(auth.login)


#User
app.route('/register',methods=['POST'])(user.createUser)
app.route('/profile/<id>',methods=['GET'])(user.readUser)
app.route('/update/profile/<id>',methods=['PATCH'])(user.updateUser)
app.route('/delete/profile/<id>',methods=['DELETE'])(user.deleteUser)
app.route('/activate/<id>',methods=['GET'])(user.activateUser)
app.route('/forgot',methods=['POST'])(user.forgotPassword)
app.route('/changepassword/<id>',methods=['GET'])(user.getChangePassword)
app.route('/changepassword/<id>',methods=['PATCH'])(user.setChangePassword)




#CATEGORY
app.route('/list/categories',methods = ['GET'])(category.listCategory)
app.route('/create/category',methods = ['POST'])(category.createCategory)
app.route('/read/category/<id>',methods = ['GET'])(category.readCategory)
app.route('/update/category/<id>',methods = ['PATCH'])(category.updateCategory)
app.route('/delete/category/<id>',methods = ['DELETE'])(category.deleteCategory)

#TAGS
app.route('/list/tags',methods = ['GET'])(tag.listTag)
app.route('/create/tag',methods = ['POST'])(tag.createTag)


# Article
app.route('/create/article', methods=["POST"])(article.createArticle)
app.route('/read/article/<id>', methods=["GET"])(article.readArticle)
app.route('/update/article/<id>', methods=["PUT"])(article.updateArticle)
app.route('/delete/article/<id>', methods=["DELETE"])(article.deleteArticle)
app.route('/list/articles', methods=["GET"])(article.readAllArticle)
app.route('/list/userRecentArticles/<id>', methods=["GET"])(article.userRecentArticle)


# Comment
app.route('/create/comment', methods=["POST"])(comment.createComment)
app.route('/delete/comment/<id>', methods=["DELETE"])(comment.deleteComment)


# Like
app.route('/update/like/<id>', methods=["POST"])(articleLikes.updateLike)
app.route('/read/like/<id>', methods=["GET"])(articleLikes.readLike)
