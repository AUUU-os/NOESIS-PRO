from fastapi import FastAPI
app = FastAPI()

@app.get('/live')
def live():
    return {'runtime':'active','drift':'low'}
