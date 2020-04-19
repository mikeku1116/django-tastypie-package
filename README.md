# django-tastypie-package #

## 專案介紹 ##

本專案使用Django tastypie套件，來開發具有基本功能的RESTful API，其中以簡單的查詢音樂清單API為範例，來瞭解Django tastypie套件的使用方式，可以搭配[[Django教學12]利用輕量的Django tastypie來打造屬於自己的API](https://www.learncodewithmike.com/2020/04/django-tastypie.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行方式 ##

啟動本地端伺服器後，接著即可利用專案中的doc.http檔案，來進行API的請求練習。