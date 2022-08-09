# Copyright (c) 2022, Geoffrey Karani, Upeosoft Limited and contributors
# For license information, please see license.txt


# import frappe
# from upeotelesom.services.telescom_sms import UpeosoftTelesom

# def welcome_customer(doc, event):
#     mobile = frappe.db.get_value("Customer", {'name': doc.name}, ['mobile'])
#     message = "Hello and welcome to our platform"

#     message_object = UpeosoftTelesom()
#     message_object.send_sms(mobile, message)