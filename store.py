import os
from sqlite_store import SQLiteStore


def build_store_from_env():
    """
    SQLite 전용 저장소 생성. 실패 시 None 반환.
    - STORAGE_BACKEND는 무시하고, SQLITE_PATH만 사용합니다.
    """
    try:
        store = SQLiteStore()
        return store if store.enabled else None
    except Exception:
        return None
