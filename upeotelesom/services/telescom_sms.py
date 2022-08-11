# Copyright (c) 2022, Geoffrey Karani, Upeosoft Limited and contributors
# For license information, please see license.txt

import frappe
import json
import hashlib
import datetime
import requests


class UpeosoftTelesom:
    def __init__(self):
        try:
            self.username = frappe.db.get_value('SMS Parameter', {'parameter': 'usermname'}, ['value'])
            self.password = frappe.db.get_value('SMS Parameter', {'parameter': 'password'}, ['value'])
            self.sender = frappe.db.get_value('SMS Parameter', {'parameter': 'sender'}, ['value'])
            self.key = frappe.db.get_value('SMS Parameter', {'parameter': 'key'}, ['value'])

            self.curentDate = self.get_current_date()

        except Exception as e:
            frappe.throw(f"Received error response {str(e)}")
            print ("\n\n\n Received error response:%s \n\n\n" %str(e))

        


    def send_sms(self, mobile, message):
        try:
            string = f"{self.username}|{self.password}|{mobile}|{message}|{self.sender}|{self.curentDate}|{self.key}"
            string = string.replace(" ", "%20")

            hashkey = hashlib.md5(string.encode()).hexdigest()
            hashkey = hashkey.upper()

            url = "https://sms.mytelesom.com/index.php/Gateway/sendsms"

            response = requests.get(f"{url}/{self.sender}/{message}/{mobile}/{hashkey}")

            data = json.loads(response.text)

            print(f"\n\n\n { response.status_code } \n\n\n")

            return response

            return data

        except Exception as e:
            frappe.throw(f"Received error response {str(e)}")
            print ("\n\n\n Received error response:%s \n\n\n" %str(e))


    def get_current_date(self):
        try:
            current_date = datetime.datetime.now()
            current_date = current_date.date()
            return current_date.strftime("%d/%m/%Y")
        except Exception as e:
            frappe.throw(f"Received error response {str(e)}")
            print ("\n\n\n Received error response:%s \n\n\n" %str(e))