__all__ = ["XeryonXLS"]

import asyncio
from ._xeryon import Xeryon

from yaqd_core import HasTransformedPosition, IsHomeable, HasLimits, UsesUart


class XeryonXLS(HasTransformedPosition, IsHomeable, HasLimits, UsesUart):
    _kind = "xeryon-xls"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        self.controller = Xeryon(config["serial_port"], config["baud_rate"])

    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        # If there is no state to monitor continuously, delete this function
        while True:
            # Perform any updates to internal state
            self._busy = False
            # There must be at least one `await` in this loop
            # This one waits for something to trigger the "busy" state
            # (Setting `self._busy = True)
            # Otherwise, you can simply `await asyncio.sleep(0.01)`
            await self._busy_sig.wait()
