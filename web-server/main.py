from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import store

app = FastAPI()


@app.get("/")
def get_list():
    return [1, 2, 3, 4]


@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Soy una pagina de contact</h1>
    """


def run():
    store.get_categories()


if __name__ == "__main__":
    run()
