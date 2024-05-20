from fastapi import FastAPI
import uvicorn
import routers.message_router as message_router
app = FastAPI()

app.include_router(message_router.router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)