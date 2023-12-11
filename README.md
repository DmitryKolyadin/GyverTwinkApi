# GyverTwinkApi

Модуль для управления умной адресной гирляндой [GyverTwink](https://github.com/AlexGyver/GyverTwink)

![Static Badge](https://img.shields.io/badge/DevDK-GyverTwinkApi-GyverTwinkApi)
![GitHub top language](https://img.shields.io/github/languages/top/DeveloperDmitryKolyadin/GyverTwinkApi)
![GitHub](https://img.shields.io/github/license/DeveloperDmitryKolyadin/GyverTwinkApi)
![GitHub Repo stars](https://img.shields.io/github/stars/DeveloperDmitryKolyadin/GyverTwinkApi)
![GitHub issues](https://img.shields.io/github/issues/DeveloperDmitryKolyadin/GyverTwinkApi)

## Возможности

1. Поиск устройств в локальной сети
2. Управление гирляндой
   - Включение/выключение
   - Установка яркости
   - Установка скорости
   - Смена эффектов
   - Уставнока таймера
3. Получение настроек гирлянды

## Установка

Через менеджер пакетов pip:

```bash
pip install GyverTwinkApi
```

## Использование

```python
from gyvertwink import GyverTwink

# Поиск гирлянд в локальной сети
twinks = GyverTwink.discover("192.168.0.255") # Передаём адрес локальной сети
twink = twinks[0]

# Подключение к гирлянде по ip
twink = GyverTwink("192.168.0.100")

# Включение и выключение гирлянды
twink.on()
twink.off()

# Установка яркости
twink.set_brightness(150)

# Получение текущих настроек гирлянды
settings = twink.get_settings()
print(settings)

# Переключение эффекта на следующий
twink.next_effect()

# Выбор эфекта по номеру (также возвращает словарь словарь с информацией о выбранном эффекте (favorite, scale, speed))
print(twink.select_effect(3))

# Настройка текущего эффекта
twink.set_favorite(True)
twink.set_scale(10)
twink.set_speed(20)

# Установка таймера выключение
twink.set_timer(True)
twink.set_timer_value(60) # от 1 до 240

# Установка автоматической смены режимов
twink.set_auto_change(True)
twink.set_random_change(True) # рандомная смена режимов
twink.set_change_period(True) # период смены режимов
```

## Поддержка

Если у вас возникли сложности или вопросы по использованию проекта, создайте
[обсуждение](https://github.com/DeveloperDmitryKolyadin/GyverTwinkApi/issues/new/choose) в данном репозитории или напишите мне в телеграме [@DeveloperDK](https://t.me/DeveloperDK)

## Полезные ссылки

- [GyverTwinkHA](https://github.com/DeveloperDmitryKolyadin/GyverTwinkHA) - интеграция GyverTwink в Home Assistant (Мой проект)
- [GyverTwink](https://github.com/AlexGyver/GyverTwink) - страница проекта [@AlexGyver](https://github.com/AlexGyver)