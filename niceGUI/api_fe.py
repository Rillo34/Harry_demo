import httpx
from nicegui import ui
import os 

class APIController:
    BASE = os.getenv("API_BASE", "http://localhost:8100")  # Docker backend service name

    def __init__(self, controller=None):
        self.controller = controller

    async def _request(self, method, endpoint, *, params=None, json=None, files=None, timeout=30):
        url = f"{self.BASE.rstrip('/')}/{endpoint.lstrip('/')}"
        print(f"➡️ Request: {method} {url}")

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json,
                    files=files,
                )

            if response.status_code != 200:
                ui.notify(f"Backend error {response.status_code}", type="warning")
                return None

            return response.json()

        except Exception as e:
            print("❌ Network error:", e)
            ui.notify(f"Nätverksfel: {e}", type="warning")
            return None

    # -----------------------------
    # DEMO ENDPOINTS
    # -----------------------------

    async def ping(self):
        return await self._request("GET", "/api/ping")

    async def echo(self, payload: dict):
        return await self._request("POST", "/api/echo", json=payload)


class UploadController:
    """Minimal placeholder so app_state.py does not break."""
    pass

