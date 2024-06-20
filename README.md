# Test-projectFastAPI1

Этот проект представляет собой REST API для управления продуктами на торговой площадке. API позволяет пользователям добавлять, обновлять, удалять и получать информацию о продуктах, а также получать информацию о категориях и фильтровать продукты по различным параметрам.

## Установка и запуск

### Предварительные условия

- Python 3.7 или выше
- pip

### Шаги по установке

1. **Клонируйте репозиторий проекта:**

   ```bash
   git clone https://github.com/Bazalter/Test-projectFastAPI1.git
   cd Test-projectFastAPI1
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Запустите сервер:**

   ```bash
   uvicorn app.main:app --reload
   ```
   ## Примеры запросов

1. **Получение списка продуктов:**

   ```bash
   curl -X GET \
     http://127.0.0.1:8000/products/ \
     -H 'accept: application/json'
   ```
2. **Создание нового продукта:**

   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/products/' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Product 1",
     "description": "Description for product 1",
     "price": 9.99,
     "category_id": 1
   }'
   ```
   
3. **Обновление продукта:**

   ```bash
   curl -X 'PUT' \
     'http://127.0.0.1:8000/products/1' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Updated Product 1",
     "description": "Updated description for product 1",
     "price": 19.99,
     "category_id": 1
   }'
   ```
   
4. **Удаление продукта:**

   ```bash
   curl -X 'DELETE' \
     'http://127.0.0.1:8000/products/1' \
     -H 'accept: application/json'
   
   curl -X DELETE \
     http://127.0.0.1:8000/products/1 \
     -H 'accept: application/json'
   ```



