# <p align="center"> Alisa bot
  
  
<p align="center">Telegram bot for user
  <p align="center">A simple, but extensible Python implementation for the <a href="https://core.telegram.org/bots/api">Telegram Bot API</a>.
    
    
[![PyPi Package Version](https://img.shields.io/pypi/v/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Build Status](https://travis-ci.org/eternnoir/pyTelegramBotAPI.svg?branch=master)](https://travis-ci.org/eternnoir/pyTelegramBotAPI)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTelegramBotAPI.svg)](https://pypi.org/project/pyTelegramBotAPI/)    

* [Описание.](#getting-started)
  * [Writing your first bot](#writing-your-first-bot)
    * [Prerequisites](#prerequisites)
    * [A simple echo bot](#a-simple-echo-bot)
  * [General API Documentation](#general-api-documentation)
    * [Types](#types)
    * [Methods](#methods)
    * [General use of the API](#general-use-of-the-api)
      * [Message handlers](#message-handlers)
      * [Callback Query handlers](#callback-query-handler)
      * [Middleware handlers](#middleware-handler)
      * [TeleBot](#telebot)
      * [Reply markup](#reply-markup)
      * [Inline Mode](#inline-mode)
  * [Advanced use of the API](#advanced-use-of-the-api)
    * [Asynchronous delivery of messages](#asynchronous-delivery-of-messages)
    * [Sending large text messages](#sending-large-text-messages)
    * [Controlling the amount of Threads used by TeleBot](#controlling-the-amount-of-threads-used-by-telebot)
    * [The listener mechanism](#the-listener-mechanism)
    * [Using web hooks](#using-web-hooks)
    * [Logging](#logging)
    * [Proxy](#proxy)
  * [API conformance](#api-conformance)
  * [Change log](#change-log)
  * [F.A.Q.](#faq)
    * [Bot 2.0](#bot-20)
    * [How can I distinguish a User and a GroupChat in message.chat?](#how-can-i-distinguish-a-user-and-a-groupchat-in-messagechat)
    * [How can I handle reocurring ConnectionResetErrors?](#how-can-i-handle-reocurring-connectionreseterrors)
  * [The Telegram Chat Group](#the-telegram-chat-group)
  * [More examples](#more-examples)
  * [Bots using this API](#bots-using-this-api)
	  
	  
## Описание.

Бот предназначен для демонстрации навыков, возможностей и знаний автора где используются авторские библиотеки монетизацию которых автор не претендует!
Простой телеграм бот в которого будут входить функции пересылка первого абзаца с Википедии и информацию о погоде в районном центре или обл центре в режиме реального времени. 

## Профилактика. 
Библиотеки могут конфликтовать между собой поетому я рекомендую на новосозданую виртуальную среду накатить следующие :	  

	  pip3 install --upgrade pip
	  
	  pip3 install --upgrade setuptools pip
	  
	  pip install --upgrade setuptools pip


Данный набор библиотек тестировался на Python 3.9-3.10
 Важно устанавливать на Python 3 через pip3
	 
	  pip3 install selenium
	 
	  pip3 install wikipedia
	
	  pip3 install pyowm
	 
	  pip3 install googletrans==3.1.0a0
	 
	  pip3 install PyTelegramBotApi

Если возникнет ошибка с телеграм бот API убедись нет ли у тебя сторонней библеотеки для работы с телеграмом и введи следующие

	  
	  pip3 uninstall pytelegrambotapi
	  
	  pip3 install --no-cache-dir pytelegrambotapi



	  
	  
	  
This API is tested with Python Python 3.6-3.9 and Pypy 3.
There are two ways to install the library:

* Installation using pip (a Python package manager)*:

```
$ pip install pyTelegramBotAPI
```
* Installation from source (requires git):

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```

It is generally recommended to use the first option.

**While the API is production-ready, it is still under development and it has regular updates, do not forget to update it regularly by calling `pip install pytelegrambotapi --upgrade`*

## Writing your first bot

### Prerequisites
