from fastapi import APIRouter, WebSocket, WebSocketDisconnect, FastAPI
from datetime import datetime
from crewai_with_websocket.report_generator.src.report_generator.crew import ReportGenerator

router = APIRouter()
app = FastAPI()

async def run_crew(topic):
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    try:
        result = ReportGenerator().crew().kickoff(inputs=inputs)
        return {"status": "success", "result": result.raw}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.websocket("/ws/run-crew")
async def websocket_run_crew(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            topic = await websocket.receive_text()  # Wait for any message to trigger
            result = await run_crew(topic)
            await websocket.send_json(result)
    except WebSocketDisconnect:
        pass


app.include_router(router)