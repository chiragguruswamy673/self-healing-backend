from fastapi import FastAPI
import random
import time

app = FastAPI()   # 👈 THIS MUST EXIST

@app.get("/health")
def health_check():
    if random.randint(1, 5) == 3:
        return {"status": "DOWN"}
    return {"status": "UP"}

@app.get("/critical")
def critical_service():
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "Critical service running"}

