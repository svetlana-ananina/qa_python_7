class URLS:
    SERVER_URL = 'http://qa-scooter.praktikum-services.ru'

class ENDPOINTS:
    CREATE_COURIER  = '/api/v1/courier'
    LOGIN_COURIER   = '/api/v1/courier/login'
    DELETE_COURIER  = '/api/v1/courier/{}'           # '/api/v1/courier/:id'

_debug = True
#_debug = False

class STATUS_CODES:
    CREATED     = 201
    BAD_REQUEST = 400
    CONFLICT    = 409
    OK          = 200

class RESPONSE_MESSAGES:
    OK_TEXT = 'ok'
    MESSAGE_TEXT = 'message'
    NOT_ALL_DATA_RECEIVED_TEXT = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_USED_TEXT = 'Этот логин уже используется'
