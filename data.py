class URLS:
    SERVER_URL = 'http://qa-scooter.praktikum-services.ru'

class ENDPOINTS:
    CREATE_COURIER  = '/api/v1/courier'
    LOGIN_COURIER   = '/api/v1/courier/login'
    DELETE_COURIER  = '/api/v1/courier/'              # '/api/v1/courier/:id'

_debug = True
#_debug = False

class STATUS_CODES:
    CREATED     = 201
    BAD_REQUEST = 400
    CONFLICT    = 409
    OK          = 200
    NOT_FOUND   = 404

class RESPONSE_MESSAGES:
    OK_TEXT                 = 'ok'
    CREATE_BAD_REQUEST      = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_USED_TEXT = 'Этот логин уже используется'
    LOGIN_BAD_REQUEST       = 'Недостаточно данных для входа'
    LOGIN_NOT_FOUND         = 'Учетная запись не найдена'

class RESPONSE_KEYS:
    MESSAGE_KEY = 'message'
    OK_KEY  = 'ok'
    ID_KEY  = 'id'
    LOGIN = 'login'
    PASSWORD = 'password'

