main = Blueprint('language_blueprint', __name__)
@main.route('/')
def get_languages():
    has_access = Security.verify_token(request.headers)

    if has_access:
        try:
            languages = LanguageService.get_language()
            if (len(languages)> 0)
                return jsonify({'languages': languages, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "ERROR", 'success': False})
            
        except Exception as ex:
            return jsonify({'message': "ERROR", 'success': False})
    else:
        response= jsonify ({'message': 'Unauthorized'})
        return response, 401