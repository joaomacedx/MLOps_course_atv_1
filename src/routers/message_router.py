from fastapi import APIRouter
from models.message_model import MessageModel
from services.classifier_service import ClassifierService
from services.date_or_day_service import DateOrDayService


router = APIRouter()
classifier = ClassifierService()

@router.post("/message")
async def message(message: MessageModel):
    classified_message = classifier.classify_text(message.text)
    response = DateOrDayService.get_response(classified_message)
    return {"response": response}