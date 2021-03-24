from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise


app = FastAPI()


@app.get('/')
def index():
    return 'Hi!'


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['app.users.models']},
    generate_schemas=True,
    add_exception_handlers=True
)