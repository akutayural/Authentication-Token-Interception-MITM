import json
import logging

from mitmproxy import http
import redis
from mitmproxy.log import ALERT

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class InterceptBackendAuthToken:
    def __init__(self):
        try:
            self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
            logger.info("Proxy script started.")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")

    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_url == "https://user-auth-crru.onrender.com/oauth/token":
            logger.info("Backend server OAuth token request intercepted.")

    def response(self, flow: http.HTTPFlow) -> bool:
        if flow.request.pretty_url == "https://user-auth-crru.onrender.com/oauth/token":
            logger.info("Backend server OAuth token response intercepted.")

            # Parse JSON response to extract the access token
            try:
                data = json.loads(flow.response.text)
                access_token = data.get('access_token')

                if access_token:
                    # Log the token for debugging
                    logger.log(ALERT, f"Captured Access Token: {access_token}")

                    # Store the token in Redis
                    redis_key = "backend_access_token"
                    self.redis_client.set(redis_key, access_token)
                    logger.info(f"Access token stored in Redis with key: {redis_key}")
                    return True
                else:
                    logger.error("Access token not found in the response.")
                    return False

            except json.JSONDecodeError as e:
                logger.error(f"Error decoding JSON from response: {e}")
                return False
            except Exception as e:
                logger.error(f"Error processing the backend server response: {e}")
                return False

    def __del__(self):
        try:
            logger.info("Proxy script stopped.")
            self.redis_client.close()
        except Exception as e:
            print(f"Failed to close Redis connection: {e}")


addons = [
    InterceptBackendAuthToken()
]