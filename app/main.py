from fastapi import FastAPI

app = FastAPI(
    title="Health Navigator AI",
    description="AI-powered Personal Health Assistant",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Health Navigator AI 🚀"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}