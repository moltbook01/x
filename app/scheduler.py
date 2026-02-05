import asyncio
from datetime import datetime, timezone


class Scheduler:
    def __init__(self, interval_seconds: float = 5.0) -> None:
        self._interval_seconds = interval_seconds
        self._task: asyncio.Task | None = None
        self._running = asyncio.Event()

    async def start(self) -> None:
        if self._task and not self._task.done():
            return
        self._running.set()
        self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        self._running.clear()
        if self._task:
            await self._task

    async def _run(self) -> None:
        while self._running.is_set():
            tick = datetime.now(timezone.utc).isoformat()
            # Placeholder for scheduled work.
            print(f"[scheduler] tick {tick}")
            await asyncio.sleep(self._interval_seconds)
