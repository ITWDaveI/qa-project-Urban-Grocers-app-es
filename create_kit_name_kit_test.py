from sender_stand_request import create_user
from configuration import URL_SERVICE
from data import user_data
from sender_stand_request import create_kit_for_user

def positive_assert(kit_body):
    response = create_user(URL_SERVICE, user_data)
    body = response.json()
    user_authToken = body["authToken"]
    kit_response = create_kit_for_user(URL_SERVICE, kit_body, user_authToken)
    assert kit_response.status_code == 201

def negative_assert(kit_body):
    response = create_user(URL_SERVICE, user_data)
    body = response.json()
    user_authToken = body["authToken"]
    kit_response = create_kit_for_user(URL_SERVICE, kit_body, user_authToken)
    assert kit_response.status_code == 400

def get_kit_body(kit_name):
    return { "name": kit_name}

def test01_el_numero_permitido_de_caracteres_1():
    kit_body = get_kit_body('a')
    positive_assert(kit_body)

def test02_el_numero_permitido_de_caracteres_511():
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    positive_assert(kit_body)

def test03_el_numero_de_caracteres_es_menor_que_la_cantidad_permitida_0():
    kit_body = get_kit_body('')
    negative_assert(kit_body)

def test04_el_numero_de_caracteres_es_mayor_que_la_cantidad_permitida_512():
    kit_body = get_kit_body('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    negative_assert(kit_body)

def test05_se_permiten_caracteres_especiales():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

def test06_se_permiten_espacios():
    kit_body = get_kit_body(' A Aaa ')
    positive_assert(kit_body)

def test07_se_permiten_numeros():
    kit_body = get_kit_body('123')
    positive_assert(kit_body)

def test08_el_parámetro_no_se_pasa_en_la_solicitud():
    kit_body = {}
    negative_assert(kit_body)

def test09_se_ha_pasado_un_tipo_de_parametro_diferente_numero():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)