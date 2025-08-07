from httpx import Request, Response

from utils.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def log_request_event_hook(request: Request):
    """
    Логирует информацию об отправленном HTTP-запросе.
    :param request: Объект запроса HTTPX.
    """
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    """
    Логирует информацию о полученном HTTP-ответе.
    :param response: Объект ответа HTTPX.
    """
    logger.info(f"Response {response.status_code}"
                f" {response.reason_phrase} from {response.url}")
