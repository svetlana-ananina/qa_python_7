class URLS:
    SERVER_URL = 'http://qa-scooter.praktikum-services.ru'


class ENDPOINTS:
    CREATE_COURIER  = '/api/v1/courier'
    LOGIN_COURIER   = '/api/v1/courier/login'
    DELETE_COURIER  = '/api/v1/courier/'              # '/api/v1/courier/:id'
    CREATE_ORDER    = '/api/v1/orders'                  # Метод POST
    GET_ORDER_LIST  = '/api/v1/orders'                  # Метод GET
    BY_COURIER_ID   = '?courierId='                      # '?courierId=<:id>'


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
    OK_KEY      = 'ok'
    ID_KEY      = 'id'
    LOGIN       = 'login'
    PASSWORD    = 'password'
    TRACK       = 'track'
    ORDERS      = 'orders'


class ORDER_FIELDS:
    ID              = 'id'
    COURIER_ID      = 'courierId'
    FIRST_NAME      = 'firstName'
    LAST_NAME       = 'lastName'
    ADDRESS         = 'address'
    METRO_STATION   = 'metroStation'
    PHONE           = 'phone'
    RENT_TIME       = 'rentTime'
    DELIVERY_DATE   = 'deliveryDate'
    TRACK           = 'track'
    COLOR           = 'color'
    COMMENT         = 'comment'
    CREATED_AT      = 'createdAt'
    UPDATED_AT      = 'updatedAt'
    STATUS          = 'status'

    COLOR_BLACK     = 'BLACK'
    COLOR_GREY      = 'GREY'


ORDER_DATA = {
    'firstName'     : "Иван",
    'lastName'      : "Иванов",
    'address'       : "Русаковская улица, 22",
    'metroStation'  : 4,
    'phone'         : "+79999999999",
    'rentTime'      : 1,
    'deliveryDate'  : "01.01.2024",
    'comment'       : "Позвоните за полчаса"
}

