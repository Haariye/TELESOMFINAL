# Copyright (c) 2022, Geoffrey Karani, Upeosoft Limited and contributors
# For license information, please see license.txt

import frappe
import json
import hashlib
import datetime
import requests


class UpeosoftTelesom:
    def __init__(self):
        telesom_settings = frappe.db.get_all("Telesom Settings", ['username', 'password', 'sender', 'key'])

        if len(telesom_settings) > 1:
            frappe.throw("You can only have one sender ID record in Telesom Settings.")
        else:
            self.username = telesom_settings[0].username
            self.password = telesom_settings[0].password
            self.sender = telesom_settings[0].sender
            self.curentDate = self.get_current_date()
            self.key = telesom_settings[0].key


    def send_sms(self, mobile, message):
        string = f"{self.username}|{self.password}|{mobile}|{message}|{self.sender}|{self.curentDate}|{self.key}"
        string = string.replace(" ", "%20")

        hashkey = hashlib.md5(string.encode()).hexdigest()
        hashkey = hashkey.upper()

        url = "https://sms.mytelesom.com/index.php/Gateway/sendsms"

        response = requests.get(f"{url}/{self.sender}/{message}/{mobile}/{hashkey}")

        data = json.loads(response.text)

        print(f"\n\n\n {data} \n\n\n")

        return data


    def get_current_date(self):
        current_date = datetime.datetime.now()
        current_date = current_date.date()
        return current_date.strftime("%d/%m/%Y")