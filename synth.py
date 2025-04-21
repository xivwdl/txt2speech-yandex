from argparse import ArgumentParser

# Попытаемся импортировать библиотеки, и если они отсутствуют, установим их
try:
    from speechkit import model_repository, configure_credentials, creds
except ImportError:
    print("Необходимые библиотеки не установлены. Устанавливаю их...")
    try:
        import subprocess
        subprocess.check_call(["pip", "install", "yandex-speechkit"])
        from speechkit import model_repository, configure_credentials, creds
        print("Библиотеки успешно установлены.")
    except Exception as e:
        print(f"Ошибка при установке библиотек: {e}")
        exit(1)

# Аутентификация через API-ключ.
configure_credentials(
   yandex_credentials=creds.YandexCredentials(
      api_key='ВАШ_API_КЛЮЧ'
   )
)

def synthesize(input_text, export_path=None):
    model = model_repository.synthesis_model()

    # Задайте настройки синтеза.
    model.voice = 'jane'
    model.role = 'neutral'

    # Считываем текст из файла
    with open(input_text, 'r', encoding='utf-8') as text_file:
        text_to_synthesize = text_file.read()

    # Определите имя файла без расширения (без .txt)
    import os
    base_filename = os.path.splitext(os.path.basename(input_text))[0]

    # Если export_path не указан, используем имя файла с текстом для сохранения
    if export_path is None:
        export_path = f"{base_filename}.wav"

    # Разбиение текста на части
    MAX_SIZE = 5000
    parts = []
    current_part = ""
    for sentence in text_to_synthesize.split('.'):
        if len(current_part) + len(sentence) < MAX_SIZE:
            current_part += sentence + '.'
        else:
            parts.append(current_part)
            current_part = sentence + '.'
    if current_part:
        parts.append(current_part)

    # Синтез речи для каждой части
    for index, part in enumerate(parts):
        result = model.synthesize(part, raw_format=False)
        part_export_path = f"{export_path[:-4]}_{index + 1}.wav"
        result.export(part_export_path, 'wav')

if __name__ == '__main__':
   parser = ArgumentParser()
   parser.add_argument('--input', type=str, help='input text file', required=True)
   parser.add_argument('--export', type=str, help='export path for synthesized audio', required=False)

   args = parser.parse_args()

   synthesize(args.input, args.export)
