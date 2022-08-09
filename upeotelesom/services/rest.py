import frappe
import json
import hashlib
import datetime
import requests


@frappe.whitelist(allow_guest=True)
def send_sms(mobile, message):

    telesom_settings = frappe.db.get_all("Telesom Settings", ['username', 'password', 'sender', 'key'])

    if len(telesom_settings) > 1:
        frappe.throw("You can only have one sender ID record in Telesom Settings.")
    else:
        username = telesom_settings[0].username
        password = telesom_settings[0].password
        sender = telesom_settings[0].sender
        curentDate = get_current_date()
        key = telesom_settings[0].key

        string = f"{username}|{password}|{mobile}|{message}|{sender}|{curentDate}|{key}"
        string = string.replace(" ", "%20")

        hashkey = hashlib.md5(string.encode()).hexdigest()
        hashkey = hashkey.upper()

        url = "https://sms.mytelesom.com/index.php/Gateway/sendsms"

        response = requests.get(f"{url}/{sender}/{message}/{mobile}/{hashkey}")

        data = json.loads(response.text)

        return data


def get_current_date():
    current_date = datetime.datetime.now()
    current_date = current_date.date()
    return current_date.strftime("%d/%m/%Y")