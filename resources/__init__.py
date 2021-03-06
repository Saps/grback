# rest-api приложения
from flask import Blueprint
from flask_restful import Api
from . import info
from . import sprav
from . import logic


RestApiBP = Blueprint('restapi', __name__,
                      template_folder='templates')
RestApi = Api(RestApiBP)

RestApi.add_resource(info.Info, '/info/<string:param_name>','/info')

RestApi.add_resource(sprav.SprMission, '/sprav/mission')
RestApi.add_resource(sprav.SprSpecType, '/sprav/spectypes')

RestApi.add_resource(logic.CalcStep, '/step')


#RestApi.add_resource(info.Info, '/info')

#RestApi.add_resource(user.UserLogin, '/user/login')
#RestApi.add_resource(user.UserLoginVK, '/user/login/vk/')
#RestApi.add_resource(user.UserLoginVKCallBack, '/user/login/vk/callback')

#RestApi.add_resource(user.UserLogout, '/user/logout')
#RestApi.add_resource(user.UserCurrent, '/user/current')
#RestApi.add_resource(user.UserRegister, '/user/register')
# RestApi.add_resource(user.GetUserData, '/user/getData')
#RestApi.add_resource(user.PutUserData, '/user/changeData')
#RestApi.add_resource(user.ChangePassword, '/user/changePassword/<string:usertoken>')
#RestApi.add_resource(user.SendingResetPasswordMail, '/user/forgotPassword')
#RestApi.add_resource(teams.CreateTeam, '/team/createTeam')
#RestApi.add_resource(teams.DeleteTeam, '/team/deleteTeam')
#RestApi.add_resource(teams.SendApplication, '/team/sendApplication')
#RestApi.add_resource(teams.Accept, '/team/accept')
#RestApi.add_resource(teams.KickFromTeam, '/team/kickFromTeam')
#RestApi.add_resource(teams.LeaveTeam, '/team/leaveTeam')
