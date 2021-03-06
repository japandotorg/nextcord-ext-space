from ..op import OpDetails

class BaseRecorder:
    started: bool
    async def start(self) -> None: ...
    async def end(self) -> None: ...
    async def last_events_id(self) -> int: ...
    async def save_events(self, name: str, payload: dict, *, unknown: bool) -> None: ...
    async def save_packets(self, op_code: str, details: OpDetails) -> None: ...