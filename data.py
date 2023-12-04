_to_print = True


class URLS:
    SERVER_URL = 'http://qa-scooter.praktikum-services.ru'


class ENDPOINTS:
    CREATE_COURIER  = '/api/v1/courier'                 # POST '/api/v1/courier'
    LOGIN_COURIER   = '/api/v1/courier/login'           # POST '/api/v1/courier/login'
    DELETE_COURIER  = '/api/v1/courier/'                # DELETE '/api/v1/courier/:id'
    CREATE_ORDER    = '/api/v1/orders'                  # POST '/api/v1/orders'
    GET_ORDER_LIST  = '/api/v1/orders'                  # GET '/api/v1/orders'
    GET_ORDER       = '/api/v1/orders/track'            # GET '/api/v1/orders?t=<track_id>'
    BY_TRACK        = '?t='                              # '?t=<track>'
    ACCEPT_ORDER    = '/api/v1/orders/accept/'          # PUT '/api/v1/orders/accept/:id'

    BY_COURIER_ID   = '?courierId='                     # '?courierId=<id>'         ???


class STATUS_CODES:
    CREATED     = 201
    BAD_REQUEST = 400
    CONFLICT    = 409
    OK          = 200
    NOT_FOUND   = 404


class RESPONSE_MESSAGES:
    OK_TEXT                     = 'ok'
    CREATE_BAD_REQUEST          = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_USED_TEXT     = 'Этот логин уже используется'
    LOGIN_BAD_REQUEST           = 'Недостаточно данных для входа'
    LOGIN_NOT_FOUND             = 'Учетная запись не найдена'
    DELETE_COURIER_BAD_REQUEST  = 'Недостаточно данных для удаления курьера'
    DELETE_COURIER_NOT_FOUND    = 'Курьера с таким id нет'
    ACCEPT_BAD_REQUEST          = 'Недостаточно данных для поиска'
    ACCEPT_ORDER_ID_NOT_FOUND   = 'Заказа с таким id не существует'
    ACCEPT_COURIER_ID_NOT_FOUND = 'Курьера с таким id не существует'
    GET_ORDER_BAD_REQUEST       = 'Недостаточно данных для поиска'
    GET_ORDER_NOT_FOUND         = 'Заказ не найден'


class RESPONSE_KEYS:
    MESSAGE_KEY = 'message'
    OK_KEY      = 'ok'
    ID_KEY      = 'id'
    LOGIN       = 'login'
    PASSWORD    = 'password'
    TRACK       = 'track'
    ORDERS      = 'orders'
    ORDER       = 'order'


class ORDER_FIELDS:
    FIRST_NAME      = 'firstName'
    LAST_NAME       = 'lastName'
    ADDRESS         = 'address'
    METRO_STATION   = 'metroStation'
    PHONE           = 'phone'
    RENT_TIME       = 'rentTime'
    DELIVERY_DATE   = 'deliveryDate'
    TRACK           = 'track'
    COLOR           = 'color'               # не обязательное ???
    COMMENT         = 'comment'

    ID              = 'id'
    CREATED_AT      = 'createdAt'
    UPDATED_AT      = 'updatedAt'
    STATUS          = 'status'
    COURIER_ID      = 'courierId'           # не обязательное
    CANCELLED       = 'cancelled'
    FINISHED        = 'finished'
    IN_DELIVERY     = 'inDelivery'
    COURIER_FIRST_NAME  = 'courierFirstName'

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

