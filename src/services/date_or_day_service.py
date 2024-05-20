from datetime import datetime
import locale
import constants.constants as ct
class DateOrDayService:
    @staticmethod
    def get_response(prediction: str) -> str:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        now = datetime.now()
        if prediction == ct.DAY:
            return now.strftime('%A')
        elif prediction == ct.HOUR:
            return now.strftime('%d/%m/%Y %H:%M')