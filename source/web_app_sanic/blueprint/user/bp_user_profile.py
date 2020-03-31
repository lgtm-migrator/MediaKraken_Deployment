from common import common_global
from sanic import Blueprint

blueprint_user_profile = Blueprint('name_blueprint_user_profile', url_prefix='/user')


@blueprint_user_profile.route('/user_profile', methods=['GET', 'POST'])
@common_global.jinja_template.template('bss_user/bss_user_profile.html')
@common_global.auth.login_required
async def url_bp_user_profile(request):
    return {}
