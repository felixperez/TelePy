# -*- coding: utf-8 -*-
import os
import commands
import telebot
import random
from telebot import types

TOKEN = 'AQUI PONED EL TOKEN'
bot = telebot.TeleBot(TOKEN)
"""Empieza el codigo del bueno Primero aniadimos un listener para que nos muestre 
en pantalla de la rasp todo lo que se envia al bot, lo podemos quitar pues no es necesairo"""
def listener(mensajes):
 	for m in mensajes:
		chat_id = m.chat.id
		texto = m.text
		print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto)
# Ahora tenemos el codigo que es el que nos mira el texto
def get_user_step(cid):
	return userStep.get(cid)

# Funcion para ocultar el teclado
ocultarTeclado = types.ReplyKeyboardHide()
reply_markup=ocultarTeclado
"""Con el reply_markup lo que hacemos es llamar a la funcion, esto lo podemos poner
en cualquier handler, en el que despues de hacer una accion, queramos cerrar dicho teclado,
como por ejemplo en un bot.send_message(chat_id, reply_markup=ocultarTeclado)
""" 
bot.set_update_listener(listener)
@bot.message_handler(commands=['foto'])
def captura(m):
	cid = m.chat.id
	caption = open ('/direccion/donde/tengamos/alojada/la/foto.jpg.png...')
	bot.send_photo(cid,caption)

@bot.message_handler(commands=['ex'])
def command_long_text(m):
    cid = m.chat.id
    if cid == MI NUMERO DE TELEGRAM: """Aqui tenemos que poner el numero que tenemos en teelgram, nuestro "DNI" """ 
	bot.send_message(cid, "Ejecutando: "+m.text[len("/exec"):])
	bot.send_chat_action(cid, 'typing') # show the bot "typing" (max. 5 secs)
   	f = os.popen(m.text[len("/exec"):])
    	result = f.read()
    	bot.send_message(cid, "Resultado: "+result)
    else: 
	bot.send_message(cid, 'No tienes permiso para ejecutar comandos... >:(')
"""ahora que nos responda a un hola"""
@bot.message_handler(commands=['hola'])
def comando_hola(mensaje):
	chat_id = mensaje.chat.id
	bot.send_message(chat_id, 'Te digo Hola desde la rasp')

@bot.message_handler(commands=['chao'])
def comando_chao(mensaje):
	chat_id = mensaje.chat.id
	bot.send_message(chat_id, 'Te digo Chao desde la rasp')

@bot.message_handler(commands=['random','Random'])
def comando_alex(mensaje):
	chat_id = mensaje.chat.id
	lista = [str(random.randint(0,21361287361278637182367182378)),'Hola']
	bot.send_message(chat_id, random.choice(lista))

@bot.message_handler(commands=['start'])
def comando_start(mensaje):
	chat_id = mensaje.chat.id
	bot.send_message(chat_id,"Espero servirle estupendamente, señorito")
	bot.send_message(chat_id,"Si quieres tener la botonera con la prueba de todos los botones, escribe /test")
@bot.message_handler(commands=['test'])
def com_test(mensaje):
	chat = mensaje.chat.id
	markup = types.ReplyKeyboardMarkup()
	itembtn1 = types.KeyboardButton('/random')
	itembtn2 = types.KeyboardButton('/hola')
	itembtn3 = types.KeyboardButton('hi')
	itembtn4 = types.KeyboardButton('no comando')
	itembtn5 = types.KeyboardButton('/chao')
	itembtn6 = types.KeyboardButton('/temp')
	itembtn7 = types.KeyboardButton('/foto')
	markup.row(itembtn1, itembtn2)
	markup.row(itembtn3, itembtn4, itembtn5)
	markup.row(itembtn6)
	markup.row(itembtn7)
	bot.send_message(chat,"Selecciona una accion:", reply_markup=markup)
"""Lanzamos la lectura de la temperatura, luego calculamos unos cuantos digitos de PI y lanzamos de nuevo la lectura de la temperatura
recordad que esto es para la raspberry por lo que en otros sitemas tendreis que mirar donde teneis alojados
las lecturas de dichas temperaturas"""
@bot.message_handler(commands=['temp'])
def pi(mensaje):
	for i in range(1):
		tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
		cpu_temp = tempFile.read()
		tempFile.close()
		chat_id = mensaje.chat.id
		ftemp = float(cpu_temp)/1000
		bot.send_message(chat_id,"Temperatura inicial: " + str(ftemp) + 'ºC')	
		bot.send_message(chat_id,'Tardo unos 5 segundos en calcular :(')
		os.system('/usr/bin/python pi.py')
		tempFile2 = open('/sys/class/thermal/thermal_zone0/temp')
		cpu_temp2 = tempFile2.read()
		tempFile.close()
		fftemp = float(cpu_temp2)/1000
		bot.send_message(chat_id,'Temperatura despues de calcular PI: ' +str(fftemp) + 'ºC')

#Funcion para que en caso de recibir un mensaje que no entendemos, que nos conteste
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Yeee! Hola a ti tambien")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "No entiendo a que te refiers con \"" + m.text + "\"\nIntenta poner un comando aceptado :D ")

bot.polling()
