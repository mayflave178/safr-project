# Сборка SAFR под Windows

## 1. Подготовка окружения

```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -r build_requirements.txt
```

## 2. Проверка из исходников

```cmd
python main.py --headless
python main.py
```

## 3. Сборка

```cmd
pyinstaller safr.spec --clean --noconfirm
```

## 4. Запуск

`dist\SAFR\SAFR.exe`

Рядом с exe автоматически создаются `exports\`, `logs\`,
`user_plugins\signals\`, `user_plugins\filters\`. Папку `dist\SAFR\`
можно переносить на другие Windows-машины целиком (Python там не нужен).

## 5. Ограничения сборки

* Сборка работает только на той ОС, где выполнена (нет кросс-компиляции).
* Размер бандла ~300–400 МБ (PySide6 + matplotlib).
* UPX не применяется — конфликтует с DLL PySide6.
* Не размещать exe в `C:\Program Files\` — нужны права на запись рядом.