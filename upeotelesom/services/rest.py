# Copyright (c) 2022, Geoffrey Karani, Upeosoft Limited and contributors
# For license information, please see license.txt


import frappe
import requests
from upeotelesom.services.telescom_sms import UpeosoftTelesom
from frappe.core.doctype.sms_settings.sms_settings import get_headers

# def welcome_customer(doc, event):
#     mobile = frappe.db.get_value("Customer", {'name': doc.name}, ['mobile'])
#     message = "Hello and welcome to our platform"

#     message_object = UpeosoftTelesom()
#     message_object.send_sms(mobile, message)


@frappe.whitelist()
def send_test_message(mobile, message):
    try:
        message_object = UpeosoftTelesom()
        message_object.send_sms(mobile, message)

        frappe.msgprint("Test message sent successfully!")

    except Exception as e:
        frappe.throw(f"Received error response {str(e)}")
        print ("\n\n\n Received error response:%s \n\n\n" %str(e))