from fastapi import FastAPI
from src.app import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app = FastAPI(debug=True, title='Mutual Fund Returns Calculator',
              description='Mutual Fund Returns Calculator',
              versions="1.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def startup_event():
    pass  


app.include_router(router.router, tags=['Returns Calculator Api'])


