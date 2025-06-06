# 🗣️ Text-to-Speech с помощью Yandex SpeechKit

Скрипт для синтеза речи из текстового файла в аудиофайлы `.wav` с использованием Yandex SpeechKit. Удобен для озвучки длинных текстов: автоматически разбивает текст на части и сохраняет их как отдельные аудиофайлы.

## 🚀 Возможности

- Автоматическая установка необходимых зависимостей
- Поддержка длинных текстов (авторазбиение по 5000 символов)
- Удобная работа через аргументы командной строки
- Выбор имени файла для экспорта
- Использование качественного голоса `jane` с нейтральной интонацией.<br> Полный список голосов [по ссылке](https://yandex.cloud/ru/docs/speechkit/tts/voices) 


## 📦 Установка и требования

Клонируйте репозиторий:

```bash
git clone https://github.com/xivwdl/txt2speech-yandex.git
cd yandex-tts-synth
```

### Требования

Python **3.6 – 3.10**  
  > ⚠️ Библиотека [`yandex-speechkit`](https://pypi.org/project/speechkit/) официально поддерживает Python версий от **3.6 до 3.10**.  
  Использование более новых версий (3.11 и выше) может вызвать ошибки.

### Зависимости

При первом запуске скрипт сам установит `speechkit`, если она отсутствует.<br>
В случае неудачи — установите её вручную:

```python
python -m pip install speechkit
```


## 🔐 Получение API-ключа

Для работы скрипта вам нужен API-ключ от Яндекс SpeechKit. Получите его по инструкции:

👉 [Инструкция по получению API-ключа](https://yandex.cloud/ru/docs/speechkit/concepts/auth#service-account_1)

После получения ключа откройте файл `synth.py` и замените значение `api_key` на ваш:

```python
configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key='ВАШ_API_КЛЮЧ'
   )
)
```


## 🧪 Использование

### Подготовка текста:
Для более естественного произношения используйте [TTS-разметку](https://yandex.cloud/ru/docs/speechkit/tts/markup/tts-markup) исходного текста

### Пример запуска:

```bash
python synth.py --input path/to/text.txt
```

Вы также можете указать путь и имя итогового аудиофайла:

```bash
python synth.py --input path/to/text.txt --export output.wav
```

Если `--export` не указан, имя `.wav` файла будет совпадать с именем текстового файла.

Если текст слишком длинный, результат будет разбит на несколько файлов:

```
output_1.wav
output_2.wav
...
```

## 📄 Лицензия
MIT License
