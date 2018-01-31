from app import app_object,db
from app.controllers import controller_user, controller_home

# APPLICATION ROUTES
app_object.add_url_rule('/signup','add_new_user',controller_user.add_new_user,methods=['POST'])
app_object.add_url_rule('/login','login',controller_user.login,methods=['PUT'])
app_object.add_url_rule('/feed','get_feed',controller_home.get_feed,methods=['GET'])
app_object.add_url_rule('/sentiment','sentiment',controller_home.sentiment,methods=['POST'])

if __name__ == '__main__':
  app_object.run(host='0.0.0.0', port=app_object.config['PORT'])
