import azure.functions as func
from azure.functions import AsgiMiddleware
import api

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="{*route}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def fastapi_proxy(
    req: func.HttpRequest, context: func.Context
) -> func.HttpResponse:
    return await func.AsgiMiddleware(api.app).handle_async(req, context)