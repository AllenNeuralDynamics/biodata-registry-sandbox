import base64
import json
from typing import Optional
import logging

def encode_next_token(item_id: int) -> str:
    """Encodes the item ID into a secure, opaque continuation token."""
    token_str = json.dumps({"id": item_id})
    return base64.b64encode(token_str.encode('utf-8')).decode('utf-8')

def decode_next_token(token: str) -> Optional[int]:
    """Decodes the continuation token back into an item ID."""
    if not token:
        return None
    try:
        token_str = base64.b64decode(token.encode('utf-8')).decode('utf-8')
        data = json.loads(token_str)
        return data.get("id")
    except Exception as e:
        logging.error(e)
        return None